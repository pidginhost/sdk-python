# pidginhost_sdk.DedicatedApi

All URIs are relative to *https://www.pidginhost.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dedicated_servers_list**](DedicatedApi.md#dedicated_servers_list) | **GET** /api/dedicated/servers/ | 
[**dedicated_servers_power_create**](DedicatedApi.md#dedicated_servers_power_create) | **POST** /api/dedicated/servers/{id}/power/ | 
[**dedicated_servers_rdns_create**](DedicatedApi.md#dedicated_servers_rdns_create) | **POST** /api/dedicated/servers/{id}/rdns/ | 
[**dedicated_servers_reinstall_create**](DedicatedApi.md#dedicated_servers_reinstall_create) | **POST** /api/dedicated/servers/{id}/reinstall/ | 
[**dedicated_servers_retrieve**](DedicatedApi.md#dedicated_servers_retrieve) | **GET** /api/dedicated/servers/{id}/ | 


# **dedicated_servers_list**
> PaginatedDedicatedServerList dedicated_servers_list(page=page)

List and manage dedicated server services.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.paginated_dedicated_server_list import PaginatedDedicatedServerList
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
    api_instance = pidginhost_sdk.DedicatedApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.dedicated_servers_list(page=page)
        print("The response of DedicatedApi->dedicated_servers_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DedicatedApi->dedicated_servers_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedDedicatedServerList**](PaginatedDedicatedServerList.md)

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

# **dedicated_servers_power_create**
> PowerActionResponse dedicated_servers_power_create(id, power_action_request)

Execute a power management action (start, stop, restart, shutdown).

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.power_action_request import PowerActionRequest
from pidginhost_sdk.models.power_action_response import PowerActionResponse
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
    api_instance = pidginhost_sdk.DedicatedApi(api_client)
    id = 'id_example' # str | 
    power_action_request = pidginhost_sdk.PowerActionRequest() # PowerActionRequest | 

    try:
        api_response = api_instance.dedicated_servers_power_create(id, power_action_request)
        print("The response of DedicatedApi->dedicated_servers_power_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DedicatedApi->dedicated_servers_power_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **power_action_request** | [**PowerActionRequest**](PowerActionRequest.md)|  | 

### Return type

[**PowerActionResponse**](PowerActionResponse.md)

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

# **dedicated_servers_rdns_create**
> RDNSUpdateResponse dedicated_servers_rdns_create(id, dedicated_rdns_request)

Update reverse DNS for a dedicated server IP.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.dedicated_rdns_request import DedicatedRDNSRequest
from pidginhost_sdk.models.rdns_update_response import RDNSUpdateResponse
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
    api_instance = pidginhost_sdk.DedicatedApi(api_client)
    id = 'id_example' # str | 
    dedicated_rdns_request = pidginhost_sdk.DedicatedRDNSRequest() # DedicatedRDNSRequest | 

    try:
        api_response = api_instance.dedicated_servers_rdns_create(id, dedicated_rdns_request)
        print("The response of DedicatedApi->dedicated_servers_rdns_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DedicatedApi->dedicated_servers_rdns_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **dedicated_rdns_request** | [**DedicatedRDNSRequest**](DedicatedRDNSRequest.md)|  | 

### Return type

[**RDNSUpdateResponse**](RDNSUpdateResponse.md)

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

# **dedicated_servers_reinstall_create**
> ReinstallResponse dedicated_servers_reinstall_create(id, reinstall_request)

Reinstall the dedicated server with a new operating system.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.reinstall_request import ReinstallRequest
from pidginhost_sdk.models.reinstall_response import ReinstallResponse
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
    api_instance = pidginhost_sdk.DedicatedApi(api_client)
    id = 'id_example' # str | 
    reinstall_request = pidginhost_sdk.ReinstallRequest() # ReinstallRequest | 

    try:
        api_response = api_instance.dedicated_servers_reinstall_create(id, reinstall_request)
        print("The response of DedicatedApi->dedicated_servers_reinstall_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DedicatedApi->dedicated_servers_reinstall_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **reinstall_request** | [**ReinstallRequest**](ReinstallRequest.md)|  | 

### Return type

[**ReinstallResponse**](ReinstallResponse.md)

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

# **dedicated_servers_retrieve**
> DedicatedServer dedicated_servers_retrieve(id)

List and manage dedicated server services.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.dedicated_server import DedicatedServer
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
    api_instance = pidginhost_sdk.DedicatedApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.dedicated_servers_retrieve(id)
        print("The response of DedicatedApi->dedicated_servers_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DedicatedApi->dedicated_servers_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**DedicatedServer**](DedicatedServer.md)

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

