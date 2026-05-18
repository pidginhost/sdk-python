"""
PidginHost API Client

Simple wrapper around the generated SDK.

Usage:
    from pidginhost_sdk.client import PidginHost

    client = PidginHost("your-api-token")
    servers = client.cloud.cloud_servers_list()
    keys = client.account.account_ssh_keys_list()
"""

from pidginhost_sdk.api.account_api import AccountApi
from pidginhost_sdk.api.auth_api import AuthApi
from pidginhost_sdk.api.billing_api import BillingApi
from pidginhost_sdk.api.cloud_api import CloudApi
from pidginhost_sdk.api.dedicated_api import DedicatedApi
from pidginhost_sdk.api.domain_api import DomainApi
from pidginhost_sdk.api.freedns_api import FreednsApi
from pidginhost_sdk.api.hosting_api import HostingApi
from pidginhost_sdk.api.kubernetes_api import KubernetesApi
from pidginhost_sdk.api.support_api import SupportApi
from pidginhost_sdk.api_client import ApiClient
from pidginhost_sdk.configuration import Configuration


class PidginHost:
    """PidginHost API client.

    Args:
        token: API authentication token.
        host: Override the default API host.
    """

    def __init__(self, token: str, host: str | None = None):
        self._configuration = Configuration()
        if host is not None:
            self._configuration.host = host
        self._configuration.api_key["tokenAuth"] = token
        self._configuration.api_key_prefix["tokenAuth"] = "Token"
        self._api_client = ApiClient(self._configuration)

        self.account = AccountApi(self._api_client)
        self.auth = AuthApi(self._api_client)
        self.billing = BillingApi(self._api_client)
        self.cloud = CloudApi(self._api_client)
        self.dedicated = DedicatedApi(self._api_client)
        self.domain = DomainApi(self._api_client)
        self.freedns = FreednsApi(self._api_client)
        self.hosting = HostingApi(self._api_client)
        self.kubernetes = KubernetesApi(self._api_client)
        self.support = SupportApi(self._api_client)

    def close(self):
        self._api_client.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()
