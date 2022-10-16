from commons.restclient.restclient import RestClient
from apis.dm_api_account.models.account import RegistrationRequestModel, UserDetailsEnvelopeResponseModel
from requests import Response


class AccountApi:
    def __init__(self, host, headers=None, proxies=None):
        self.host = host
        self.headers = headers
        self.proxies = proxies
        self.client = RestClient(
            host=self.host,
            headers=self.headers,
            proxies=self.proxies,
        )

    @staticmethod
    def _check_status_code(response, status_code):
        response_status_code = response.status_code
        assert response_status_code == status_code, \
            f'Status code should be {status_code}, but got {response_status_code}'

    def post_v1_account(
            self,
            registration_request_model: RegistrationRequestModel,
            status_code: int = 200
    ) -> Response:
        """
        Register new user
        :param registration_request_model: json data
        :param status_code: check status code
        :return: requests.Response
        """
        response = self.client.post(
            path=f'/v1/account',
            json=registration_request_model.to_struct()
        )
        self._check_status_code(response, status_code)
        return response

    def get_v1_account(
            self,
            status_code: int = 200
    ) -> UserDetailsEnvelopeResponseModel:
        """
        Get current user
        :param status_code: check status code
        :return: UserDetailsEnvelopeResponseModel
        """
        response = self.client.get(path=f'/v1/account')
        response_json = response.json()
        self._check_status_code(response, status_code)
        return UserDetailsEnvelopeResponseModel(**response_json)

    def put_v1_account_token(
            self,
            token: str,
            status_code: int = 200
    ):
        """
        Activate registered user
        :param token: activation token from registration email
        :param status_code: check status code
        :return: UserDetailsEnvelopeResponseModel
        """
        response = self.client.put(path=f'/v1/account/{token}')
        response_json = response.json()
        self._check_status_code(response, status_code)
        return UserDetailsEnvelopeResponseModel(**response_json)