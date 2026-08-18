# pidginhost_sdk.EmailApi

All URIs are relative to *https://www.pidginhost.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**email_api_credentials_create**](EmailApi.md#email_api_credentials_create) | **POST** /api/email/api_credentials/ | 
[**email_api_credentials_destroy**](EmailApi.md#email_api_credentials_destroy) | **DELETE** /api/email/api_credentials/{id}/ | 
[**email_api_credentials_list**](EmailApi.md#email_api_credentials_list) | **GET** /api/email/api_credentials/ | 
[**email_api_credentials_retrieve**](EmailApi.md#email_api_credentials_retrieve) | **GET** /api/email/api_credentials/{id}/ | 
[**email_domains_create**](EmailApi.md#email_domains_create) | **POST** /api/email/domains/ | 
[**email_domains_inbound_routes_create**](EmailApi.md#email_domains_inbound_routes_create) | **POST** /api/email/domains/{domain_pk}/inbound_routes/ | 
[**email_domains_inbound_routes_list**](EmailApi.md#email_domains_inbound_routes_list) | **GET** /api/email/domains/{domain_pk}/inbound_routes/ | 
[**email_domains_list**](EmailApi.md#email_domains_list) | **GET** /api/email/domains/ | 
[**email_domains_retrieve**](EmailApi.md#email_domains_retrieve) | **GET** /api/email/domains/{id}/ | 
[**email_domains_rotate_dkim_create**](EmailApi.md#email_domains_rotate_dkim_create) | **POST** /api/email/domains/{id}/rotate_dkim/ | 
[**email_domains_toggle_inbound_create**](EmailApi.md#email_domains_toggle_inbound_create) | **POST** /api/email/domains/{id}/toggle_inbound/ | 
[**email_domains_verify_create**](EmailApi.md#email_domains_verify_create) | **POST** /api/email/domains/{id}/verify/ | 
[**email_inbound_routes_create**](EmailApi.md#email_inbound_routes_create) | **POST** /api/email/inbound_routes/ | 
[**email_inbound_routes_destroy**](EmailApi.md#email_inbound_routes_destroy) | **DELETE** /api/email/inbound_routes/{id}/ | 
[**email_inbound_routes_list**](EmailApi.md#email_inbound_routes_list) | **GET** /api/email/inbound_routes/ | 
[**email_inbound_routes_partial_update**](EmailApi.md#email_inbound_routes_partial_update) | **PATCH** /api/email/inbound_routes/{id}/ | 
[**email_inbound_routes_retrieve**](EmailApi.md#email_inbound_routes_retrieve) | **GET** /api/email/inbound_routes/{id}/ | 
[**email_messages_retrieve**](EmailApi.md#email_messages_retrieve) | **GET** /api/email/messages/{message_id}/ | 
[**email_sandbox_addresses_create**](EmailApi.md#email_sandbox_addresses_create) | **POST** /api/email/sandbox_addresses/ | 
[**email_sandbox_addresses_destroy**](EmailApi.md#email_sandbox_addresses_destroy) | **DELETE** /api/email/sandbox_addresses/{id}/ | 
[**email_sandbox_addresses_list**](EmailApi.md#email_sandbox_addresses_list) | **GET** /api/email/sandbox_addresses/ | 
[**email_sandbox_addresses_retrieve**](EmailApi.md#email_sandbox_addresses_retrieve) | **GET** /api/email/sandbox_addresses/{id}/ | 
[**email_send_create**](EmailApi.md#email_send_create) | **POST** /api/email/send/ | 
[**email_services_api_credentials_create**](EmailApi.md#email_services_api_credentials_create) | **POST** /api/email/services/{service_pk}/api_credentials/ | 
[**email_services_api_credentials_list**](EmailApi.md#email_services_api_credentials_list) | **GET** /api/email/services/{service_pk}/api_credentials/ | 
[**email_services_cancel_create**](EmailApi.md#email_services_cancel_create) | **POST** /api/email/services/{id}/cancel/ | 
[**email_services_change_tier_partial_update**](EmailApi.md#email_services_change_tier_partial_update) | **PATCH** /api/email/services/{id}/change_tier/ | 
[**email_services_create**](EmailApi.md#email_services_create) | **POST** /api/email/services/ | 
[**email_services_dedicated_ip_create**](EmailApi.md#email_services_dedicated_ip_create) | **POST** /api/email/services/{id}/dedicated_ip/ | 
[**email_services_dedicated_ip_destroy**](EmailApi.md#email_services_dedicated_ip_destroy) | **DELETE** /api/email/services/{id}/dedicated_ip/ | 
[**email_services_destroy**](EmailApi.md#email_services_destroy) | **DELETE** /api/email/services/{id}/ | 
[**email_services_domains_create**](EmailApi.md#email_services_domains_create) | **POST** /api/email/services/{service_pk}/domains/ | 
[**email_services_domains_list**](EmailApi.md#email_services_domains_list) | **GET** /api/email/services/{service_pk}/domains/ | 
[**email_services_list**](EmailApi.md#email_services_list) | **GET** /api/email/services/ | 
[**email_services_messages_retrieve**](EmailApi.md#email_services_messages_retrieve) | **GET** /api/email/services/{service_pk}/messages/ | 
[**email_services_partial_update**](EmailApi.md#email_services_partial_update) | **PATCH** /api/email/services/{id}/ | 
[**email_services_restore_create**](EmailApi.md#email_services_restore_create) | **POST** /api/email/services/{id}/restore/ | 
[**email_services_retrieve**](EmailApi.md#email_services_retrieve) | **GET** /api/email/services/{id}/ | 
[**email_services_sandbox_addresses_create**](EmailApi.md#email_services_sandbox_addresses_create) | **POST** /api/email/services/{service_pk}/sandbox_addresses/ | 
[**email_services_sandbox_addresses_list**](EmailApi.md#email_services_sandbox_addresses_list) | **GET** /api/email/services/{service_pk}/sandbox_addresses/ | 
[**email_services_smtp_credentials_create**](EmailApi.md#email_services_smtp_credentials_create) | **POST** /api/email/services/{service_pk}/smtp_credentials/ | 
[**email_services_smtp_credentials_list**](EmailApi.md#email_services_smtp_credentials_list) | **GET** /api/email/services/{service_pk}/smtp_credentials/ | 
[**email_services_stats_retrieve**](EmailApi.md#email_services_stats_retrieve) | **GET** /api/email/services/{service_pk}/stats/ | 
[**email_services_suppressions_create**](EmailApi.md#email_services_suppressions_create) | **POST** /api/email/services/{service_pk}/suppressions/ | 
[**email_services_suppressions_list**](EmailApi.md#email_services_suppressions_list) | **GET** /api/email/services/{service_pk}/suppressions/ | 
[**email_smtp_credentials_create**](EmailApi.md#email_smtp_credentials_create) | **POST** /api/email/smtp_credentials/ | 
[**email_smtp_credentials_destroy**](EmailApi.md#email_smtp_credentials_destroy) | **DELETE** /api/email/smtp_credentials/{id}/ | 
[**email_smtp_credentials_list**](EmailApi.md#email_smtp_credentials_list) | **GET** /api/email/smtp_credentials/ | 
[**email_smtp_credentials_retrieve**](EmailApi.md#email_smtp_credentials_retrieve) | **GET** /api/email/smtp_credentials/{id}/ | 
[**email_suppressions_create**](EmailApi.md#email_suppressions_create) | **POST** /api/email/suppressions/ | 
[**email_suppressions_destroy**](EmailApi.md#email_suppressions_destroy) | **DELETE** /api/email/suppressions/{id}/ | 
[**email_suppressions_list**](EmailApi.md#email_suppressions_list) | **GET** /api/email/suppressions/ | 
[**email_suppressions_retrieve**](EmailApi.md#email_suppressions_retrieve) | **GET** /api/email/suppressions/{id}/ | 


# **email_api_credentials_create**
> ApiCredential email_api_credentials_create(api_credential=api_credential)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.api_credential import ApiCredential
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    api_credential = pidginhost_sdk.ApiCredential() # ApiCredential |  (optional)

    try:
        api_response = api_instance.email_api_credentials_create(api_credential=api_credential)
        print("The response of EmailApi->email_api_credentials_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_api_credentials_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_credential** | [**ApiCredential**](ApiCredential.md)|  | [optional] 

### Return type

[**ApiCredential**](ApiCredential.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_api_credentials_destroy**
> email_api_credentials_destroy(id)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    id = 56 # int | A unique integer value identifying this api credential.

    try:
        api_instance.email_api_credentials_destroy(id)
    except Exception as e:
        print("Exception when calling EmailApi->email_api_credentials_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this api credential. | 

### Return type

void (empty response body)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_api_credentials_list**
> PaginatedApiCredentialList email_api_credentials_list(page=page)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.paginated_api_credential_list import PaginatedApiCredentialList
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.email_api_credentials_list(page=page)
        print("The response of EmailApi->email_api_credentials_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_api_credentials_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedApiCredentialList**](PaginatedApiCredentialList.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_api_credentials_retrieve**
> ApiCredential email_api_credentials_retrieve(id)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.api_credential import ApiCredential
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    id = 56 # int | A unique integer value identifying this api credential.

    try:
        api_response = api_instance.email_api_credentials_retrieve(id)
        print("The response of EmailApi->email_api_credentials_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_api_credentials_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this api credential. | 

### Return type

[**ApiCredential**](ApiCredential.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_domains_create**
> SendingDomain email_domains_create(domain_add)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.domain_add import DomainAdd
from pidginhost_sdk.models.sending_domain import SendingDomain
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    domain_add = pidginhost_sdk.DomainAdd() # DomainAdd | 

    try:
        api_response = api_instance.email_domains_create(domain_add)
        print("The response of EmailApi->email_domains_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_domains_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_add** | [**DomainAdd**](DomainAdd.md)|  | 

### Return type

[**SendingDomain**](SendingDomain.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_domains_inbound_routes_create**
> InboundRoute email_domains_inbound_routes_create(domain_pk, inbound_route)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.inbound_route import InboundRoute
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    domain_pk = 56 # int | 
    inbound_route = pidginhost_sdk.InboundRoute() # InboundRoute | 

    try:
        api_response = api_instance.email_domains_inbound_routes_create(domain_pk, inbound_route)
        print("The response of EmailApi->email_domains_inbound_routes_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_domains_inbound_routes_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_pk** | **int**|  | 
 **inbound_route** | [**InboundRoute**](InboundRoute.md)|  | 

### Return type

[**InboundRoute**](InboundRoute.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_domains_inbound_routes_list**
> PaginatedInboundRouteList email_domains_inbound_routes_list(domain_pk, page=page)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.paginated_inbound_route_list import PaginatedInboundRouteList
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    domain_pk = 56 # int | 
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.email_domains_inbound_routes_list(domain_pk, page=page)
        print("The response of EmailApi->email_domains_inbound_routes_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_domains_inbound_routes_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_pk** | **int**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedInboundRouteList**](PaginatedInboundRouteList.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_domains_list**
> PaginatedSendingDomainList email_domains_list(page=page)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.paginated_sending_domain_list import PaginatedSendingDomainList
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.email_domains_list(page=page)
        print("The response of EmailApi->email_domains_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_domains_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedSendingDomainList**](PaginatedSendingDomainList.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_domains_retrieve**
> SendingDomain email_domains_retrieve(id)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.sending_domain import SendingDomain
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    id = 56 # int | A unique integer value identifying this sending domain.

    try:
        api_response = api_instance.email_domains_retrieve(id)
        print("The response of EmailApi->email_domains_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_domains_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this sending domain. | 

### Return type

[**SendingDomain**](SendingDomain.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_domains_rotate_dkim_create**
> SendingDomain email_domains_rotate_dkim_create(id, sending_domain=sending_domain)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.sending_domain import SendingDomain
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    id = 56 # int | A unique integer value identifying this sending domain.
    sending_domain = pidginhost_sdk.SendingDomain() # SendingDomain |  (optional)

    try:
        api_response = api_instance.email_domains_rotate_dkim_create(id, sending_domain=sending_domain)
        print("The response of EmailApi->email_domains_rotate_dkim_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_domains_rotate_dkim_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this sending domain. | 
 **sending_domain** | [**SendingDomain**](SendingDomain.md)|  | [optional] 

### Return type

[**SendingDomain**](SendingDomain.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_domains_toggle_inbound_create**
> SendingDomain email_domains_toggle_inbound_create(id, sending_domain=sending_domain)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.sending_domain import SendingDomain
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    id = 56 # int | A unique integer value identifying this sending domain.
    sending_domain = pidginhost_sdk.SendingDomain() # SendingDomain |  (optional)

    try:
        api_response = api_instance.email_domains_toggle_inbound_create(id, sending_domain=sending_domain)
        print("The response of EmailApi->email_domains_toggle_inbound_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_domains_toggle_inbound_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this sending domain. | 
 **sending_domain** | [**SendingDomain**](SendingDomain.md)|  | [optional] 

### Return type

[**SendingDomain**](SendingDomain.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_domains_verify_create**
> SendingDomain email_domains_verify_create(id, sending_domain=sending_domain)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.sending_domain import SendingDomain
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    id = 56 # int | A unique integer value identifying this sending domain.
    sending_domain = pidginhost_sdk.SendingDomain() # SendingDomain |  (optional)

    try:
        api_response = api_instance.email_domains_verify_create(id, sending_domain=sending_domain)
        print("The response of EmailApi->email_domains_verify_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_domains_verify_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this sending domain. | 
 **sending_domain** | [**SendingDomain**](SendingDomain.md)|  | [optional] 

### Return type

[**SendingDomain**](SendingDomain.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_inbound_routes_create**
> InboundRoute email_inbound_routes_create(inbound_route)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.inbound_route import InboundRoute
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    inbound_route = pidginhost_sdk.InboundRoute() # InboundRoute | 

    try:
        api_response = api_instance.email_inbound_routes_create(inbound_route)
        print("The response of EmailApi->email_inbound_routes_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_inbound_routes_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_route** | [**InboundRoute**](InboundRoute.md)|  | 

### Return type

[**InboundRoute**](InboundRoute.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_inbound_routes_destroy**
> email_inbound_routes_destroy(id)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    id = 56 # int | A unique integer value identifying this inbound route.

    try:
        api_instance.email_inbound_routes_destroy(id)
    except Exception as e:
        print("Exception when calling EmailApi->email_inbound_routes_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this inbound route. | 

### Return type

void (empty response body)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_inbound_routes_list**
> PaginatedInboundRouteList email_inbound_routes_list(page=page)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.paginated_inbound_route_list import PaginatedInboundRouteList
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.email_inbound_routes_list(page=page)
        print("The response of EmailApi->email_inbound_routes_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_inbound_routes_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedInboundRouteList**](PaginatedInboundRouteList.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_inbound_routes_partial_update**
> InboundRoute email_inbound_routes_partial_update(id, patched_inbound_route=patched_inbound_route)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.inbound_route import InboundRoute
from pidginhost_sdk.models.patched_inbound_route import PatchedInboundRoute
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    id = 56 # int | A unique integer value identifying this inbound route.
    patched_inbound_route = pidginhost_sdk.PatchedInboundRoute() # PatchedInboundRoute |  (optional)

    try:
        api_response = api_instance.email_inbound_routes_partial_update(id, patched_inbound_route=patched_inbound_route)
        print("The response of EmailApi->email_inbound_routes_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_inbound_routes_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this inbound route. | 
 **patched_inbound_route** | [**PatchedInboundRoute**](PatchedInboundRoute.md)|  | [optional] 

### Return type

[**InboundRoute**](InboundRoute.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_inbound_routes_retrieve**
> InboundRoute email_inbound_routes_retrieve(id)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.inbound_route import InboundRoute
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    id = 56 # int | A unique integer value identifying this inbound route.

    try:
        api_response = api_instance.email_inbound_routes_retrieve(id)
        print("The response of EmailApi->email_inbound_routes_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_inbound_routes_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this inbound route. | 

### Return type

[**InboundRoute**](InboundRoute.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_messages_retrieve**
> email_messages_retrieve(message_id)

Look up a single message via Postal v3 legacy API using the server's own token.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    message_id = 'message_id_example' # str | 

    try:
        api_instance.email_messages_retrieve(message_id)
    except Exception as e:
        print("Exception when calling EmailApi->email_messages_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_sandbox_addresses_create**
> SandboxAddress email_sandbox_addresses_create(sandbox_address)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.sandbox_address import SandboxAddress
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    sandbox_address = pidginhost_sdk.SandboxAddress() # SandboxAddress | 

    try:
        api_response = api_instance.email_sandbox_addresses_create(sandbox_address)
        print("The response of EmailApi->email_sandbox_addresses_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_sandbox_addresses_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandbox_address** | [**SandboxAddress**](SandboxAddress.md)|  | 

### Return type

[**SandboxAddress**](SandboxAddress.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_sandbox_addresses_destroy**
> email_sandbox_addresses_destroy(id)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    id = 56 # int | A unique integer value identifying this sandbox verified address.

    try:
        api_instance.email_sandbox_addresses_destroy(id)
    except Exception as e:
        print("Exception when calling EmailApi->email_sandbox_addresses_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this sandbox verified address. | 

### Return type

void (empty response body)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_sandbox_addresses_list**
> PaginatedSandboxAddressList email_sandbox_addresses_list(page=page)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.paginated_sandbox_address_list import PaginatedSandboxAddressList
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.email_sandbox_addresses_list(page=page)
        print("The response of EmailApi->email_sandbox_addresses_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_sandbox_addresses_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedSandboxAddressList**](PaginatedSandboxAddressList.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_sandbox_addresses_retrieve**
> SandboxAddress email_sandbox_addresses_retrieve(id)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.sandbox_address import SandboxAddress
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    id = 56 # int | A unique integer value identifying this sandbox verified address.

    try:
        api_response = api_instance.email_sandbox_addresses_retrieve(id)
        print("The response of EmailApi->email_sandbox_addresses_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_sandbox_addresses_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this sandbox verified address. | 

### Return type

[**SandboxAddress**](SandboxAddress.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_send_create**
> email_send_create()

### Example


```python
import pidginhost_sdk
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)


# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)

    try:
        api_instance.email_send_create()
    except Exception as e:
        print("Exception when calling EmailApi->email_send_create: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_services_api_credentials_create**
> ApiCredential email_services_api_credentials_create(service_pk, api_credential=api_credential)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.api_credential import ApiCredential
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    service_pk = 56 # int | 
    api_credential = pidginhost_sdk.ApiCredential() # ApiCredential |  (optional)

    try:
        api_response = api_instance.email_services_api_credentials_create(service_pk, api_credential=api_credential)
        print("The response of EmailApi->email_services_api_credentials_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_services_api_credentials_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_pk** | **int**|  | 
 **api_credential** | [**ApiCredential**](ApiCredential.md)|  | [optional] 

### Return type

[**ApiCredential**](ApiCredential.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_services_api_credentials_list**
> PaginatedApiCredentialList email_services_api_credentials_list(service_pk, page=page)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.paginated_api_credential_list import PaginatedApiCredentialList
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    service_pk = 56 # int | 
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.email_services_api_credentials_list(service_pk, page=page)
        print("The response of EmailApi->email_services_api_credentials_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_services_api_credentials_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_pk** | **int**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedApiCredentialList**](PaginatedApiCredentialList.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_services_cancel_create**
> EmailService email_services_cancel_create(id)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.email_service import EmailService
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    id = 56 # int | A unique integer value identifying this email service.

    try:
        api_response = api_instance.email_services_cancel_create(id)
        print("The response of EmailApi->email_services_cancel_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_services_cancel_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this email service. | 

### Return type

[**EmailService**](EmailService.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_services_change_tier_partial_update**
> EmailService email_services_change_tier_partial_update(id, patched_subscribe=patched_subscribe)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.email_service import EmailService
from pidginhost_sdk.models.patched_subscribe import PatchedSubscribe
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    id = 56 # int | A unique integer value identifying this email service.
    patched_subscribe = pidginhost_sdk.PatchedSubscribe() # PatchedSubscribe |  (optional)

    try:
        api_response = api_instance.email_services_change_tier_partial_update(id, patched_subscribe=patched_subscribe)
        print("The response of EmailApi->email_services_change_tier_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_services_change_tier_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this email service. | 
 **patched_subscribe** | [**PatchedSubscribe**](PatchedSubscribe.md)|  | [optional] 

### Return type

[**EmailService**](EmailService.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_services_create**
> EmailService email_services_create(subscribe)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.email_service import EmailService
from pidginhost_sdk.models.subscribe import Subscribe
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    subscribe = pidginhost_sdk.Subscribe() # Subscribe | 

    try:
        api_response = api_instance.email_services_create(subscribe)
        print("The response of EmailApi->email_services_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_services_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscribe** | [**Subscribe**](Subscribe.md)|  | 

### Return type

[**EmailService**](EmailService.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_services_dedicated_ip_create**
> EmailService email_services_dedicated_ip_create(id)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.email_service import EmailService
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    id = 56 # int | A unique integer value identifying this email service.

    try:
        api_response = api_instance.email_services_dedicated_ip_create(id)
        print("The response of EmailApi->email_services_dedicated_ip_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_services_dedicated_ip_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this email service. | 

### Return type

[**EmailService**](EmailService.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_services_dedicated_ip_destroy**
> email_services_dedicated_ip_destroy(id)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    id = 56 # int | A unique integer value identifying this email service.

    try:
        api_instance.email_services_dedicated_ip_destroy(id)
    except Exception as e:
        print("Exception when calling EmailApi->email_services_dedicated_ip_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this email service. | 

### Return type

void (empty response body)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_services_destroy**
> email_services_destroy(id)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    id = 56 # int | A unique integer value identifying this email service.

    try:
        api_instance.email_services_destroy(id)
    except Exception as e:
        print("Exception when calling EmailApi->email_services_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this email service. | 

### Return type

void (empty response body)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_services_domains_create**
> SendingDomain email_services_domains_create(service_pk, domain_add)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.domain_add import DomainAdd
from pidginhost_sdk.models.sending_domain import SendingDomain
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    service_pk = 56 # int | 
    domain_add = pidginhost_sdk.DomainAdd() # DomainAdd | 

    try:
        api_response = api_instance.email_services_domains_create(service_pk, domain_add)
        print("The response of EmailApi->email_services_domains_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_services_domains_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_pk** | **int**|  | 
 **domain_add** | [**DomainAdd**](DomainAdd.md)|  | 

### Return type

[**SendingDomain**](SendingDomain.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_services_domains_list**
> PaginatedSendingDomainList email_services_domains_list(service_pk, page=page)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.paginated_sending_domain_list import PaginatedSendingDomainList
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    service_pk = 56 # int | 
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.email_services_domains_list(service_pk, page=page)
        print("The response of EmailApi->email_services_domains_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_services_domains_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_pk** | **int**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedSendingDomainList**](PaginatedSendingDomainList.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_services_list**
> PaginatedEmailServiceList email_services_list(page=page)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.paginated_email_service_list import PaginatedEmailServiceList
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.email_services_list(page=page)
        print("The response of EmailApi->email_services_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_services_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedEmailServiceList**](PaginatedEmailServiceList.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_services_messages_retrieve**
> email_services_messages_retrieve(service_pk)

List recently observed messages for a customer's email service.

Postal v3 legacy API exposes per-message lookups only; phclient builds the
list locally from webhook events. Each message_id is deduped, keeping the
most recent event_type as the message status.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    service_pk = 56 # int | 

    try:
        api_instance.email_services_messages_retrieve(service_pk)
    except Exception as e:
        print("Exception when calling EmailApi->email_services_messages_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_pk** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_services_partial_update**
> EmailService email_services_partial_update(id, patched_email_service=patched_email_service)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.email_service import EmailService
from pidginhost_sdk.models.patched_email_service import PatchedEmailService
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    id = 56 # int | A unique integer value identifying this email service.
    patched_email_service = pidginhost_sdk.PatchedEmailService() # PatchedEmailService |  (optional)

    try:
        api_response = api_instance.email_services_partial_update(id, patched_email_service=patched_email_service)
        print("The response of EmailApi->email_services_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_services_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this email service. | 
 **patched_email_service** | [**PatchedEmailService**](PatchedEmailService.md)|  | [optional] 

### Return type

[**EmailService**](EmailService.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_services_restore_create**
> EmailService email_services_restore_create(id)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.email_service import EmailService
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    id = 56 # int | A unique integer value identifying this email service.

    try:
        api_response = api_instance.email_services_restore_create(id)
        print("The response of EmailApi->email_services_restore_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_services_restore_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this email service. | 

### Return type

[**EmailService**](EmailService.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_services_retrieve**
> EmailService email_services_retrieve(id)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.email_service import EmailService
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    id = 56 # int | A unique integer value identifying this email service.

    try:
        api_response = api_instance.email_services_retrieve(id)
        print("The response of EmailApi->email_services_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_services_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this email service. | 

### Return type

[**EmailService**](EmailService.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_services_sandbox_addresses_create**
> SandboxAddress email_services_sandbox_addresses_create(service_pk, sandbox_address)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.sandbox_address import SandboxAddress
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    service_pk = 56 # int | 
    sandbox_address = pidginhost_sdk.SandboxAddress() # SandboxAddress | 

    try:
        api_response = api_instance.email_services_sandbox_addresses_create(service_pk, sandbox_address)
        print("The response of EmailApi->email_services_sandbox_addresses_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_services_sandbox_addresses_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_pk** | **int**|  | 
 **sandbox_address** | [**SandboxAddress**](SandboxAddress.md)|  | 

### Return type

[**SandboxAddress**](SandboxAddress.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_services_sandbox_addresses_list**
> PaginatedSandboxAddressList email_services_sandbox_addresses_list(service_pk, page=page)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.paginated_sandbox_address_list import PaginatedSandboxAddressList
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    service_pk = 56 # int | 
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.email_services_sandbox_addresses_list(service_pk, page=page)
        print("The response of EmailApi->email_services_sandbox_addresses_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_services_sandbox_addresses_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_pk** | **int**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedSandboxAddressList**](PaginatedSandboxAddressList.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_services_smtp_credentials_create**
> SmtpCredential email_services_smtp_credentials_create(service_pk, smtp_credential=smtp_credential)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.smtp_credential import SmtpCredential
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    service_pk = 56 # int | 
    smtp_credential = pidginhost_sdk.SmtpCredential() # SmtpCredential |  (optional)

    try:
        api_response = api_instance.email_services_smtp_credentials_create(service_pk, smtp_credential=smtp_credential)
        print("The response of EmailApi->email_services_smtp_credentials_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_services_smtp_credentials_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_pk** | **int**|  | 
 **smtp_credential** | [**SmtpCredential**](SmtpCredential.md)|  | [optional] 

### Return type

[**SmtpCredential**](SmtpCredential.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_services_smtp_credentials_list**
> PaginatedSmtpCredentialList email_services_smtp_credentials_list(service_pk, page=page)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.paginated_smtp_credential_list import PaginatedSmtpCredentialList
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    service_pk = 56 # int | 
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.email_services_smtp_credentials_list(service_pk, page=page)
        print("The response of EmailApi->email_services_smtp_credentials_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_services_smtp_credentials_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_pk** | **int**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedSmtpCredentialList**](PaginatedSmtpCredentialList.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_services_stats_retrieve**
> email_services_stats_retrieve(service_pk)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    service_pk = 56 # int | 

    try:
        api_instance.email_services_stats_retrieve(service_pk)
    except Exception as e:
        print("Exception when calling EmailApi->email_services_stats_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_pk** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_services_suppressions_create**
> SuppressionEntry email_services_suppressions_create(service_pk, suppression_entry=suppression_entry)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.suppression_entry import SuppressionEntry
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    service_pk = 56 # int | 
    suppression_entry = pidginhost_sdk.SuppressionEntry() # SuppressionEntry |  (optional)

    try:
        api_response = api_instance.email_services_suppressions_create(service_pk, suppression_entry=suppression_entry)
        print("The response of EmailApi->email_services_suppressions_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_services_suppressions_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_pk** | **int**|  | 
 **suppression_entry** | [**SuppressionEntry**](SuppressionEntry.md)|  | [optional] 

### Return type

[**SuppressionEntry**](SuppressionEntry.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_services_suppressions_list**
> PaginatedSuppressionEntryList email_services_suppressions_list(service_pk, page=page)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.paginated_suppression_entry_list import PaginatedSuppressionEntryList
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    service_pk = 56 # int | 
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.email_services_suppressions_list(service_pk, page=page)
        print("The response of EmailApi->email_services_suppressions_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_services_suppressions_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_pk** | **int**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedSuppressionEntryList**](PaginatedSuppressionEntryList.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_smtp_credentials_create**
> SmtpCredential email_smtp_credentials_create(smtp_credential=smtp_credential)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.smtp_credential import SmtpCredential
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    smtp_credential = pidginhost_sdk.SmtpCredential() # SmtpCredential |  (optional)

    try:
        api_response = api_instance.email_smtp_credentials_create(smtp_credential=smtp_credential)
        print("The response of EmailApi->email_smtp_credentials_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_smtp_credentials_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smtp_credential** | [**SmtpCredential**](SmtpCredential.md)|  | [optional] 

### Return type

[**SmtpCredential**](SmtpCredential.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_smtp_credentials_destroy**
> email_smtp_credentials_destroy(id)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    id = 56 # int | A unique integer value identifying this smtp credential.

    try:
        api_instance.email_smtp_credentials_destroy(id)
    except Exception as e:
        print("Exception when calling EmailApi->email_smtp_credentials_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this smtp credential. | 

### Return type

void (empty response body)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_smtp_credentials_list**
> PaginatedSmtpCredentialList email_smtp_credentials_list(page=page)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.paginated_smtp_credential_list import PaginatedSmtpCredentialList
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.email_smtp_credentials_list(page=page)
        print("The response of EmailApi->email_smtp_credentials_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_smtp_credentials_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedSmtpCredentialList**](PaginatedSmtpCredentialList.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_smtp_credentials_retrieve**
> SmtpCredential email_smtp_credentials_retrieve(id)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.smtp_credential import SmtpCredential
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    id = 56 # int | A unique integer value identifying this smtp credential.

    try:
        api_response = api_instance.email_smtp_credentials_retrieve(id)
        print("The response of EmailApi->email_smtp_credentials_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_smtp_credentials_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this smtp credential. | 

### Return type

[**SmtpCredential**](SmtpCredential.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_suppressions_create**
> SuppressionEntry email_suppressions_create(suppression_entry=suppression_entry)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.suppression_entry import SuppressionEntry
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    suppression_entry = pidginhost_sdk.SuppressionEntry() # SuppressionEntry |  (optional)

    try:
        api_response = api_instance.email_suppressions_create(suppression_entry=suppression_entry)
        print("The response of EmailApi->email_suppressions_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_suppressions_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **suppression_entry** | [**SuppressionEntry**](SuppressionEntry.md)|  | [optional] 

### Return type

[**SuppressionEntry**](SuppressionEntry.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_suppressions_destroy**
> email_suppressions_destroy(id)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    id = 56 # int | A unique integer value identifying this suppression entry.

    try:
        api_instance.email_suppressions_destroy(id)
    except Exception as e:
        print("Exception when calling EmailApi->email_suppressions_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this suppression entry. | 

### Return type

void (empty response body)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_suppressions_list**
> PaginatedSuppressionEntryList email_suppressions_list(page=page)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.paginated_suppression_entry_list import PaginatedSuppressionEntryList
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.email_suppressions_list(page=page)
        print("The response of EmailApi->email_suppressions_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_suppressions_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedSuppressionEntryList**](PaginatedSuppressionEntryList.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_suppressions_retrieve**
> SuppressionEntry email_suppressions_retrieve(id)

Intersect the beta gate and IAM with the configured API permissions.

Keeping the gate additive preserves authentication, custom-token scope,
and OAuth scope checks when the customer-facing feature flag is open.
Per-action permission overrides (the staff-only restore action) remain in
the same intersection.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.suppression_entry import SuppressionEntry
from pidginhost_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://www.pidginhost.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pidginhost_sdk.Configuration(
    host = "https://www.pidginhost.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    id = 56 # int | A unique integer value identifying this suppression entry.

    try:
        api_response = api_instance.email_suppressions_retrieve(id)
        print("The response of EmailApi->email_suppressions_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_suppressions_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this suppression entry. | 

### Return type

[**SuppressionEntry**](SuppressionEntry.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

