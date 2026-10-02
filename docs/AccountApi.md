# pidginhost_sdk.AccountApi

All URIs are relative to *https://www.pidginhost.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_api_tokens_create**](AccountApi.md#account_api_tokens_create) | **POST** /api/account/api-tokens/ | 
[**account_api_tokens_destroy**](AccountApi.md#account_api_tokens_destroy) | **DELETE** /api/account/api-tokens/{id}/ | 
[**account_api_tokens_list**](AccountApi.md#account_api_tokens_list) | **GET** /api/account/api-tokens/ | 
[**account_companies_create**](AccountApi.md#account_companies_create) | **POST** /api/account/companies/ | 
[**account_companies_destroy**](AccountApi.md#account_companies_destroy) | **DELETE** /api/account/companies/{id}/ | 
[**account_companies_list**](AccountApi.md#account_companies_list) | **GET** /api/account/companies/ | 
[**account_companies_partial_update**](AccountApi.md#account_companies_partial_update) | **PATCH** /api/account/companies/{id}/ | 
[**account_companies_retrieve**](AccountApi.md#account_companies_retrieve) | **GET** /api/account/companies/{id}/ | 
[**account_companies_update**](AccountApi.md#account_companies_update) | **PUT** /api/account/companies/{id}/ | 
[**account_emails_list**](AccountApi.md#account_emails_list) | **GET** /api/account/emails/ | 
[**account_profile_partial_update**](AccountApi.md#account_profile_partial_update) | **PATCH** /api/account/profile | 
[**account_profile_retrieve**](AccountApi.md#account_profile_retrieve) | **GET** /api/account/profile | 
[**account_profile_update**](AccountApi.md#account_profile_update) | **PUT** /api/account/profile | 
[**account_ssh_keys_create**](AccountApi.md#account_ssh_keys_create) | **POST** /api/account/ssh-keys/ | 
[**account_ssh_keys_destroy**](AccountApi.md#account_ssh_keys_destroy) | **DELETE** /api/account/ssh-keys/{id}/ | 
[**account_ssh_keys_list**](AccountApi.md#account_ssh_keys_list) | **GET** /api/account/ssh-keys/ | 
[**account_ssh_keys_partial_update**](AccountApi.md#account_ssh_keys_partial_update) | **PATCH** /api/account/ssh-keys/{id}/ | 
[**account_ssh_keys_retrieve**](AccountApi.md#account_ssh_keys_retrieve) | **GET** /api/account/ssh-keys/{id}/ | 
[**account_ssh_keys_update**](AccountApi.md#account_ssh_keys_update) | **PUT** /api/account/ssh-keys/{id}/ | 


# **account_api_tokens_create**
> APITokenCreate account_api_tokens_create(api_token_create_request)

Manage your API tokens

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.api_token_create import APITokenCreate
from pidginhost_sdk.models.api_token_create_request import APITokenCreateRequest
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
    api_instance = pidginhost_sdk.AccountApi(api_client)
    api_token_create_request = pidginhost_sdk.APITokenCreateRequest() # APITokenCreateRequest | 

    try:
        api_response = api_instance.account_api_tokens_create(api_token_create_request)
        print("The response of AccountApi->account_api_tokens_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->account_api_tokens_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token_create_request** | [**APITokenCreateRequest**](APITokenCreateRequest.md)|  | 

### Return type

[**APITokenCreate**](APITokenCreate.md)

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

# **account_api_tokens_destroy**
> account_api_tokens_destroy(id)

Manage your API tokens

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
    api_instance = pidginhost_sdk.AccountApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.account_api_tokens_destroy(id)
    except Exception as e:
        print("Exception when calling AccountApi->account_api_tokens_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **account_api_tokens_list**
> PaginatedAPITokenListList account_api_tokens_list(page=page)

Manage your API tokens

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.paginated_api_token_list_list import PaginatedAPITokenListList
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
    api_instance = pidginhost_sdk.AccountApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.account_api_tokens_list(page=page)
        print("The response of AccountApi->account_api_tokens_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->account_api_tokens_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedAPITokenListList**](PaginatedAPITokenListList.md)

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

# **account_companies_create**
> Company account_companies_create(company_request)

Manage your companies

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.company import Company
from pidginhost_sdk.models.company_request import CompanyRequest
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
    api_instance = pidginhost_sdk.AccountApi(api_client)
    company_request = pidginhost_sdk.CompanyRequest() # CompanyRequest | 

    try:
        api_response = api_instance.account_companies_create(company_request)
        print("The response of AccountApi->account_companies_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->account_companies_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_request** | [**CompanyRequest**](CompanyRequest.md)|  | 

### Return type

[**Company**](Company.md)

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

# **account_companies_destroy**
> account_companies_destroy(id)

Manage your companies

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
    api_instance = pidginhost_sdk.AccountApi(api_client)
    id = 56 # int | A unique integer value identifying this company.

    try:
        api_instance.account_companies_destroy(id)
    except Exception as e:
        print("Exception when calling AccountApi->account_companies_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this company. | 

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

# **account_companies_list**
> PaginatedCompanyList account_companies_list(page=page)

Manage your companies

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.paginated_company_list import PaginatedCompanyList
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
    api_instance = pidginhost_sdk.AccountApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.account_companies_list(page=page)
        print("The response of AccountApi->account_companies_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->account_companies_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedCompanyList**](PaginatedCompanyList.md)

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

# **account_companies_partial_update**
> Company account_companies_partial_update(id, patched_company_request=patched_company_request)

Manage your companies

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.company import Company
from pidginhost_sdk.models.patched_company_request import PatchedCompanyRequest
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
    api_instance = pidginhost_sdk.AccountApi(api_client)
    id = 56 # int | A unique integer value identifying this company.
    patched_company_request = pidginhost_sdk.PatchedCompanyRequest() # PatchedCompanyRequest |  (optional)

    try:
        api_response = api_instance.account_companies_partial_update(id, patched_company_request=patched_company_request)
        print("The response of AccountApi->account_companies_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->account_companies_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this company. | 
 **patched_company_request** | [**PatchedCompanyRequest**](PatchedCompanyRequest.md)|  | [optional] 

### Return type

[**Company**](Company.md)

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

# **account_companies_retrieve**
> Company account_companies_retrieve(id)

Manage your companies

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.company import Company
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
    api_instance = pidginhost_sdk.AccountApi(api_client)
    id = 56 # int | A unique integer value identifying this company.

    try:
        api_response = api_instance.account_companies_retrieve(id)
        print("The response of AccountApi->account_companies_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->account_companies_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this company. | 

### Return type

[**Company**](Company.md)

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

# **account_companies_update**
> Company account_companies_update(id, company_request)

Manage your companies

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.company import Company
from pidginhost_sdk.models.company_request import CompanyRequest
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
    api_instance = pidginhost_sdk.AccountApi(api_client)
    id = 56 # int | A unique integer value identifying this company.
    company_request = pidginhost_sdk.CompanyRequest() # CompanyRequest | 

    try:
        api_response = api_instance.account_companies_update(id, company_request)
        print("The response of AccountApi->account_companies_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->account_companies_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this company. | 
 **company_request** | [**CompanyRequest**](CompanyRequest.md)|  | 

### Return type

[**Company**](Company.md)

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

# **account_emails_list**
> PaginatedEmailHistoryList account_emails_list(page=page)

List email history for the authenticated user.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.paginated_email_history_list import PaginatedEmailHistoryList
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
    api_instance = pidginhost_sdk.AccountApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.account_emails_list(page=page)
        print("The response of AccountApi->account_emails_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->account_emails_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedEmailHistoryList**](PaginatedEmailHistoryList.md)

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

# **account_profile_partial_update**
> Profile account_profile_partial_update(patched_profile_request=patched_profile_request)

Manage your profile data

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.patched_profile_request import PatchedProfileRequest
from pidginhost_sdk.models.profile import Profile
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
    api_instance = pidginhost_sdk.AccountApi(api_client)
    patched_profile_request = pidginhost_sdk.PatchedProfileRequest() # PatchedProfileRequest |  (optional)

    try:
        api_response = api_instance.account_profile_partial_update(patched_profile_request=patched_profile_request)
        print("The response of AccountApi->account_profile_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->account_profile_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patched_profile_request** | [**PatchedProfileRequest**](PatchedProfileRequest.md)|  | [optional] 

### Return type

[**Profile**](Profile.md)

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

# **account_profile_retrieve**
> Profile account_profile_retrieve()

Manage your profile data

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.profile import Profile
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
    api_instance = pidginhost_sdk.AccountApi(api_client)

    try:
        api_response = api_instance.account_profile_retrieve()
        print("The response of AccountApi->account_profile_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->account_profile_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Profile**](Profile.md)

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

# **account_profile_update**
> Profile account_profile_update(profile_request)

Manage your profile data

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.profile import Profile
from pidginhost_sdk.models.profile_request import ProfileRequest
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
    api_instance = pidginhost_sdk.AccountApi(api_client)
    profile_request = pidginhost_sdk.ProfileRequest() # ProfileRequest | 

    try:
        api_response = api_instance.account_profile_update(profile_request)
        print("The response of AccountApi->account_profile_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->account_profile_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_request** | [**ProfileRequest**](ProfileRequest.md)|  | 

### Return type

[**Profile**](Profile.md)

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

# **account_ssh_keys_create**
> SSHKey account_ssh_keys_create(ssh_key_request)

Account context + IAM role enforcement for the account residue:
billing identity (profile/companies/email history) is owner-only account
state, SSH keys are account infra, tokens stay actor-owned.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.ssh_key import SSHKey
from pidginhost_sdk.models.ssh_key_request import SSHKeyRequest
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
    api_instance = pidginhost_sdk.AccountApi(api_client)
    ssh_key_request = pidginhost_sdk.SSHKeyRequest() # SSHKeyRequest | 

    try:
        api_response = api_instance.account_ssh_keys_create(ssh_key_request)
        print("The response of AccountApi->account_ssh_keys_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->account_ssh_keys_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_key_request** | [**SSHKeyRequest**](SSHKeyRequest.md)|  | 

### Return type

[**SSHKey**](SSHKey.md)

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

# **account_ssh_keys_destroy**
> account_ssh_keys_destroy(id)

Account context + IAM role enforcement for the account residue:
billing identity (profile/companies/email history) is owner-only account
state, SSH keys are account infra, tokens stay actor-owned.

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
    api_instance = pidginhost_sdk.AccountApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.account_ssh_keys_destroy(id)
    except Exception as e:
        print("Exception when calling AccountApi->account_ssh_keys_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **account_ssh_keys_list**
> PaginatedSSHKeyList account_ssh_keys_list(page=page)

Account context + IAM role enforcement for the account residue:
billing identity (profile/companies/email history) is owner-only account
state, SSH keys are account infra, tokens stay actor-owned.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.paginated_ssh_key_list import PaginatedSSHKeyList
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
    api_instance = pidginhost_sdk.AccountApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.account_ssh_keys_list(page=page)
        print("The response of AccountApi->account_ssh_keys_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->account_ssh_keys_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedSSHKeyList**](PaginatedSSHKeyList.md)

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

# **account_ssh_keys_partial_update**
> SSHKey account_ssh_keys_partial_update(id, patched_ssh_key_update_request=patched_ssh_key_update_request)

Account context + IAM role enforcement for the account residue:
billing identity (profile/companies/email history) is owner-only account
state, SSH keys are account infra, tokens stay actor-owned.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.patched_ssh_key_update_request import PatchedSSHKeyUpdateRequest
from pidginhost_sdk.models.ssh_key import SSHKey
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
    api_instance = pidginhost_sdk.AccountApi(api_client)
    id = 'id_example' # str | 
    patched_ssh_key_update_request = pidginhost_sdk.PatchedSSHKeyUpdateRequest() # PatchedSSHKeyUpdateRequest |  (optional)

    try:
        api_response = api_instance.account_ssh_keys_partial_update(id, patched_ssh_key_update_request=patched_ssh_key_update_request)
        print("The response of AccountApi->account_ssh_keys_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->account_ssh_keys_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **patched_ssh_key_update_request** | [**PatchedSSHKeyUpdateRequest**](PatchedSSHKeyUpdateRequest.md)|  | [optional] 

### Return type

[**SSHKey**](SSHKey.md)

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

# **account_ssh_keys_retrieve**
> SSHKey account_ssh_keys_retrieve(id)

Account context + IAM role enforcement for the account residue:
billing identity (profile/companies/email history) is owner-only account
state, SSH keys are account infra, tokens stay actor-owned.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.ssh_key import SSHKey
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
    api_instance = pidginhost_sdk.AccountApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.account_ssh_keys_retrieve(id)
        print("The response of AccountApi->account_ssh_keys_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->account_ssh_keys_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SSHKey**](SSHKey.md)

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

# **account_ssh_keys_update**
> SSHKey account_ssh_keys_update(id, ssh_key_update_request=ssh_key_update_request)

Account context + IAM role enforcement for the account residue:
billing identity (profile/companies/email history) is owner-only account
state, SSH keys are account infra, tokens stay actor-owned.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.ssh_key import SSHKey
from pidginhost_sdk.models.ssh_key_update_request import SSHKeyUpdateRequest
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
    api_instance = pidginhost_sdk.AccountApi(api_client)
    id = 'id_example' # str | 
    ssh_key_update_request = pidginhost_sdk.SSHKeyUpdateRequest() # SSHKeyUpdateRequest |  (optional)

    try:
        api_response = api_instance.account_ssh_keys_update(id, ssh_key_update_request=ssh_key_update_request)
        print("The response of AccountApi->account_ssh_keys_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->account_ssh_keys_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **ssh_key_update_request** | [**SSHKeyUpdateRequest**](SSHKeyUpdateRequest.md)|  | [optional] 

### Return type

[**SSHKey**](SSHKey.md)

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

