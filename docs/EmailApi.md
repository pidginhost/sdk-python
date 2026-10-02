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
> ApiCredentialCreated email_api_credentials_create(credential_create_request=credential_create_request)

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
from pidginhost_sdk.models.api_credential_created import ApiCredentialCreated
from pidginhost_sdk.models.credential_create_request import CredentialCreateRequest
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
    credential_create_request = pidginhost_sdk.CredentialCreateRequest() # CredentialCreateRequest |  (optional)

    try:
        api_response = api_instance.email_api_credentials_create(credential_create_request=credential_create_request)
        print("The response of EmailApi->email_api_credentials_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_api_credentials_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_create_request** | [**CredentialCreateRequest**](CredentialCreateRequest.md)|  | [optional] 

### Return type

[**ApiCredentialCreated**](ApiCredentialCreated.md)

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
> SendingDomain email_domains_create(domain_add_request)

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
from pidginhost_sdk.models.domain_add_request import DomainAddRequest
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
    domain_add_request = pidginhost_sdk.DomainAddRequest() # DomainAddRequest | 

    try:
        api_response = api_instance.email_domains_create(domain_add_request)
        print("The response of EmailApi->email_domains_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_domains_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_add_request** | [**DomainAddRequest**](DomainAddRequest.md)|  | 

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
> InboundRouteWriteResponse email_domains_inbound_routes_create(domain_pk, inbound_route_create_request)

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
from pidginhost_sdk.models.inbound_route_create_request import InboundRouteCreateRequest
from pidginhost_sdk.models.inbound_route_write_response import InboundRouteWriteResponse
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
    inbound_route_create_request = pidginhost_sdk.InboundRouteCreateRequest() # InboundRouteCreateRequest | 

    try:
        api_response = api_instance.email_domains_inbound_routes_create(domain_pk, inbound_route_create_request)
        print("The response of EmailApi->email_domains_inbound_routes_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_domains_inbound_routes_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_pk** | **int**|  | 
 **inbound_route_create_request** | [**InboundRouteCreateRequest**](InboundRouteCreateRequest.md)|  | 

### Return type

[**InboundRouteWriteResponse**](InboundRouteWriteResponse.md)

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
> SendingDomain email_domains_rotate_dkim_create(id)

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
        api_response = api_instance.email_domains_rotate_dkim_create(id)
        print("The response of EmailApi->email_domains_rotate_dkim_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_domains_rotate_dkim_create: %s\n" % e)
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

# **email_domains_toggle_inbound_create**
> SendingDomain email_domains_toggle_inbound_create(id, toggle_inbound_request=toggle_inbound_request)

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
from pidginhost_sdk.models.toggle_inbound_request import ToggleInboundRequest
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
    toggle_inbound_request = pidginhost_sdk.ToggleInboundRequest() # ToggleInboundRequest |  (optional)

    try:
        api_response = api_instance.email_domains_toggle_inbound_create(id, toggle_inbound_request=toggle_inbound_request)
        print("The response of EmailApi->email_domains_toggle_inbound_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_domains_toggle_inbound_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this sending domain. | 
 **toggle_inbound_request** | [**ToggleInboundRequest**](ToggleInboundRequest.md)|  | [optional] 

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
> SendingDomain email_domains_verify_create(id)

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
        api_response = api_instance.email_domains_verify_create(id)
        print("The response of EmailApi->email_domains_verify_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_domains_verify_create: %s\n" % e)
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

# **email_inbound_routes_create**
> InboundRouteWriteResponse email_inbound_routes_create(inbound_route_create_request)

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
from pidginhost_sdk.models.inbound_route_create_request import InboundRouteCreateRequest
from pidginhost_sdk.models.inbound_route_write_response import InboundRouteWriteResponse
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
    inbound_route_create_request = pidginhost_sdk.InboundRouteCreateRequest() # InboundRouteCreateRequest | 

    try:
        api_response = api_instance.email_inbound_routes_create(inbound_route_create_request)
        print("The response of EmailApi->email_inbound_routes_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_inbound_routes_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inbound_route_create_request** | [**InboundRouteCreateRequest**](InboundRouteCreateRequest.md)|  | 

### Return type

[**InboundRouteWriteResponse**](InboundRouteWriteResponse.md)

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
> InboundRouteWriteResponse email_inbound_routes_partial_update(id, patched_inbound_route_create_request=patched_inbound_route_create_request)

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
from pidginhost_sdk.models.inbound_route_write_response import InboundRouteWriteResponse
from pidginhost_sdk.models.patched_inbound_route_create_request import PatchedInboundRouteCreateRequest
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
    patched_inbound_route_create_request = pidginhost_sdk.PatchedInboundRouteCreateRequest() # PatchedInboundRouteCreateRequest |  (optional)

    try:
        api_response = api_instance.email_inbound_routes_partial_update(id, patched_inbound_route_create_request=patched_inbound_route_create_request)
        print("The response of EmailApi->email_inbound_routes_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_inbound_routes_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this inbound route. | 
 **patched_inbound_route_create_request** | [**PatchedInboundRouteCreateRequest**](PatchedInboundRouteCreateRequest.md)|  | [optional] 

### Return type

[**InboundRouteWriteResponse**](InboundRouteWriteResponse.md)

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
> Dict[str, object] email_messages_retrieve(message_id)

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
        api_response = api_instance.email_messages_retrieve(message_id)
        print("The response of EmailApi->email_messages_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_messages_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **str**|  | 

### Return type

**Dict[str, object]**

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

# **email_sandbox_addresses_create**
> SandboxAddress email_sandbox_addresses_create(sandbox_address_request)

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
from pidginhost_sdk.models.sandbox_address_request import SandboxAddressRequest
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
    sandbox_address_request = pidginhost_sdk.SandboxAddressRequest() # SandboxAddressRequest | 

    try:
        api_response = api_instance.email_sandbox_addresses_create(sandbox_address_request)
        print("The response of EmailApi->email_sandbox_addresses_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_sandbox_addresses_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandbox_address_request** | [**SandboxAddressRequest**](SandboxAddressRequest.md)|  | 

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
> EmailSendResponse email_send_create(send_request)

### Example

* Bearer (phme_<key>) Authentication (emailApiKey):

```python
import pidginhost_sdk
from pidginhost_sdk.models.email_send_response import EmailSendResponse
from pidginhost_sdk.models.send_request import SendRequest
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

# Configure Bearer authorization (phme_<key>): emailApiKey
configuration = pidginhost_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.EmailApi(api_client)
    send_request = pidginhost_sdk.SendRequest() # SendRequest | 

    try:
        api_response = api_instance.email_send_create(send_request)
        print("The response of EmailApi->email_send_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_send_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_request** | [**SendRequest**](SendRequest.md)|  | 

### Return type

[**EmailSendResponse**](EmailSendResponse.md)

### Authorization

[emailApiKey](../README.md#emailApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_services_api_credentials_create**
> ApiCredentialCreated email_services_api_credentials_create(service_pk, credential_create_request=credential_create_request)

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
from pidginhost_sdk.models.api_credential_created import ApiCredentialCreated
from pidginhost_sdk.models.credential_create_request import CredentialCreateRequest
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
    credential_create_request = pidginhost_sdk.CredentialCreateRequest() # CredentialCreateRequest |  (optional)

    try:
        api_response = api_instance.email_services_api_credentials_create(service_pk, credential_create_request=credential_create_request)
        print("The response of EmailApi->email_services_api_credentials_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_services_api_credentials_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_pk** | **int**|  | 
 **credential_create_request** | [**CredentialCreateRequest**](CredentialCreateRequest.md)|  | [optional] 

### Return type

[**ApiCredentialCreated**](ApiCredentialCreated.md)

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
> EmailService email_services_change_tier_partial_update(id, subscribe_request)

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
from pidginhost_sdk.models.subscribe_request import SubscribeRequest
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
    subscribe_request = pidginhost_sdk.SubscribeRequest() # SubscribeRequest | 

    try:
        api_response = api_instance.email_services_change_tier_partial_update(id, subscribe_request)
        print("The response of EmailApi->email_services_change_tier_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_services_change_tier_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this email service. | 
 **subscribe_request** | [**SubscribeRequest**](SubscribeRequest.md)|  | 

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
> EmailService email_services_create(subscribe_request)

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
from pidginhost_sdk.models.subscribe_request import SubscribeRequest
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
    subscribe_request = pidginhost_sdk.SubscribeRequest() # SubscribeRequest | 

    try:
        api_response = api_instance.email_services_create(subscribe_request)
        print("The response of EmailApi->email_services_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_services_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscribe_request** | [**SubscribeRequest**](SubscribeRequest.md)|  | 

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
> EmailService email_services_dedicated_ip_destroy(id)

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
        api_response = api_instance.email_services_dedicated_ip_destroy(id)
        print("The response of EmailApi->email_services_dedicated_ip_destroy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_services_dedicated_ip_destroy: %s\n" % e)
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

# **email_services_domains_create**
> SendingDomain email_services_domains_create(service_pk, domain_add_request)

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
from pidginhost_sdk.models.domain_add_request import DomainAddRequest
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
    domain_add_request = pidginhost_sdk.DomainAddRequest() # DomainAddRequest | 

    try:
        api_response = api_instance.email_services_domains_create(service_pk, domain_add_request)
        print("The response of EmailApi->email_services_domains_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_services_domains_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_pk** | **int**|  | 
 **domain_add_request** | [**DomainAddRequest**](DomainAddRequest.md)|  | 

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
> EmailMessageList email_services_messages_retrieve(service_pk, page=page, per_page=per_page)

List recently observed messages for a customer's email service.

Postal v3 legacy API exposes per-message lookups only; phclient builds the
list locally from webhook events. Each message_id is deduped, keeping the
most recent event_type as the message status.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.email_message_list import EmailMessageList
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
    page = 56 # int | Page number, starting at 1. (optional)
    per_page = 56 # int | Page size, capped at 200; defaults to 50. (optional)

    try:
        api_response = api_instance.email_services_messages_retrieve(service_pk, page=page, per_page=per_page)
        print("The response of EmailApi->email_services_messages_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_services_messages_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_pk** | **int**|  | 
 **page** | **int**| Page number, starting at 1. | [optional] 
 **per_page** | **int**| Page size, capped at 200; defaults to 50. | [optional] 

### Return type

[**EmailMessageList**](EmailMessageList.md)

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

# **email_services_partial_update**
> EmailService email_services_partial_update(id)

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
        api_response = api_instance.email_services_partial_update(id)
        print("The response of EmailApi->email_services_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_services_partial_update: %s\n" % e)
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
> SandboxAddress email_services_sandbox_addresses_create(service_pk, sandbox_address_request)

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
from pidginhost_sdk.models.sandbox_address_request import SandboxAddressRequest
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
    sandbox_address_request = pidginhost_sdk.SandboxAddressRequest() # SandboxAddressRequest | 

    try:
        api_response = api_instance.email_services_sandbox_addresses_create(service_pk, sandbox_address_request)
        print("The response of EmailApi->email_services_sandbox_addresses_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_services_sandbox_addresses_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_pk** | **int**|  | 
 **sandbox_address_request** | [**SandboxAddressRequest**](SandboxAddressRequest.md)|  | 

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
> SmtpCredentialCreated email_services_smtp_credentials_create(service_pk, credential_create_request=credential_create_request)

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
from pidginhost_sdk.models.credential_create_request import CredentialCreateRequest
from pidginhost_sdk.models.smtp_credential_created import SmtpCredentialCreated
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
    credential_create_request = pidginhost_sdk.CredentialCreateRequest() # CredentialCreateRequest |  (optional)

    try:
        api_response = api_instance.email_services_smtp_credentials_create(service_pk, credential_create_request=credential_create_request)
        print("The response of EmailApi->email_services_smtp_credentials_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_services_smtp_credentials_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_pk** | **int**|  | 
 **credential_create_request** | [**CredentialCreateRequest**](CredentialCreateRequest.md)|  | [optional] 

### Return type

[**SmtpCredentialCreated**](SmtpCredentialCreated.md)

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
> EmailStats email_services_stats_retrieve(service_pk, end=end, start=start)

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
from pidginhost_sdk.models.email_stats import EmailStats
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
    end = '2013-10-20' # date |  (optional)
    start = '2013-10-20' # date |  (optional)

    try:
        api_response = api_instance.email_services_stats_retrieve(service_pk, end=end, start=start)
        print("The response of EmailApi->email_services_stats_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_services_stats_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_pk** | **int**|  | 
 **end** | **date**|  | [optional] 
 **start** | **date**|  | [optional] 

### Return type

[**EmailStats**](EmailStats.md)

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

# **email_services_suppressions_create**
> SuppressionEntry email_services_suppressions_create(service_pk, suppression_add_request)

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
from pidginhost_sdk.models.suppression_add_request import SuppressionAddRequest
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
    suppression_add_request = pidginhost_sdk.SuppressionAddRequest() # SuppressionAddRequest | 

    try:
        api_response = api_instance.email_services_suppressions_create(service_pk, suppression_add_request)
        print("The response of EmailApi->email_services_suppressions_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_services_suppressions_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_pk** | **int**|  | 
 **suppression_add_request** | [**SuppressionAddRequest**](SuppressionAddRequest.md)|  | 

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
> SmtpCredentialCreated email_smtp_credentials_create(credential_create_request=credential_create_request)

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
from pidginhost_sdk.models.credential_create_request import CredentialCreateRequest
from pidginhost_sdk.models.smtp_credential_created import SmtpCredentialCreated
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
    credential_create_request = pidginhost_sdk.CredentialCreateRequest() # CredentialCreateRequest |  (optional)

    try:
        api_response = api_instance.email_smtp_credentials_create(credential_create_request=credential_create_request)
        print("The response of EmailApi->email_smtp_credentials_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_smtp_credentials_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential_create_request** | [**CredentialCreateRequest**](CredentialCreateRequest.md)|  | [optional] 

### Return type

[**SmtpCredentialCreated**](SmtpCredentialCreated.md)

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
> SuppressionEntry email_suppressions_create(suppression_add_request)

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
from pidginhost_sdk.models.suppression_add_request import SuppressionAddRequest
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
    suppression_add_request = pidginhost_sdk.SuppressionAddRequest() # SuppressionAddRequest | 

    try:
        api_response = api_instance.email_suppressions_create(suppression_add_request)
        print("The response of EmailApi->email_suppressions_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->email_suppressions_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **suppression_add_request** | [**SuppressionAddRequest**](SuppressionAddRequest.md)|  | 

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

