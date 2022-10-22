from apis.dm_api_account.apis import LoginApi, AccountApi


class DmApiAccount:
    def __init__(self, host, headers=None, proxies=None):
        self.account = AccountApi(host=host, headers=headers, proxies=proxies)
        self.login = LoginApi(host=host, headers=headers, proxies=proxies)

    def set_headers(self, api_name, headers):
        self.__getattribute__(api_name).client.headers = headers
