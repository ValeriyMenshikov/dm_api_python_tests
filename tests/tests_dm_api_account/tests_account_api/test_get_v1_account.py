from apis.dm_api_account.models.login import LoginCredentialsRequestModel


def test_get_v1_account(dm_account_api):
    response = dm_account_api.login.post_v1_account_login(
        login_credentials_request_model=LoginCredentialsRequestModel(
            login='test_user_1',
            password='test_user_1',
            remember_me=True
        ),
        _full_response=True
    )

    dm_account_api.account.set_headers(
        headers={'X-Dm-Auth-Token': response.headers['X-Dm-Auth-Token']}
    )
    response = dm_account_api.account.get_v1_account()