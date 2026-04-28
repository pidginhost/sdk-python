# pidginhost_sdk.KubernetesApi

All URIs are relative to *https://www.pidginhost.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**kubernetes_cluster_types_list**](KubernetesApi.md#kubernetes_cluster_types_list) | **GET** /api/kubernetes/cluster-types/ | 
[**kubernetes_clusters_connect_vm_create**](KubernetesApi.md#kubernetes_clusters_connect_vm_create) | **POST** /api/kubernetes/clusters/{id}/connect-vm/ | 
[**kubernetes_clusters_connected_vms_retrieve**](KubernetesApi.md#kubernetes_clusters_connected_vms_retrieve) | **GET** /api/kubernetes/clusters/{id}/connected-vms/ | 
[**kubernetes_clusters_create**](KubernetesApi.md#kubernetes_clusters_create) | **POST** /api/kubernetes/clusters/ | 
[**kubernetes_clusters_destroy**](KubernetesApi.md#kubernetes_clusters_destroy) | **DELETE** /api/kubernetes/clusters/{id}/ | 
[**kubernetes_clusters_disconnect_vm_create**](KubernetesApi.md#kubernetes_clusters_disconnect_vm_create) | **POST** /api/kubernetes/clusters/{id}/disconnect-vm/ | 
[**kubernetes_clusters_eligible_vms_retrieve**](KubernetesApi.md#kubernetes_clusters_eligible_vms_retrieve) | **GET** /api/kubernetes/clusters/{id}/eligible-vms/ | 
[**kubernetes_clusters_httproutes_create**](KubernetesApi.md#kubernetes_clusters_httproutes_create) | **POST** /api/kubernetes/clusters/{cluster_id}/httproutes/ | 
[**kubernetes_clusters_httproutes_destroy**](KubernetesApi.md#kubernetes_clusters_httproutes_destroy) | **DELETE** /api/kubernetes/clusters/{cluster_id}/httproutes/{id}/ | 
[**kubernetes_clusters_httproutes_partial_update**](KubernetesApi.md#kubernetes_clusters_httproutes_partial_update) | **PATCH** /api/kubernetes/clusters/{cluster_id}/httproutes/{id}/ | 
[**kubernetes_clusters_httproutes_retrieve**](KubernetesApi.md#kubernetes_clusters_httproutes_retrieve) | **GET** /api/kubernetes/clusters/{cluster_id}/httproutes/ | 
[**kubernetes_clusters_httproutes_retrieve2**](KubernetesApi.md#kubernetes_clusters_httproutes_retrieve2) | **GET** /api/kubernetes/clusters/{cluster_id}/httproutes/{id}/ | 
[**kubernetes_clusters_httproutes_update**](KubernetesApi.md#kubernetes_clusters_httproutes_update) | **PUT** /api/kubernetes/clusters/{cluster_id}/httproutes/{id}/ | 
[**kubernetes_clusters_kube_version_upgrade_create**](KubernetesApi.md#kubernetes_clusters_kube_version_upgrade_create) | **POST** /api/kubernetes/clusters/{id}/kube-version-upgrade/ | 
[**kubernetes_clusters_kubeconfig_create**](KubernetesApi.md#kubernetes_clusters_kubeconfig_create) | **POST** /api/kubernetes/clusters/{id}/kubeconfig/ | 
[**kubernetes_clusters_kubeconfig_retrieve**](KubernetesApi.md#kubernetes_clusters_kubeconfig_retrieve) | **GET** /api/kubernetes/clusters/{id}/kubeconfig/ | 
[**kubernetes_clusters_lb_firewall_create**](KubernetesApi.md#kubernetes_clusters_lb_firewall_create) | **POST** /api/kubernetes/clusters/{cluster_id}/lb-firewall/ | 
[**kubernetes_clusters_lb_firewall_destroy**](KubernetesApi.md#kubernetes_clusters_lb_firewall_destroy) | **DELETE** /api/kubernetes/clusters/{cluster_id}/lb-firewall/{id}/ | 
[**kubernetes_clusters_lb_firewall_list**](KubernetesApi.md#kubernetes_clusters_lb_firewall_list) | **GET** /api/kubernetes/clusters/{cluster_id}/lb-firewall/ | 
[**kubernetes_clusters_lb_firewall_partial_update**](KubernetesApi.md#kubernetes_clusters_lb_firewall_partial_update) | **PATCH** /api/kubernetes/clusters/{cluster_id}/lb-firewall/{id}/ | 
[**kubernetes_clusters_lb_firewall_retrieve**](KubernetesApi.md#kubernetes_clusters_lb_firewall_retrieve) | **GET** /api/kubernetes/clusters/{cluster_id}/lb-firewall/{id}/ | 
[**kubernetes_clusters_lb_firewall_update**](KubernetesApi.md#kubernetes_clusters_lb_firewall_update) | **PUT** /api/kubernetes/clusters/{cluster_id}/lb-firewall/{id}/ | 
[**kubernetes_clusters_list**](KubernetesApi.md#kubernetes_clusters_list) | **GET** /api/kubernetes/clusters/ | 
[**kubernetes_clusters_partial_update**](KubernetesApi.md#kubernetes_clusters_partial_update) | **PATCH** /api/kubernetes/clusters/{id}/ | 
[**kubernetes_clusters_port_forwards_create**](KubernetesApi.md#kubernetes_clusters_port_forwards_create) | **POST** /api/kubernetes/clusters/{cluster_id}/port-forwards/ | 
[**kubernetes_clusters_port_forwards_destroy**](KubernetesApi.md#kubernetes_clusters_port_forwards_destroy) | **DELETE** /api/kubernetes/clusters/{cluster_id}/port-forwards/{id}/ | 
[**kubernetes_clusters_port_forwards_partial_update**](KubernetesApi.md#kubernetes_clusters_port_forwards_partial_update) | **PATCH** /api/kubernetes/clusters/{cluster_id}/port-forwards/{id}/ | 
[**kubernetes_clusters_port_forwards_retrieve**](KubernetesApi.md#kubernetes_clusters_port_forwards_retrieve) | **GET** /api/kubernetes/clusters/{cluster_id}/port-forwards/ | 
[**kubernetes_clusters_port_forwards_retrieve2**](KubernetesApi.md#kubernetes_clusters_port_forwards_retrieve2) | **GET** /api/kubernetes/clusters/{cluster_id}/port-forwards/{id}/ | 
[**kubernetes_clusters_port_forwards_update**](KubernetesApi.md#kubernetes_clusters_port_forwards_update) | **PUT** /api/kubernetes/clusters/{cluster_id}/port-forwards/{id}/ | 
[**kubernetes_clusters_resource_pools_create**](KubernetesApi.md#kubernetes_clusters_resource_pools_create) | **POST** /api/kubernetes/clusters/{cluster_id}/resource-pools/ | 
[**kubernetes_clusters_resource_pools_destroy**](KubernetesApi.md#kubernetes_clusters_resource_pools_destroy) | **DELETE** /api/kubernetes/clusters/{cluster_id}/resource-pools/{id}/ | 
[**kubernetes_clusters_resource_pools_list**](KubernetesApi.md#kubernetes_clusters_resource_pools_list) | **GET** /api/kubernetes/clusters/{cluster_id}/resource-pools/ | 
[**kubernetes_clusters_resource_pools_nodes_destroy**](KubernetesApi.md#kubernetes_clusters_resource_pools_nodes_destroy) | **DELETE** /api/kubernetes/clusters/{cluster_id}/resource-pools/{pool_id}/nodes/{id}/ | 
[**kubernetes_clusters_resource_pools_nodes_list**](KubernetesApi.md#kubernetes_clusters_resource_pools_nodes_list) | **GET** /api/kubernetes/clusters/{cluster_id}/resource-pools/{pool_id}/nodes/ | 
[**kubernetes_clusters_resource_pools_nodes_metrics_retrieve**](KubernetesApi.md#kubernetes_clusters_resource_pools_nodes_metrics_retrieve) | **GET** /api/kubernetes/clusters/{cluster_id}/resource-pools/{pool_id}/nodes/{id}/metrics/ | 
[**kubernetes_clusters_resource_pools_nodes_retrieve**](KubernetesApi.md#kubernetes_clusters_resource_pools_nodes_retrieve) | **GET** /api/kubernetes/clusters/{cluster_id}/resource-pools/{pool_id}/nodes/{id}/ | 
[**kubernetes_clusters_resource_pools_nodes_rrd_retrieve**](KubernetesApi.md#kubernetes_clusters_resource_pools_nodes_rrd_retrieve) | **GET** /api/kubernetes/clusters/{cluster_id}/resource-pools/{pool_id}/nodes/{id}/rrd/ | 
[**kubernetes_clusters_resource_pools_partial_update**](KubernetesApi.md#kubernetes_clusters_resource_pools_partial_update) | **PATCH** /api/kubernetes/clusters/{cluster_id}/resource-pools/{id}/ | 
[**kubernetes_clusters_resource_pools_retrieve**](KubernetesApi.md#kubernetes_clusters_resource_pools_retrieve) | **GET** /api/kubernetes/clusters/{cluster_id}/resource-pools/{id}/ | 
[**kubernetes_clusters_resource_pools_update**](KubernetesApi.md#kubernetes_clusters_resource_pools_update) | **PUT** /api/kubernetes/clusters/{cluster_id}/resource-pools/{id}/ | 
[**kubernetes_clusters_retrieve**](KubernetesApi.md#kubernetes_clusters_retrieve) | **GET** /api/kubernetes/clusters/{id}/ | 
[**kubernetes_clusters_talos_version_upgrade_create**](KubernetesApi.md#kubernetes_clusters_talos_version_upgrade_create) | **POST** /api/kubernetes/clusters/{id}/talos-version-upgrade/ | 
[**kubernetes_clusters_tcproutes_create**](KubernetesApi.md#kubernetes_clusters_tcproutes_create) | **POST** /api/kubernetes/clusters/{cluster_id}/tcproutes/ | 
[**kubernetes_clusters_tcproutes_destroy**](KubernetesApi.md#kubernetes_clusters_tcproutes_destroy) | **DELETE** /api/kubernetes/clusters/{cluster_id}/tcproutes/{id}/ | 
[**kubernetes_clusters_tcproutes_partial_update**](KubernetesApi.md#kubernetes_clusters_tcproutes_partial_update) | **PATCH** /api/kubernetes/clusters/{cluster_id}/tcproutes/{id}/ | 
[**kubernetes_clusters_tcproutes_retrieve**](KubernetesApi.md#kubernetes_clusters_tcproutes_retrieve) | **GET** /api/kubernetes/clusters/{cluster_id}/tcproutes/ | 
[**kubernetes_clusters_tcproutes_retrieve2**](KubernetesApi.md#kubernetes_clusters_tcproutes_retrieve2) | **GET** /api/kubernetes/clusters/{cluster_id}/tcproutes/{id}/ | 
[**kubernetes_clusters_tcproutes_update**](KubernetesApi.md#kubernetes_clusters_tcproutes_update) | **PUT** /api/kubernetes/clusters/{cluster_id}/tcproutes/{id}/ | 
[**kubernetes_clusters_toggle_cloud_vm_access_create**](KubernetesApi.md#kubernetes_clusters_toggle_cloud_vm_access_create) | **POST** /api/kubernetes/clusters/{id}/toggle-cloud-vm-access/ | 
[**kubernetes_clusters_udproutes_create**](KubernetesApi.md#kubernetes_clusters_udproutes_create) | **POST** /api/kubernetes/clusters/{cluster_id}/udproutes/ | 
[**kubernetes_clusters_udproutes_destroy**](KubernetesApi.md#kubernetes_clusters_udproutes_destroy) | **DELETE** /api/kubernetes/clusters/{cluster_id}/udproutes/{id}/ | 
[**kubernetes_clusters_udproutes_partial_update**](KubernetesApi.md#kubernetes_clusters_udproutes_partial_update) | **PATCH** /api/kubernetes/clusters/{cluster_id}/udproutes/{id}/ | 
[**kubernetes_clusters_udproutes_retrieve**](KubernetesApi.md#kubernetes_clusters_udproutes_retrieve) | **GET** /api/kubernetes/clusters/{cluster_id}/udproutes/ | 
[**kubernetes_clusters_udproutes_retrieve2**](KubernetesApi.md#kubernetes_clusters_udproutes_retrieve2) | **GET** /api/kubernetes/clusters/{cluster_id}/udproutes/{id}/ | 
[**kubernetes_clusters_udproutes_update**](KubernetesApi.md#kubernetes_clusters_udproutes_update) | **PUT** /api/kubernetes/clusters/{cluster_id}/udproutes/{id}/ | 
[**kubernetes_clusters_update**](KubernetesApi.md#kubernetes_clusters_update) | **PUT** /api/kubernetes/clusters/{id}/ | 
[**kubernetes_clusters_upgrade_feature_create**](KubernetesApi.md#kubernetes_clusters_upgrade_feature_create) | **POST** /api/kubernetes/clusters/{id}/upgrade-feature/ | 


# **kubernetes_cluster_types_list**
> PaginatedClusterTypeList kubernetes_cluster_types_list(page=page)

Require complete user profile for provisioning (create) API actions.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.paginated_cluster_type_list import PaginatedClusterTypeList
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.kubernetes_cluster_types_list(page=page)
        print("The response of KubernetesApi->kubernetes_cluster_types_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_cluster_types_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedClusterTypeList**](PaginatedClusterTypeList.md)

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

# **kubernetes_clusters_connect_vm_create**
> ConnectVMResponse kubernetes_clusters_connect_vm_create(id, connect_vm_request)

Connect a cloud VM to the cluster private network.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.connect_vm_request import ConnectVMRequest
from pidginhost_sdk.models.connect_vm_response import ConnectVMResponse
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    id = 'id_example' # str | 
    connect_vm_request = pidginhost_sdk.ConnectVMRequest() # ConnectVMRequest | 

    try:
        api_response = api_instance.kubernetes_clusters_connect_vm_create(id, connect_vm_request)
        print("The response of KubernetesApi->kubernetes_clusters_connect_vm_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_connect_vm_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **connect_vm_request** | [**ConnectVMRequest**](ConnectVMRequest.md)|  | 

### Return type

[**ConnectVMResponse**](ConnectVMResponse.md)

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

# **kubernetes_clusters_connected_vms_retrieve**
> ConnectedVMsResponse kubernetes_clusters_connected_vms_retrieve(id)

List cloud VMs connected to the cluster private network.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.connected_vms_response import ConnectedVMsResponse
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.kubernetes_clusters_connected_vms_retrieve(id)
        print("The response of KubernetesApi->kubernetes_clusters_connected_vms_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_connected_vms_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ConnectedVMsResponse**](ConnectedVMsResponse.md)

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

# **kubernetes_clusters_create**
> ClusterAddResponse kubernetes_clusters_create(cluster_add)

Create new k8s cluster

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.cluster_add import ClusterAdd
from pidginhost_sdk.models.cluster_add_response import ClusterAddResponse
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_add = pidginhost_sdk.ClusterAdd() # ClusterAdd | 

    try:
        api_response = api_instance.kubernetes_clusters_create(cluster_add)
        print("The response of KubernetesApi->kubernetes_clusters_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_add** | [**ClusterAdd**](ClusterAdd.md)|  | 

### Return type

[**ClusterAddResponse**](ClusterAddResponse.md)

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

# **kubernetes_clusters_destroy**
> kubernetes_clusters_destroy(id)

Require complete user profile for provisioning (create) API actions.

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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.kubernetes_clusters_destroy(id)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_disconnect_vm_create**
> DisconnectVMResponse kubernetes_clusters_disconnect_vm_create(id, disconnect_vm_request)

Disconnect a cloud VM from the cluster private network.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.disconnect_vm_request import DisconnectVMRequest
from pidginhost_sdk.models.disconnect_vm_response import DisconnectVMResponse
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    id = 'id_example' # str | 
    disconnect_vm_request = pidginhost_sdk.DisconnectVMRequest() # DisconnectVMRequest | 

    try:
        api_response = api_instance.kubernetes_clusters_disconnect_vm_create(id, disconnect_vm_request)
        print("The response of KubernetesApi->kubernetes_clusters_disconnect_vm_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_disconnect_vm_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **disconnect_vm_request** | [**DisconnectVMRequest**](DisconnectVMRequest.md)|  | 

### Return type

[**DisconnectVMResponse**](DisconnectVMResponse.md)

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

# **kubernetes_clusters_eligible_vms_retrieve**
> EligibleVMsResponse kubernetes_clusters_eligible_vms_retrieve(id)

List cloud VMs eligible for connection to this cluster.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.eligible_vms_response import EligibleVMsResponse
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.kubernetes_clusters_eligible_vms_retrieve(id)
        print("The response of KubernetesApi->kubernetes_clusters_eligible_vms_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_eligible_vms_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**EligibleVMsResponse**](EligibleVMsResponse.md)

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

# **kubernetes_clusters_httproutes_create**
> HTTPRoute kubernetes_clusters_httproutes_create(cluster_id, http_route)

Create new HTTPRoute

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.http_route import HTTPRoute
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    http_route = pidginhost_sdk.HTTPRoute() # HTTPRoute | 

    try:
        api_response = api_instance.kubernetes_clusters_httproutes_create(cluster_id, http_route)
        print("The response of KubernetesApi->kubernetes_clusters_httproutes_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_httproutes_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **http_route** | [**HTTPRoute**](HTTPRoute.md)|  | 

### Return type

[**HTTPRoute**](HTTPRoute.md)

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

# **kubernetes_clusters_httproutes_destroy**
> kubernetes_clusters_httproutes_destroy(cluster_id, id)

ViewSet for managing HTTPRoute resources.

HTTPRoutes expose HTTP/HTTPS services through the Gateway with optional automatic TLS certificate issuance.

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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 

    try:
        api_instance.kubernetes_clusters_httproutes_destroy(cluster_id, id)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_httproutes_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_httproutes_partial_update**
> HTTPRoute kubernetes_clusters_httproutes_partial_update(cluster_id, id, patched_http_route=patched_http_route)

Partially update HTTPRoute

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.http_route import HTTPRoute
from pidginhost_sdk.models.patched_http_route import PatchedHTTPRoute
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 
    patched_http_route = pidginhost_sdk.PatchedHTTPRoute() # PatchedHTTPRoute |  (optional)

    try:
        api_response = api_instance.kubernetes_clusters_httproutes_partial_update(cluster_id, id, patched_http_route=patched_http_route)
        print("The response of KubernetesApi->kubernetes_clusters_httproutes_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_httproutes_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 
 **patched_http_route** | [**PatchedHTTPRoute**](PatchedHTTPRoute.md)|  | [optional] 

### Return type

[**HTTPRoute**](HTTPRoute.md)

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

# **kubernetes_clusters_httproutes_retrieve**
> kubernetes_clusters_httproutes_retrieve(cluster_id)

ViewSet for managing HTTPRoute resources.

HTTPRoutes expose HTTP/HTTPS services through the Gateway with optional automatic TLS certificate issuance.

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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 

    try:
        api_instance.kubernetes_clusters_httproutes_retrieve(cluster_id)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_httproutes_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_httproutes_retrieve2**
> kubernetes_clusters_httproutes_retrieve2(cluster_id, id)

ViewSet for managing HTTPRoute resources.

HTTPRoutes expose HTTP/HTTPS services through the Gateway with optional automatic TLS certificate issuance.

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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 

    try:
        api_instance.kubernetes_clusters_httproutes_retrieve2(cluster_id, id)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_httproutes_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_httproutes_update**
> HTTPRoute kubernetes_clusters_httproutes_update(cluster_id, id, http_route)

Update HTTPRoute

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.http_route import HTTPRoute
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 
    http_route = pidginhost_sdk.HTTPRoute() # HTTPRoute | 

    try:
        api_response = api_instance.kubernetes_clusters_httproutes_update(cluster_id, id, http_route)
        print("The response of KubernetesApi->kubernetes_clusters_httproutes_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_httproutes_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 
 **http_route** | [**HTTPRoute**](HTTPRoute.md)|  | 

### Return type

[**HTTPRoute**](HTTPRoute.md)

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

# **kubernetes_clusters_kube_version_upgrade_create**
> KubeUpgradeResponse kubernetes_clusters_kube_version_upgrade_create(id)

Upgrade kubernetes to the next available version.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.kube_upgrade_response import KubeUpgradeResponse
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.kubernetes_clusters_kube_version_upgrade_create(id)
        print("The response of KubernetesApi->kubernetes_clusters_kube_version_upgrade_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_kube_version_upgrade_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**KubeUpgradeResponse**](KubeUpgradeResponse.md)

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

# **kubernetes_clusters_kubeconfig_create**
> str kubernetes_clusters_kubeconfig_create(id)

Download kubeconfig file. Use POST to generate a new kubeconfig.

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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.kubernetes_clusters_kubeconfig_create(id)
        print("The response of KubernetesApi->kubernetes_clusters_kubeconfig_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_kubeconfig_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**str**

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_kubeconfig_retrieve**
> str kubernetes_clusters_kubeconfig_retrieve(id)

Download kubeconfig file. Use POST to generate a new kubeconfig.

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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.kubernetes_clusters_kubeconfig_retrieve(id)
        print("The response of KubernetesApi->kubernetes_clusters_kubeconfig_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_kubeconfig_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**str**

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_lb_firewall_create**
> LBFirewallRule kubernetes_clusters_lb_firewall_create(cluster_id, lb_firewall_rule=lb_firewall_rule)

Require complete user profile for provisioning (create) API actions.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.lb_firewall_rule import LBFirewallRule
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    lb_firewall_rule = pidginhost_sdk.LBFirewallRule() # LBFirewallRule |  (optional)

    try:
        api_response = api_instance.kubernetes_clusters_lb_firewall_create(cluster_id, lb_firewall_rule=lb_firewall_rule)
        print("The response of KubernetesApi->kubernetes_clusters_lb_firewall_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_lb_firewall_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **lb_firewall_rule** | [**LBFirewallRule**](LBFirewallRule.md)|  | [optional] 

### Return type

[**LBFirewallRule**](LBFirewallRule.md)

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

# **kubernetes_clusters_lb_firewall_destroy**
> kubernetes_clusters_lb_firewall_destroy(cluster_id, id)

Require complete user profile for provisioning (create) API actions.

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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 

    try:
        api_instance.kubernetes_clusters_lb_firewall_destroy(cluster_id, id)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_lb_firewall_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_lb_firewall_list**
> PaginatedLBFirewallRuleList kubernetes_clusters_lb_firewall_list(cluster_id, page=page)

Require complete user profile for provisioning (create) API actions.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.paginated_lb_firewall_rule_list import PaginatedLBFirewallRuleList
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.kubernetes_clusters_lb_firewall_list(cluster_id, page=page)
        print("The response of KubernetesApi->kubernetes_clusters_lb_firewall_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_lb_firewall_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedLBFirewallRuleList**](PaginatedLBFirewallRuleList.md)

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

# **kubernetes_clusters_lb_firewall_partial_update**
> LBFirewallRule kubernetes_clusters_lb_firewall_partial_update(cluster_id, id, patched_lb_firewall_rule=patched_lb_firewall_rule)

Require complete user profile for provisioning (create) API actions.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.lb_firewall_rule import LBFirewallRule
from pidginhost_sdk.models.patched_lb_firewall_rule import PatchedLBFirewallRule
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 
    patched_lb_firewall_rule = pidginhost_sdk.PatchedLBFirewallRule() # PatchedLBFirewallRule |  (optional)

    try:
        api_response = api_instance.kubernetes_clusters_lb_firewall_partial_update(cluster_id, id, patched_lb_firewall_rule=patched_lb_firewall_rule)
        print("The response of KubernetesApi->kubernetes_clusters_lb_firewall_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_lb_firewall_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 
 **patched_lb_firewall_rule** | [**PatchedLBFirewallRule**](PatchedLBFirewallRule.md)|  | [optional] 

### Return type

[**LBFirewallRule**](LBFirewallRule.md)

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

# **kubernetes_clusters_lb_firewall_retrieve**
> LBFirewallRule kubernetes_clusters_lb_firewall_retrieve(cluster_id, id)

Require complete user profile for provisioning (create) API actions.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.lb_firewall_rule import LBFirewallRule
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 

    try:
        api_response = api_instance.kubernetes_clusters_lb_firewall_retrieve(cluster_id, id)
        print("The response of KubernetesApi->kubernetes_clusters_lb_firewall_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_lb_firewall_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 

### Return type

[**LBFirewallRule**](LBFirewallRule.md)

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

# **kubernetes_clusters_lb_firewall_update**
> LBFirewallRule kubernetes_clusters_lb_firewall_update(cluster_id, id, lb_firewall_rule=lb_firewall_rule)

Require complete user profile for provisioning (create) API actions.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.lb_firewall_rule import LBFirewallRule
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 
    lb_firewall_rule = pidginhost_sdk.LBFirewallRule() # LBFirewallRule |  (optional)

    try:
        api_response = api_instance.kubernetes_clusters_lb_firewall_update(cluster_id, id, lb_firewall_rule=lb_firewall_rule)
        print("The response of KubernetesApi->kubernetes_clusters_lb_firewall_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_lb_firewall_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 
 **lb_firewall_rule** | [**LBFirewallRule**](LBFirewallRule.md)|  | [optional] 

### Return type

[**LBFirewallRule**](LBFirewallRule.md)

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

# **kubernetes_clusters_list**
> PaginatedClusterDetailList kubernetes_clusters_list(page=page)

Require complete user profile for provisioning (create) API actions.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.paginated_cluster_detail_list import PaginatedClusterDetailList
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.kubernetes_clusters_list(page=page)
        print("The response of KubernetesApi->kubernetes_clusters_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedClusterDetailList**](PaginatedClusterDetailList.md)

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

# **kubernetes_clusters_partial_update**
> ClusterDetail kubernetes_clusters_partial_update(id, patched_cluster_detail=patched_cluster_detail)

Require complete user profile for provisioning (create) API actions.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.cluster_detail import ClusterDetail
from pidginhost_sdk.models.patched_cluster_detail import PatchedClusterDetail
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    id = 'id_example' # str | 
    patched_cluster_detail = pidginhost_sdk.PatchedClusterDetail() # PatchedClusterDetail |  (optional)

    try:
        api_response = api_instance.kubernetes_clusters_partial_update(id, patched_cluster_detail=patched_cluster_detail)
        print("The response of KubernetesApi->kubernetes_clusters_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **patched_cluster_detail** | [**PatchedClusterDetail**](PatchedClusterDetail.md)|  | [optional] 

### Return type

[**ClusterDetail**](ClusterDetail.md)

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

# **kubernetes_clusters_port_forwards_create**
> kubernetes_clusters_port_forwards_create(cluster_id)

Require complete user profile for provisioning (create) API actions.

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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 

    try:
        api_instance.kubernetes_clusters_port_forwards_create(cluster_id)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_port_forwards_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_port_forwards_destroy**
> kubernetes_clusters_port_forwards_destroy(cluster_id, id)

Require complete user profile for provisioning (create) API actions.

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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 

    try:
        api_instance.kubernetes_clusters_port_forwards_destroy(cluster_id, id)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_port_forwards_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_port_forwards_partial_update**
> kubernetes_clusters_port_forwards_partial_update(cluster_id, id)

Require complete user profile for provisioning (create) API actions.

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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 

    try:
        api_instance.kubernetes_clusters_port_forwards_partial_update(cluster_id, id)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_port_forwards_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_port_forwards_retrieve**
> kubernetes_clusters_port_forwards_retrieve(cluster_id)

Require complete user profile for provisioning (create) API actions.

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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 

    try:
        api_instance.kubernetes_clusters_port_forwards_retrieve(cluster_id)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_port_forwards_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_port_forwards_retrieve2**
> kubernetes_clusters_port_forwards_retrieve2(cluster_id, id)

Require complete user profile for provisioning (create) API actions.

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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 

    try:
        api_instance.kubernetes_clusters_port_forwards_retrieve2(cluster_id, id)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_port_forwards_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_port_forwards_update**
> kubernetes_clusters_port_forwards_update(cluster_id, id)

Require complete user profile for provisioning (create) API actions.

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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 

    try:
        api_instance.kubernetes_clusters_port_forwards_update(cluster_id, id)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_port_forwards_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_resource_pools_create**
> ResourcePoolAddResponse kubernetes_clusters_resource_pools_create(cluster_id, resource_pool_add)

Create new resource pool

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.resource_pool_add import ResourcePoolAdd
from pidginhost_sdk.models.resource_pool_add_response import ResourcePoolAddResponse
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    resource_pool_add = pidginhost_sdk.ResourcePoolAdd() # ResourcePoolAdd | 

    try:
        api_response = api_instance.kubernetes_clusters_resource_pools_create(cluster_id, resource_pool_add)
        print("The response of KubernetesApi->kubernetes_clusters_resource_pools_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_resource_pools_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **resource_pool_add** | [**ResourcePoolAdd**](ResourcePoolAdd.md)|  | 

### Return type

[**ResourcePoolAddResponse**](ResourcePoolAddResponse.md)

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

# **kubernetes_clusters_resource_pools_destroy**
> kubernetes_clusters_resource_pools_destroy(cluster_id, id)

Require complete user profile for provisioning (create) API actions.

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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 

    try:
        api_instance.kubernetes_clusters_resource_pools_destroy(cluster_id, id)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_resource_pools_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_resource_pools_list**
> PaginatedResourcePoolList kubernetes_clusters_resource_pools_list(cluster_id, page=page)

Require complete user profile for provisioning (create) API actions.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.paginated_resource_pool_list import PaginatedResourcePoolList
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.kubernetes_clusters_resource_pools_list(cluster_id, page=page)
        print("The response of KubernetesApi->kubernetes_clusters_resource_pools_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_resource_pools_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedResourcePoolList**](PaginatedResourcePoolList.md)

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

# **kubernetes_clusters_resource_pools_nodes_destroy**
> kubernetes_clusters_resource_pools_nodes_destroy(cluster_id, id, pool_id)

Require complete user profile for provisioning (create) API actions.

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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 
    pool_id = 56 # int | 

    try:
        api_instance.kubernetes_clusters_resource_pools_nodes_destroy(cluster_id, id, pool_id)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_resource_pools_nodes_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 
 **pool_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_resource_pools_nodes_list**
> PaginatedResourcePoolNodeList kubernetes_clusters_resource_pools_nodes_list(cluster_id, pool_id, page=page)

Require complete user profile for provisioning (create) API actions.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.paginated_resource_pool_node_list import PaginatedResourcePoolNodeList
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    pool_id = 56 # int | 
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.kubernetes_clusters_resource_pools_nodes_list(cluster_id, pool_id, page=page)
        print("The response of KubernetesApi->kubernetes_clusters_resource_pools_nodes_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_resource_pools_nodes_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **pool_id** | **int**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedResourcePoolNodeList**](PaginatedResourcePoolNodeList.md)

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

# **kubernetes_clusters_resource_pools_nodes_metrics_retrieve**
> NodeMetricsResponse kubernetes_clusters_resource_pools_nodes_metrics_retrieve(cluster_id, id, pool_id)

Get real-time metrics for a node VM.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.node_metrics_response import NodeMetricsResponse
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 
    pool_id = 56 # int | 

    try:
        api_response = api_instance.kubernetes_clusters_resource_pools_nodes_metrics_retrieve(cluster_id, id, pool_id)
        print("The response of KubernetesApi->kubernetes_clusters_resource_pools_nodes_metrics_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_resource_pools_nodes_metrics_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 
 **pool_id** | **int**|  | 

### Return type

[**NodeMetricsResponse**](NodeMetricsResponse.md)

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

# **kubernetes_clusters_resource_pools_nodes_retrieve**
> ResourcePoolNode kubernetes_clusters_resource_pools_nodes_retrieve(cluster_id, id, pool_id)

Require complete user profile for provisioning (create) API actions.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.resource_pool_node import ResourcePoolNode
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 
    pool_id = 56 # int | 

    try:
        api_response = api_instance.kubernetes_clusters_resource_pools_nodes_retrieve(cluster_id, id, pool_id)
        print("The response of KubernetesApi->kubernetes_clusters_resource_pools_nodes_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_resource_pools_nodes_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 
 **pool_id** | **int**|  | 

### Return type

[**ResourcePoolNode**](ResourcePoolNode.md)

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

# **kubernetes_clusters_resource_pools_nodes_rrd_retrieve**
> NodeRRDResponse kubernetes_clusters_resource_pools_nodes_rrd_retrieve(cluster_id, id, pool_id)

Get RRD (historical) metrics data for a node VM.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.node_rrd_response import NodeRRDResponse
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 
    pool_id = 56 # int | 

    try:
        api_response = api_instance.kubernetes_clusters_resource_pools_nodes_rrd_retrieve(cluster_id, id, pool_id)
        print("The response of KubernetesApi->kubernetes_clusters_resource_pools_nodes_rrd_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_resource_pools_nodes_rrd_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 
 **pool_id** | **int**|  | 

### Return type

[**NodeRRDResponse**](NodeRRDResponse.md)

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

# **kubernetes_clusters_resource_pools_partial_update**
> ResourcePool kubernetes_clusters_resource_pools_partial_update(cluster_id, id, patched_resource_pool=patched_resource_pool)

Require complete user profile for provisioning (create) API actions.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.patched_resource_pool import PatchedResourcePool
from pidginhost_sdk.models.resource_pool import ResourcePool
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 
    patched_resource_pool = pidginhost_sdk.PatchedResourcePool() # PatchedResourcePool |  (optional)

    try:
        api_response = api_instance.kubernetes_clusters_resource_pools_partial_update(cluster_id, id, patched_resource_pool=patched_resource_pool)
        print("The response of KubernetesApi->kubernetes_clusters_resource_pools_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_resource_pools_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 
 **patched_resource_pool** | [**PatchedResourcePool**](PatchedResourcePool.md)|  | [optional] 

### Return type

[**ResourcePool**](ResourcePool.md)

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

# **kubernetes_clusters_resource_pools_retrieve**
> ResourcePool kubernetes_clusters_resource_pools_retrieve(cluster_id, id)

Require complete user profile for provisioning (create) API actions.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.resource_pool import ResourcePool
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 

    try:
        api_response = api_instance.kubernetes_clusters_resource_pools_retrieve(cluster_id, id)
        print("The response of KubernetesApi->kubernetes_clusters_resource_pools_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_resource_pools_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 

### Return type

[**ResourcePool**](ResourcePool.md)

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

# **kubernetes_clusters_resource_pools_update**
> ResourcePool kubernetes_clusters_resource_pools_update(cluster_id, id, resource_pool=resource_pool)

Require complete user profile for provisioning (create) API actions.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.resource_pool import ResourcePool
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 
    resource_pool = pidginhost_sdk.ResourcePool() # ResourcePool |  (optional)

    try:
        api_response = api_instance.kubernetes_clusters_resource_pools_update(cluster_id, id, resource_pool=resource_pool)
        print("The response of KubernetesApi->kubernetes_clusters_resource_pools_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_resource_pools_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 
 **resource_pool** | [**ResourcePool**](ResourcePool.md)|  | [optional] 

### Return type

[**ResourcePool**](ResourcePool.md)

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

# **kubernetes_clusters_retrieve**
> ClusterDetail kubernetes_clusters_retrieve(id)

Require complete user profile for provisioning (create) API actions.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.cluster_detail import ClusterDetail
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.kubernetes_clusters_retrieve(id)
        print("The response of KubernetesApi->kubernetes_clusters_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ClusterDetail**](ClusterDetail.md)

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

# **kubernetes_clusters_talos_version_upgrade_create**
> TalosUpgradeResponse kubernetes_clusters_talos_version_upgrade_create(id)

Upgrade Talos to the next available version.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.talos_upgrade_response import TalosUpgradeResponse
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.kubernetes_clusters_talos_version_upgrade_create(id)
        print("The response of KubernetesApi->kubernetes_clusters_talos_version_upgrade_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_talos_version_upgrade_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**TalosUpgradeResponse**](TalosUpgradeResponse.md)

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

# **kubernetes_clusters_tcproutes_create**
> TCPRoute kubernetes_clusters_tcproutes_create(cluster_id, tcp_route)

Create new TCPRoute

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.tcp_route import TCPRoute
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    tcp_route = pidginhost_sdk.TCPRoute() # TCPRoute | 

    try:
        api_response = api_instance.kubernetes_clusters_tcproutes_create(cluster_id, tcp_route)
        print("The response of KubernetesApi->kubernetes_clusters_tcproutes_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_tcproutes_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **tcp_route** | [**TCPRoute**](TCPRoute.md)|  | 

### Return type

[**TCPRoute**](TCPRoute.md)

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

# **kubernetes_clusters_tcproutes_destroy**
> kubernetes_clusters_tcproutes_destroy(cluster_id, id)

ViewSet for managing TCPRoute resources.

TCPRoutes expose TCP services through the Gateway on specific external ports.
Reserved ports (22, 6443, 50000, 50001) cannot be exposed.

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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 

    try:
        api_instance.kubernetes_clusters_tcproutes_destroy(cluster_id, id)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_tcproutes_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_tcproutes_partial_update**
> TCPRoute kubernetes_clusters_tcproutes_partial_update(cluster_id, id, patched_tcp_route=patched_tcp_route)

Partially update TCPRoute

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.patched_tcp_route import PatchedTCPRoute
from pidginhost_sdk.models.tcp_route import TCPRoute
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 
    patched_tcp_route = pidginhost_sdk.PatchedTCPRoute() # PatchedTCPRoute |  (optional)

    try:
        api_response = api_instance.kubernetes_clusters_tcproutes_partial_update(cluster_id, id, patched_tcp_route=patched_tcp_route)
        print("The response of KubernetesApi->kubernetes_clusters_tcproutes_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_tcproutes_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 
 **patched_tcp_route** | [**PatchedTCPRoute**](PatchedTCPRoute.md)|  | [optional] 

### Return type

[**TCPRoute**](TCPRoute.md)

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

# **kubernetes_clusters_tcproutes_retrieve**
> kubernetes_clusters_tcproutes_retrieve(cluster_id)

ViewSet for managing TCPRoute resources.

TCPRoutes expose TCP services through the Gateway on specific external ports.
Reserved ports (22, 6443, 50000, 50001) cannot be exposed.

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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 

    try:
        api_instance.kubernetes_clusters_tcproutes_retrieve(cluster_id)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_tcproutes_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_tcproutes_retrieve2**
> kubernetes_clusters_tcproutes_retrieve2(cluster_id, id)

ViewSet for managing TCPRoute resources.

TCPRoutes expose TCP services through the Gateway on specific external ports.
Reserved ports (22, 6443, 50000, 50001) cannot be exposed.

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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 

    try:
        api_instance.kubernetes_clusters_tcproutes_retrieve2(cluster_id, id)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_tcproutes_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_tcproutes_update**
> TCPRoute kubernetes_clusters_tcproutes_update(cluster_id, id, tcp_route)

Update TCPRoute

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.tcp_route import TCPRoute
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 
    tcp_route = pidginhost_sdk.TCPRoute() # TCPRoute | 

    try:
        api_response = api_instance.kubernetes_clusters_tcproutes_update(cluster_id, id, tcp_route)
        print("The response of KubernetesApi->kubernetes_clusters_tcproutes_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_tcproutes_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 
 **tcp_route** | [**TCPRoute**](TCPRoute.md)|  | 

### Return type

[**TCPRoute**](TCPRoute.md)

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

# **kubernetes_clusters_toggle_cloud_vm_access_create**
> ToggleCloudVMAccessResponse kubernetes_clusters_toggle_cloud_vm_access_create(id)

Toggle cloud VM access for this cluster.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.toggle_cloud_vm_access_response import ToggleCloudVMAccessResponse
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.kubernetes_clusters_toggle_cloud_vm_access_create(id)
        print("The response of KubernetesApi->kubernetes_clusters_toggle_cloud_vm_access_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_toggle_cloud_vm_access_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ToggleCloudVMAccessResponse**](ToggleCloudVMAccessResponse.md)

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

# **kubernetes_clusters_udproutes_create**
> UDPRoute kubernetes_clusters_udproutes_create(cluster_id, udp_route)

Create new UDPRoute

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.udp_route import UDPRoute
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    udp_route = pidginhost_sdk.UDPRoute() # UDPRoute | 

    try:
        api_response = api_instance.kubernetes_clusters_udproutes_create(cluster_id, udp_route)
        print("The response of KubernetesApi->kubernetes_clusters_udproutes_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_udproutes_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **udp_route** | [**UDPRoute**](UDPRoute.md)|  | 

### Return type

[**UDPRoute**](UDPRoute.md)

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

# **kubernetes_clusters_udproutes_destroy**
> kubernetes_clusters_udproutes_destroy(cluster_id, id)

ViewSet for managing UDPRoute resources.

UDPRoutes expose UDP services through the Gateway on specific external ports.

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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 

    try:
        api_instance.kubernetes_clusters_udproutes_destroy(cluster_id, id)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_udproutes_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_udproutes_partial_update**
> UDPRoute kubernetes_clusters_udproutes_partial_update(cluster_id, id, patched_udp_route=patched_udp_route)

Partially update UDPRoute

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.patched_udp_route import PatchedUDPRoute
from pidginhost_sdk.models.udp_route import UDPRoute
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 
    patched_udp_route = pidginhost_sdk.PatchedUDPRoute() # PatchedUDPRoute |  (optional)

    try:
        api_response = api_instance.kubernetes_clusters_udproutes_partial_update(cluster_id, id, patched_udp_route=patched_udp_route)
        print("The response of KubernetesApi->kubernetes_clusters_udproutes_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_udproutes_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 
 **patched_udp_route** | [**PatchedUDPRoute**](PatchedUDPRoute.md)|  | [optional] 

### Return type

[**UDPRoute**](UDPRoute.md)

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

# **kubernetes_clusters_udproutes_retrieve**
> kubernetes_clusters_udproutes_retrieve(cluster_id)

ViewSet for managing UDPRoute resources.

UDPRoutes expose UDP services through the Gateway on specific external ports.

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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 

    try:
        api_instance.kubernetes_clusters_udproutes_retrieve(cluster_id)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_udproutes_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_udproutes_retrieve2**
> kubernetes_clusters_udproutes_retrieve2(cluster_id, id)

ViewSet for managing UDPRoute resources.

UDPRoutes expose UDP services through the Gateway on specific external ports.

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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 

    try:
        api_instance.kubernetes_clusters_udproutes_retrieve2(cluster_id, id)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_udproutes_retrieve2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[cookieAuth](../README.md#cookieAuth), [tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_udproutes_update**
> UDPRoute kubernetes_clusters_udproutes_update(cluster_id, id, udp_route)

Update UDPRoute

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.udp_route import UDPRoute
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 
    udp_route = pidginhost_sdk.UDPRoute() # UDPRoute | 

    try:
        api_response = api_instance.kubernetes_clusters_udproutes_update(cluster_id, id, udp_route)
        print("The response of KubernetesApi->kubernetes_clusters_udproutes_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_udproutes_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 
 **udp_route** | [**UDPRoute**](UDPRoute.md)|  | 

### Return type

[**UDPRoute**](UDPRoute.md)

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

# **kubernetes_clusters_update**
> ClusterDetail kubernetes_clusters_update(id, cluster_detail)

Require complete user profile for provisioning (create) API actions.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.cluster_detail import ClusterDetail
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    id = 'id_example' # str | 
    cluster_detail = pidginhost_sdk.ClusterDetail() # ClusterDetail | 

    try:
        api_response = api_instance.kubernetes_clusters_update(id, cluster_detail)
        print("The response of KubernetesApi->kubernetes_clusters_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **cluster_detail** | [**ClusterDetail**](ClusterDetail.md)|  | 

### Return type

[**ClusterDetail**](ClusterDetail.md)

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

# **kubernetes_clusters_upgrade_feature_create**
> FeatureUpgradeResponse kubernetes_clusters_upgrade_feature_create(id, feature_upgrade_request)

Upgrade a cluster feature to the latest compatible version.

### Example

* Api Key Authentication (cookieAuth):
* Api Key Authentication (tokenAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.feature_upgrade_request import FeatureUpgradeRequest
from pidginhost_sdk.models.feature_upgrade_response import FeatureUpgradeResponse
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    id = 'id_example' # str | 
    feature_upgrade_request = pidginhost_sdk.FeatureUpgradeRequest() # FeatureUpgradeRequest | 

    try:
        api_response = api_instance.kubernetes_clusters_upgrade_feature_create(id, feature_upgrade_request)
        print("The response of KubernetesApi->kubernetes_clusters_upgrade_feature_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_upgrade_feature_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **feature_upgrade_request** | [**FeatureUpgradeRequest**](FeatureUpgradeRequest.md)|  | 

### Return type

[**FeatureUpgradeResponse**](FeatureUpgradeResponse.md)

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

