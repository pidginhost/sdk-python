# pidginhost_sdk.OApi

All URIs are relative to *https://www.pidginhost.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**o_mobile_dashboard_retrieve**](OApi.md#o_mobile_dashboard_retrieve) | **GET** /o/mobile/dashboard/ | 
[**o_mobile_session_retrieve**](OApi.md#o_mobile_session_retrieve) | **GET** /o/mobile/session/ | 
[**o_register_create**](OApi.md#o_register_create) | **POST** /o/register | 


# **o_mobile_dashboard_retrieve**
> Dashboard o_mobile_dashboard_retrieve()

### Example


```python
import pidginhost_sdk
from pidginhost_sdk.models.dashboard import Dashboard
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
    api_instance = pidginhost_sdk.OApi(api_client)

    try:
        api_response = api_instance.o_mobile_dashboard_retrieve()
        print("The response of OApi->o_mobile_dashboard_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OApi->o_mobile_dashboard_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_mobile_session_retrieve**
> MobileOAuthSession o_mobile_session_retrieve()

### Example


```python
import pidginhost_sdk
from pidginhost_sdk.models.mobile_o_auth_session import MobileOAuthSession
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
    api_instance = pidginhost_sdk.OApi(api_client)

    try:
        api_response = api_instance.o_mobile_session_retrieve()
        print("The response of OApi->o_mobile_session_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OApi->o_mobile_session_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MobileOAuthSession**](MobileOAuthSession.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_register_create**
> o_register_create()

RFC 7591 dynamic client registration (open, throttled).

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
    api_instance = pidginhost_sdk.OApi(api_client)

    try:
        api_instance.o_register_create()
    except Exception as e:
        print("Exception when calling OApi->o_register_create: %s\n" % e)
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

