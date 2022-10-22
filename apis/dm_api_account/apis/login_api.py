import requests

from apis.dm_api_account.models.account import UserEnvelopeResponseModel
from apis.dm_api_account.models.login import LoginCredentialsRequestModel
from commons.restclient.restclient import RestClient


class LoginApi:
    def __init__(self, host, headers=None, proxies=None):
        self._host = host
        self._headers = headers
        self._proxies = proxies
        self.client = RestClient(
            host=self._host,
            headers=self._headers,
            proxies=self._proxies,
        )

    def set_headers(self, headers):
        self.client.headers = headers

    @staticmethod
    def _check_status_code(response, status_code):
        response_status_code = response.status_code
        if status_code:
            assert response_status_code == status_code, \
                f'Status code should be {status_code}, but got {response_status_code}'

    def post_v1_account_login(
            self,
            login_credentials_request_model: LoginCredentialsRequestModel,
            status_code: int = None,
            _full_response: bool = False,
    ) -> UserEnvelopeResponseModel | requests.Response:
        """
        Authenticate via credentials
        :param login_credentials_request_model: json data
        :param status_code: check status code
        :param _full_response: return request.Response
        :return: UserEnvelopeResponseModel | request.Response
        """
        response = self.client.post(
            path=f'/v1/account/login',
            json=login_credentials_request_model.to_struct()
        )
        self._check_status_code(response, status_code)
        if _full_response:
            return response

        return UserEnvelopeResponseModel(**response.json())
