from commons.restclient.restclient import RestClient
from apis.dm_api_account.models.account import RegistrationRequestModel, UserDetailsEnvelopeResponseModel, \
    UserEnvelopeResponseModel, ResetPasswordRequestModel, ChangePasswordRequestModel, ChangeEmailRequestModel
from requests import Response


class AccountApi:
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

    def post_v1_account(
            self,
            registration_request_model: RegistrationRequestModel,
            status_code: int = 200,
            **kwargs
    ) -> Response:
        """
        Register new user
        :param registration_request_model: json data
        :param status_code: check status code
        :return: requests.Response
        """
        response = self.client.post(
            path=f'/v1/account',
            json=registration_request_model.to_struct(),
            **kwargs
        )
        self._check_status_code(response, status_code)
        return response

    def get_v1_account(
            self,
            status_code: int = 200,
            **kwargs
    ) -> UserDetailsEnvelopeResponseModel:
        """
        Get current user
        :param status_code: check status code
        :return: UserDetailsEnvelopeResponseModel
        """
        response = self.client.get(path=f'/v1/account', **kwargs)
        response_json = response.json()
        self._check_status_code(response, status_code)
        return UserDetailsEnvelopeResponseModel(**response_json)

    def put_v1_account_token(
            self,
            token: str,
            status_code: int = 200,
            **kwargs
    ) -> UserEnvelopeResponseModel:
        """
        Activate registered user
        :param token: activation token from registration email
        :param status_code: check status code
        :return: UserEnvelopeResponseModel
        """
        response = self.client.put(path=f'/v1/account/{token}', **kwargs)
        response_json = response.json()
        self._check_status_code(response, status_code)
        return UserEnvelopeResponseModel(**response_json)

    def post_v1_account_password(
            self,
            reset_password_request_model: ResetPasswordRequestModel,
            status_code: int = 200,
            **kwargs
    ) -> UserEnvelopeResponseModel:
        """
        Reset registered user password
        :param reset_password_request_model: json data
        :param status_code: check status code
        :return: UserEnvelopeResponseModel
        """
        response = self.client.post(
            path=f'/v1/account/password',
            json=reset_password_request_model.to_struct(),
            **kwargs
        )
        response_json = response.json()
        self._check_status_code(response, status_code)
        return UserEnvelopeResponseModel(**response_json)

    def put_v1_account_password(
            self,
            change_password_request_model: ChangePasswordRequestModel,
            status_code: int = 200,
            **kwargs
    ) -> UserEnvelopeResponseModel:
        """
        Change registered user password
        :param change_password_request_model: json data
        :param status_code: check status code
        :return: UserEnvelopeResponseModel
        """
        response = self.client.put(
            path=f'/v1/account/password',
            json=change_password_request_model.to_struct(),
            **kwargs
        )
        response_json = response.json()
        self._check_status_code(response, status_code)
        return UserEnvelopeResponseModel(**response_json)

    def put_v1_account_email(
            self,
            change_email_request_model: ChangeEmailRequestModel,
            status_code: int = 200,
            **kwargs
    ) -> UserEnvelopeResponseModel:
        """
        Change registered user email
        :param change_email_request_model: json data
        :param status_code: check status code
        :return: UserEnvelopeResponseModel
        """
        response = self.client.put(
            path=f'/v1/account/email',
            json=change_email_request_model.to_struct(),
            **kwargs
        )
        response_json = response.json()
        self._check_status_code(response, status_code)
        return UserEnvelopeResponseModel(**response_json)
