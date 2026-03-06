# pidginhost_sdk.SupportApi

All URIs are relative to *https://www.pidginhost.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**support_departments_list**](SupportApi.md#support_departments_list) | **GET** /api/support/departments/ | 
[**support_departments_list2**](SupportApi.md#support_departments_list2) | **GET** /api/v1/support/departments/ | 
[**support_tickets_close_create**](SupportApi.md#support_tickets_close_create) | **POST** /api/support/tickets/{id}/close/ | 
[**support_tickets_close_create2**](SupportApi.md#support_tickets_close_create2) | **POST** /api/v1/support/tickets/{id}/close/ | 
[**support_tickets_create**](SupportApi.md#support_tickets_create) | **POST** /api/support/tickets/ | 
[**support_tickets_create2**](SupportApi.md#support_tickets_create2) | **POST** /api/v1/support/tickets/ | 
[**support_tickets_list**](SupportApi.md#support_tickets_list) | **GET** /api/support/tickets/ | 
[**support_tickets_list2**](SupportApi.md#support_tickets_list2) | **GET** /api/v1/support/tickets/ | 
[**support_tickets_messages_attachment_retrieve**](SupportApi.md#support_tickets_messages_attachment_retrieve) | **GET** /api/support/tickets/{id}/messages/{message_id}/attachment/ | 
[**support_tickets_messages_attachment_retrieve2**](SupportApi.md#support_tickets_messages_attachment_retrieve2) | **GET** /api/v1/support/tickets/{id}/messages/{message_id}/attachment/ | 
[**support_tickets_reopen_create**](SupportApi.md#support_tickets_reopen_create) | **POST** /api/support/tickets/{id}/reopen/ | 
[**support_tickets_reopen_create2**](SupportApi.md#support_tickets_reopen_create2) | **POST** /api/v1/support/tickets/{id}/reopen/ | 
[**support_tickets_reply_create**](SupportApi.md#support_tickets_reply_create) | **POST** /api/support/tickets/{id}/reply/ | 
[**support_tickets_reply_create2**](SupportApi.md#support_tickets_reply_create2) | **POST** /api/v1/support/tickets/{id}/reply/ | 
[**support_tickets_retrieve**](SupportApi.md#support_tickets_retrieve) | **GET** /api/support/tickets/{id}/ | 
[**support_tickets_retrieve2**](SupportApi.md#support_tickets_retrieve2) | **GET** /api/v1/support/tickets/{id}/ | 


# **support_departments_list**
> List[Department] support_departments_list()

List available support departments.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.department import Department
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

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.SupportApi(api_client)

    try:
        api_response = api_instance.support_departments_list()
        print("The response of SupportApi->support_departments_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportApi->support_departments_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Department]**](Department.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **support_departments_list2**
> List[Department] support_departments_list2()

List available support departments.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.department import Department
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

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.SupportApi(api_client)

    try:
        api_response = api_instance.support_departments_list2()
        print("The response of SupportApi->support_departments_list2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportApi->support_departments_list2: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Department]**](Department.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **support_tickets_close_create**
> TicketCloseResponse support_tickets_close_create(id)

Close a ticket.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.ticket_close_response import TicketCloseResponse
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

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.SupportApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.support_tickets_close_create(id)
        print("The response of SupportApi->support_tickets_close_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportApi->support_tickets_close_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**TicketCloseResponse**](TicketCloseResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **support_tickets_close_create2**
> TicketCloseResponse support_tickets_close_create2(id)

Close a ticket.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.ticket_close_response import TicketCloseResponse
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

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.SupportApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.support_tickets_close_create2(id)
        print("The response of SupportApi->support_tickets_close_create2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportApi->support_tickets_close_create2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**TicketCloseResponse**](TicketCloseResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **support_tickets_create**
> TicketDetail support_tickets_create(ticket_create)

Create a new support ticket.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.ticket_create import TicketCreate
from pidginhost_sdk.models.ticket_detail import TicketDetail
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

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.SupportApi(api_client)
    ticket_create = pidginhost_sdk.TicketCreate() # TicketCreate | 

    try:
        api_response = api_instance.support_tickets_create(ticket_create)
        print("The response of SupportApi->support_tickets_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportApi->support_tickets_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_create** | [**TicketCreate**](TicketCreate.md)|  | 

### Return type

[**TicketDetail**](TicketDetail.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **support_tickets_create2**
> TicketDetail support_tickets_create2(ticket_create)

Create a new support ticket.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.ticket_create import TicketCreate
from pidginhost_sdk.models.ticket_detail import TicketDetail
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

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.SupportApi(api_client)
    ticket_create = pidginhost_sdk.TicketCreate() # TicketCreate | 

    try:
        api_response = api_instance.support_tickets_create2(ticket_create)
        print("The response of SupportApi->support_tickets_create2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportApi->support_tickets_create2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_create** | [**TicketCreate**](TicketCreate.md)|  | 

### Return type

[**TicketDetail**](TicketDetail.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **support_tickets_list**
> PaginatedTicketListList support_tickets_list(page=page)

List, create, and manage support tickets.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.paginated_ticket_list_list import PaginatedTicketListList
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

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.SupportApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.support_tickets_list(page=page)
        print("The response of SupportApi->support_tickets_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportApi->support_tickets_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedTicketListList**](PaginatedTicketListList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **support_tickets_list2**
> PaginatedTicketListList support_tickets_list2(page=page)

List, create, and manage support tickets.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.paginated_ticket_list_list import PaginatedTicketListList
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

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.SupportApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.support_tickets_list2(page=page)
        print("The response of SupportApi->support_tickets_list2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportApi->support_tickets_list2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedTicketListList**](PaginatedTicketListList.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **support_tickets_messages_attachment_retrieve**
> bytearray support_tickets_messages_attachment_retrieve(id, message_id)

Download an attachment from a ticket message.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

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

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.SupportApi(api_client)
    id = 'id_example' # str | 
    message_id = 'message_id_example' # str | 

    try:
        api_response = api_instance.support_tickets_messages_attachment_retrieve(id, message_id)
        print("The response of SupportApi->support_tickets_messages_attachment_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportApi->support_tickets_messages_attachment_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **message_id** | **str**|  | 

### Return type

**bytearray**

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **support_tickets_messages_attachment_retrieve2**
> bytearray support_tickets_messages_attachment_retrieve2(id, message_id)

Download an attachment from a ticket message.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

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

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.SupportApi(api_client)
    id = 'id_example' # str | 
    message_id = 'message_id_example' # str | 

    try:
        api_response = api_instance.support_tickets_messages_attachment_retrieve2(id, message_id)
        print("The response of SupportApi->support_tickets_messages_attachment_retrieve2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportApi->support_tickets_messages_attachment_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **message_id** | **str**|  | 

### Return type

**bytearray**

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **support_tickets_reopen_create**
> TicketReopenResponse support_tickets_reopen_create(id)

Reopen a closed ticket.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.ticket_reopen_response import TicketReopenResponse
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

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.SupportApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.support_tickets_reopen_create(id)
        print("The response of SupportApi->support_tickets_reopen_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportApi->support_tickets_reopen_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**TicketReopenResponse**](TicketReopenResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **support_tickets_reopen_create2**
> TicketReopenResponse support_tickets_reopen_create2(id)

Reopen a closed ticket.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.ticket_reopen_response import TicketReopenResponse
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

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.SupportApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.support_tickets_reopen_create2(id)
        print("The response of SupportApi->support_tickets_reopen_create2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportApi->support_tickets_reopen_create2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**TicketReopenResponse**](TicketReopenResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **support_tickets_reply_create**
> TicketReplyResponse support_tickets_reply_create(id, ticket_reply)

Reply to a ticket.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.ticket_reply import TicketReply
from pidginhost_sdk.models.ticket_reply_response import TicketReplyResponse
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

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.SupportApi(api_client)
    id = 'id_example' # str | 
    ticket_reply = pidginhost_sdk.TicketReply() # TicketReply | 

    try:
        api_response = api_instance.support_tickets_reply_create(id, ticket_reply)
        print("The response of SupportApi->support_tickets_reply_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportApi->support_tickets_reply_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **ticket_reply** | [**TicketReply**](TicketReply.md)|  | 

### Return type

[**TicketReplyResponse**](TicketReplyResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **support_tickets_reply_create2**
> TicketReplyResponse support_tickets_reply_create2(id, ticket_reply)

Reply to a ticket.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.ticket_reply import TicketReply
from pidginhost_sdk.models.ticket_reply_response import TicketReplyResponse
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

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.SupportApi(api_client)
    id = 'id_example' # str | 
    ticket_reply = pidginhost_sdk.TicketReply() # TicketReply | 

    try:
        api_response = api_instance.support_tickets_reply_create2(id, ticket_reply)
        print("The response of SupportApi->support_tickets_reply_create2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportApi->support_tickets_reply_create2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **ticket_reply** | [**TicketReply**](TicketReply.md)|  | 

### Return type

[**TicketReplyResponse**](TicketReplyResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **support_tickets_retrieve**
> TicketDetail support_tickets_retrieve(id)

List, create, and manage support tickets.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.ticket_detail import TicketDetail
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

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.SupportApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.support_tickets_retrieve(id)
        print("The response of SupportApi->support_tickets_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportApi->support_tickets_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**TicketDetail**](TicketDetail.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **support_tickets_retrieve2**
> TicketDetail support_tickets_retrieve2(id)

List, create, and manage support tickets.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.ticket_detail import TicketDetail
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

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with pidginhost_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pidginhost_sdk.SupportApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.support_tickets_retrieve2(id)
        print("The response of SupportApi->support_tickets_retrieve2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SupportApi->support_tickets_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**TicketDetail**](TicketDetail.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

