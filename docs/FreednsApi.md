# pidginhost_sdk.FreednsApi

All URIs are relative to *https://www.pidginhost.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**freedns_dns_activate_create**](FreednsApi.md#freedns_dns_activate_create) | **POST** /api/freedns/dns/activate/ | 
[**freedns_dns_activate_create2**](FreednsApi.md#freedns_dns_activate_create2) | **POST** /api/v1/freedns/dns/activate/ | 
[**freedns_dns_add_record_create**](FreednsApi.md#freedns_dns_add_record_create) | **POST** /api/freedns/dns/add-record/ | 
[**freedns_dns_add_record_create2**](FreednsApi.md#freedns_dns_add_record_create2) | **POST** /api/v1/freedns/dns/add-record/ | 
[**freedns_dns_deactivate_create**](FreednsApi.md#freedns_dns_deactivate_create) | **POST** /api/freedns/dns/deactivate/ | 
[**freedns_dns_deactivate_create2**](FreednsApi.md#freedns_dns_deactivate_create2) | **POST** /api/v1/freedns/dns/deactivate/ | 
[**freedns_dns_delete_record_create**](FreednsApi.md#freedns_dns_delete_record_create) | **POST** /api/freedns/dns/delete-record/ | 
[**freedns_dns_delete_record_create2**](FreednsApi.md#freedns_dns_delete_record_create2) | **POST** /api/v1/freedns/dns/delete-record/ | 
[**freedns_dns_list**](FreednsApi.md#freedns_dns_list) | **GET** /api/freedns/dns/ | 
[**freedns_dns_list2**](FreednsApi.md#freedns_dns_list2) | **GET** /api/v1/freedns/dns/ | 
[**freedns_dns_records_list**](FreednsApi.md#freedns_dns_records_list) | **GET** /api/freedns/dns/records/ | 
[**freedns_dns_records_list2**](FreednsApi.md#freedns_dns_records_list2) | **GET** /api/v1/freedns/dns/records/ | 


# **freedns_dns_activate_create**
> ActivateFreeDNSResponse freedns_dns_activate_create(activate_free_dns)

Activate FreeDNS for a domain. For internal domains the nameservers are changed to PidginHost NS. A default zone is created on the cPanel node.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.activate_free_dns import ActivateFreeDNS
from pidginhost_sdk.models.activate_free_dns_response import ActivateFreeDNSResponse
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
    api_instance = pidginhost_sdk.FreednsApi(api_client)
    activate_free_dns = pidginhost_sdk.ActivateFreeDNS() # ActivateFreeDNS | 

    try:
        api_response = api_instance.freedns_dns_activate_create(activate_free_dns)
        print("The response of FreednsApi->freedns_dns_activate_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FreednsApi->freedns_dns_activate_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activate_free_dns** | [**ActivateFreeDNS**](ActivateFreeDNS.md)|  | 

### Return type

[**ActivateFreeDNSResponse**](ActivateFreeDNSResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **freedns_dns_activate_create2**
> ActivateFreeDNSResponse freedns_dns_activate_create2(activate_free_dns)

Activate FreeDNS for a domain. For internal domains the nameservers are changed to PidginHost NS. A default zone is created on the cPanel node.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.activate_free_dns import ActivateFreeDNS
from pidginhost_sdk.models.activate_free_dns_response import ActivateFreeDNSResponse
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
    api_instance = pidginhost_sdk.FreednsApi(api_client)
    activate_free_dns = pidginhost_sdk.ActivateFreeDNS() # ActivateFreeDNS | 

    try:
        api_response = api_instance.freedns_dns_activate_create2(activate_free_dns)
        print("The response of FreednsApi->freedns_dns_activate_create2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FreednsApi->freedns_dns_activate_create2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activate_free_dns** | [**ActivateFreeDNS**](ActivateFreeDNS.md)|  | 

### Return type

[**ActivateFreeDNSResponse**](ActivateFreeDNSResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **freedns_dns_add_record_create**
> DNSRecordMutateResponse freedns_dns_add_record_create(domain, source, dns_record_create)

Add or edit a DNS record. To edit an existing record, include the 'line' field with its line number. Required type-specific fields depend on 'type': A/AAAA → address; CNAME → cname; MX → preference, exchange; SRV → priority, weight, port, target; TXT → txtdata, unencoded; TYPE257 (CAA) → flag, tag, value.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.dns_record_create import DNSRecordCreate
from pidginhost_sdk.models.dns_record_mutate_response import DNSRecordMutateResponse
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
    api_instance = pidginhost_sdk.FreednsApi(api_client)
    domain = 'domain_example' # str | Domain name or PK.
    source = 'source_example' # str | 'internal' or 'external'.
    dns_record_create = pidginhost_sdk.DNSRecordCreate() # DNSRecordCreate | 

    try:
        api_response = api_instance.freedns_dns_add_record_create(domain, source, dns_record_create)
        print("The response of FreednsApi->freedns_dns_add_record_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FreednsApi->freedns_dns_add_record_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain name or PK. | 
 **source** | **str**| &#39;internal&#39; or &#39;external&#39;. | 
 **dns_record_create** | [**DNSRecordCreate**](DNSRecordCreate.md)|  | 

### Return type

[**DNSRecordMutateResponse**](DNSRecordMutateResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **freedns_dns_add_record_create2**
> DNSRecordMutateResponse freedns_dns_add_record_create2(domain, source, dns_record_create)

Add or edit a DNS record. To edit an existing record, include the 'line' field with its line number. Required type-specific fields depend on 'type': A/AAAA → address; CNAME → cname; MX → preference, exchange; SRV → priority, weight, port, target; TXT → txtdata, unencoded; TYPE257 (CAA) → flag, tag, value.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.dns_record_create import DNSRecordCreate
from pidginhost_sdk.models.dns_record_mutate_response import DNSRecordMutateResponse
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
    api_instance = pidginhost_sdk.FreednsApi(api_client)
    domain = 'domain_example' # str | Domain name or PK.
    source = 'source_example' # str | 'internal' or 'external'.
    dns_record_create = pidginhost_sdk.DNSRecordCreate() # DNSRecordCreate | 

    try:
        api_response = api_instance.freedns_dns_add_record_create2(domain, source, dns_record_create)
        print("The response of FreednsApi->freedns_dns_add_record_create2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FreednsApi->freedns_dns_add_record_create2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain name or PK. | 
 **source** | **str**| &#39;internal&#39; or &#39;external&#39;. | 
 **dns_record_create** | [**DNSRecordCreate**](DNSRecordCreate.md)|  | 

### Return type

[**DNSRecordMutateResponse**](DNSRecordMutateResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **freedns_dns_deactivate_create**
> DeactivateFreeDNSResponse freedns_dns_deactivate_create(deactivate_free_dns)

Deactivate FreeDNS for a domain. The DNS zone is removed from the cPanel node and, for internal domains, the original nameservers are restored.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.deactivate_free_dns import DeactivateFreeDNS
from pidginhost_sdk.models.deactivate_free_dns_response import DeactivateFreeDNSResponse
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
    api_instance = pidginhost_sdk.FreednsApi(api_client)
    deactivate_free_dns = pidginhost_sdk.DeactivateFreeDNS() # DeactivateFreeDNS | 

    try:
        api_response = api_instance.freedns_dns_deactivate_create(deactivate_free_dns)
        print("The response of FreednsApi->freedns_dns_deactivate_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FreednsApi->freedns_dns_deactivate_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deactivate_free_dns** | [**DeactivateFreeDNS**](DeactivateFreeDNS.md)|  | 

### Return type

[**DeactivateFreeDNSResponse**](DeactivateFreeDNSResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **freedns_dns_deactivate_create2**
> DeactivateFreeDNSResponse freedns_dns_deactivate_create2(deactivate_free_dns)

Deactivate FreeDNS for a domain. The DNS zone is removed from the cPanel node and, for internal domains, the original nameservers are restored.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.deactivate_free_dns import DeactivateFreeDNS
from pidginhost_sdk.models.deactivate_free_dns_response import DeactivateFreeDNSResponse
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
    api_instance = pidginhost_sdk.FreednsApi(api_client)
    deactivate_free_dns = pidginhost_sdk.DeactivateFreeDNS() # DeactivateFreeDNS | 

    try:
        api_response = api_instance.freedns_dns_deactivate_create2(deactivate_free_dns)
        print("The response of FreednsApi->freedns_dns_deactivate_create2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FreednsApi->freedns_dns_deactivate_create2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deactivate_free_dns** | [**DeactivateFreeDNS**](DeactivateFreeDNS.md)|  | 

### Return type

[**DeactivateFreeDNSResponse**](DeactivateFreeDNSResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **freedns_dns_delete_record_create**
> DeleteRecordResponse freedns_dns_delete_record_create(domain, source, delete_record)

Delete a DNS record by its line number.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.delete_record import DeleteRecord
from pidginhost_sdk.models.delete_record_response import DeleteRecordResponse
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
    api_instance = pidginhost_sdk.FreednsApi(api_client)
    domain = 'domain_example' # str | Domain name or PK.
    source = 'source_example' # str | 'internal' or 'external'.
    delete_record = pidginhost_sdk.DeleteRecord() # DeleteRecord | 

    try:
        api_response = api_instance.freedns_dns_delete_record_create(domain, source, delete_record)
        print("The response of FreednsApi->freedns_dns_delete_record_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FreednsApi->freedns_dns_delete_record_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain name or PK. | 
 **source** | **str**| &#39;internal&#39; or &#39;external&#39;. | 
 **delete_record** | [**DeleteRecord**](DeleteRecord.md)|  | 

### Return type

[**DeleteRecordResponse**](DeleteRecordResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **freedns_dns_delete_record_create2**
> DeleteRecordResponse freedns_dns_delete_record_create2(domain, source, delete_record)

Delete a DNS record by its line number.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.delete_record import DeleteRecord
from pidginhost_sdk.models.delete_record_response import DeleteRecordResponse
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
    api_instance = pidginhost_sdk.FreednsApi(api_client)
    domain = 'domain_example' # str | Domain name or PK.
    source = 'source_example' # str | 'internal' or 'external'.
    delete_record = pidginhost_sdk.DeleteRecord() # DeleteRecord | 

    try:
        api_response = api_instance.freedns_dns_delete_record_create2(domain, source, delete_record)
        print("The response of FreednsApi->freedns_dns_delete_record_create2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FreednsApi->freedns_dns_delete_record_create2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain name or PK. | 
 **source** | **str**| &#39;internal&#39; or &#39;external&#39;. | 
 **delete_record** | [**DeleteRecord**](DeleteRecord.md)|  | 

### Return type

[**DeleteRecordResponse**](DeleteRecordResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **freedns_dns_list**
> List[FreeDNSDomain] freedns_dns_list()

List all domains with active FreeDNS for the authenticated user.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.free_dns_domain import FreeDNSDomain
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
    api_instance = pidginhost_sdk.FreednsApi(api_client)

    try:
        api_response = api_instance.freedns_dns_list()
        print("The response of FreednsApi->freedns_dns_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FreednsApi->freedns_dns_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[FreeDNSDomain]**](FreeDNSDomain.md)

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

# **freedns_dns_list2**
> List[FreeDNSDomain] freedns_dns_list2()

List all domains with active FreeDNS for the authenticated user.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.free_dns_domain import FreeDNSDomain
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
    api_instance = pidginhost_sdk.FreednsApi(api_client)

    try:
        api_response = api_instance.freedns_dns_list2()
        print("The response of FreednsApi->freedns_dns_list2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FreednsApi->freedns_dns_list2: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[FreeDNSDomain]**](FreeDNSDomain.md)

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

# **freedns_dns_records_list**
> List[DNSRecord] freedns_dns_records_list(domain, source)

List all DNS records for a domain with active FreeDNS.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.dns_record import DNSRecord
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
    api_instance = pidginhost_sdk.FreednsApi(api_client)
    domain = 'domain_example' # str | Domain name or PK.
    source = 'source_example' # str | 'internal' or 'external'.

    try:
        api_response = api_instance.freedns_dns_records_list(domain, source)
        print("The response of FreednsApi->freedns_dns_records_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FreednsApi->freedns_dns_records_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain name or PK. | 
 **source** | **str**| &#39;internal&#39; or &#39;external&#39;. | 

### Return type

[**List[DNSRecord]**](DNSRecord.md)

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

# **freedns_dns_records_list2**
> List[DNSRecord] freedns_dns_records_list2(domain, source)

List all DNS records for a domain with active FreeDNS.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.dns_record import DNSRecord
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
    api_instance = pidginhost_sdk.FreednsApi(api_client)
    domain = 'domain_example' # str | Domain name or PK.
    source = 'source_example' # str | 'internal' or 'external'.

    try:
        api_response = api_instance.freedns_dns_records_list2(domain, source)
        print("The response of FreednsApi->freedns_dns_records_list2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FreednsApi->freedns_dns_records_list2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Domain name or PK. | 
 **source** | **str**| &#39;internal&#39; or &#39;external&#39;. | 

### Return type

[**List[DNSRecord]**](DNSRecord.md)

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

