from apis.dm_api_account.models.account import RegistrationRequestModel


def test_v1_account(dm_account_api):
    response = dm_account_api.account.post_v1_account(
        status_code=201,
        registration_request_model=RegistrationRequestModel(
            login='test_user_1',
            email='test_user_1@mail.ru',
            password='test_user_1'
        )
    )
