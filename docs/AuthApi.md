# pidginhost_sdk.AuthApi

All URIs are relative to *https://www.pidginhost.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_cli_session_create**](AuthApi.md#auth_cli_session_create) | **POST** /api/auth/cli-session/ | 
[**auth_cli_session_retrieve**](AuthApi.md#auth_cli_session_retrieve) | **GET** /api/auth/cli-session/{session_id}/ | 


# **auth_cli_session_create**
> CLISessionCreateResponse auth_cli_session_create()

Create a CLI authentication session for browser-based approval

### Example


```python
import pidginhost_sdk
from pidginhost_sdk.models.cli_session_create_response import CLISessionCreateResponse
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
    api_instance = pidginhost_sdk.AuthApi(api_client)

    try:
        api_response = api_instance.auth_cli_session_create()
        print("The response of AuthApi->auth_cli_session_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->auth_cli_session_create: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CLISessionCreateResponse**](CLISessionCreateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_cli_session_retrieve**
> CLISessionPollResponse auth_cli_session_retrieve(session_id)

Poll a CLI authentication session. Returns token when approved.

### Example


```python
import pidginhost_sdk
from pidginhost_sdk.models.cli_session_poll_response import CLISessionPollResponse
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
    api_instance = pidginhost_sdk.AuthApi(api_client)
    session_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | 

    try:
        api_response = api_instance.auth_cli_session_retrieve(session_id)
        print("The response of AuthApi->auth_cli_session_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->auth_cli_session_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **UUID**|  | 

### Return type

[**CLISessionPollResponse**](CLISessionPollResponse.md)

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

