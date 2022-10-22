import json
import re
import time
from commons.restclient.restclient import RestClient


def retrier(attempts=10):
    def get_function(fn):
        def get_args(*args, **kwargs):
            for attempt in range(1, attempts + 1):
                response = fn(*args, **kwargs)
                print(f'Попытка выполнить запрос {attempt}')
                time.sleep(2)
                if response.status_code == 200:
                    return response
            raise AssertionError(f"Не удалось выполнить запрос, в течении {attempts} попыток")

        return get_args

    return get_function


class MailHogClient:
    def __init__(self, host, headers=None):
        self.headers = headers
        self.host = host
        self.client = RestClient(
            host=self.host,
            headers=self.headers
        )

    @retrier(10)
    def get_all_email(self, limit=50):
        params = {
            'limit': str(limit),
        }
        response = self.client.get(
            path=f'/api/v2/messages',
            params=params
        )
        return response

    def get_email_by_user_name(self, user_name):
        emails = [_ for _ in self.get_all_email().json()['items'] if user_name in str(_)]
        return emails

    def get_token_from_email(self, email):
        token = json.loads(email['Content']['Body'])['ConfirmationLinkUrl'].split('/')[-1]
        return token

    def get_token_from_last_email(self):
        emails = self.get_all_email(limit=1)
        token = json.loads(emails.json()['items'][0]['Content']['Body'])['ConfirmationLinkUrl'].split('/')[-1]
        return token

    def get_token(self, user, token_type):
        response = self.get_all_email()
        token = None
        for email in response.json()['items']:
            content = json.loads(email['Content']['Body'])
            if re.findall(f'ConfirmationLinkUrl.*{token_type}', str(content)):
                if content['Login'] == user:
                    token = content['ConfirmationLinkUrl'].split('/')[-1]
        return token

    def delete_email_by_id(self, email_id):
        response = self.client.delete(
            path=f'/api/v1/messages/{email_id}',
        )
        return response

    def delete_all_emails(self):
        response = self.client.delete(
            path=f'/api/v1/messages',
        )
        return response
