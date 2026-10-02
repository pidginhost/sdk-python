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
[**kubernetes_clusters_encryption_create**](KubernetesApi.md#kubernetes_clusters_encryption_create) | **POST** /api/kubernetes/clusters/{id}/encryption/ | 
[**kubernetes_clusters_encryption_recheck_create**](KubernetesApi.md#kubernetes_clusters_encryption_recheck_create) | **POST** /api/kubernetes/clusters/{id}/encryption/recheck/ | 
[**kubernetes_clusters_encryption_reconcile_create**](KubernetesApi.md#kubernetes_clusters_encryption_reconcile_create) | **POST** /api/kubernetes/clusters/{id}/encryption/reconcile/ | 
[**kubernetes_clusters_encryption_retrieve**](KubernetesApi.md#kubernetes_clusters_encryption_retrieve) | **GET** /api/kubernetes/clusters/{id}/encryption/ | 
[**kubernetes_clusters_httproutes_create**](KubernetesApi.md#kubernetes_clusters_httproutes_create) | **POST** /api/kubernetes/clusters/{cluster_id}/httproutes/ | 
[**kubernetes_clusters_httproutes_destroy**](KubernetesApi.md#kubernetes_clusters_httproutes_destroy) | **DELETE** /api/kubernetes/clusters/{cluster_id}/httproutes/{id}/ | 
[**kubernetes_clusters_httproutes_list**](KubernetesApi.md#kubernetes_clusters_httproutes_list) | **GET** /api/kubernetes/clusters/{cluster_id}/httproutes/ | 
[**kubernetes_clusters_httproutes_partial_update**](KubernetesApi.md#kubernetes_clusters_httproutes_partial_update) | **PATCH** /api/kubernetes/clusters/{cluster_id}/httproutes/{id}/ | 
[**kubernetes_clusters_httproutes_retrieve**](KubernetesApi.md#kubernetes_clusters_httproutes_retrieve) | **GET** /api/kubernetes/clusters/{cluster_id}/httproutes/{id}/ | 
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
[**kubernetes_clusters_node_operations_cancel_create**](KubernetesApi.md#kubernetes_clusters_node_operations_cancel_create) | **POST** /api/kubernetes/clusters/{cluster_id}/node-operations/{id}/cancel/ | 
[**kubernetes_clusters_node_operations_list**](KubernetesApi.md#kubernetes_clusters_node_operations_list) | **GET** /api/kubernetes/clusters/{cluster_id}/node-operations/ | 
[**kubernetes_clusters_node_operations_resume_create**](KubernetesApi.md#kubernetes_clusters_node_operations_resume_create) | **POST** /api/kubernetes/clusters/{cluster_id}/node-operations/{id}/resume/ | 
[**kubernetes_clusters_node_operations_retrieve**](KubernetesApi.md#kubernetes_clusters_node_operations_retrieve) | **GET** /api/kubernetes/clusters/{cluster_id}/node-operations/{id}/ | 
[**kubernetes_clusters_node_operations_retry_create**](KubernetesApi.md#kubernetes_clusters_node_operations_retry_create) | **POST** /api/kubernetes/clusters/{cluster_id}/node-operations/{id}/retry/ | 
[**kubernetes_clusters_partial_update**](KubernetesApi.md#kubernetes_clusters_partial_update) | **PATCH** /api/kubernetes/clusters/{id}/ | 
[**kubernetes_clusters_pool_removal_journals_list**](KubernetesApi.md#kubernetes_clusters_pool_removal_journals_list) | **GET** /api/kubernetes/clusters/{cluster_id}/pool-removal-journals/ | 
[**kubernetes_clusters_pool_removal_journals_resume_create**](KubernetesApi.md#kubernetes_clusters_pool_removal_journals_resume_create) | **POST** /api/kubernetes/clusters/{cluster_id}/pool-removal-journals/{id}/resume/ | 
[**kubernetes_clusters_pool_removal_journals_retrieve**](KubernetesApi.md#kubernetes_clusters_pool_removal_journals_retrieve) | **GET** /api/kubernetes/clusters/{cluster_id}/pool-removal-journals/{id}/ | 
[**kubernetes_clusters_port_forwards_create**](KubernetesApi.md#kubernetes_clusters_port_forwards_create) | **POST** /api/kubernetes/clusters/{cluster_id}/port-forwards/ | 
[**kubernetes_clusters_port_forwards_destroy**](KubernetesApi.md#kubernetes_clusters_port_forwards_destroy) | **DELETE** /api/kubernetes/clusters/{cluster_id}/port-forwards/{id}/ | 
[**kubernetes_clusters_port_forwards_list**](KubernetesApi.md#kubernetes_clusters_port_forwards_list) | **GET** /api/kubernetes/clusters/{cluster_id}/port-forwards/ | 
[**kubernetes_clusters_port_forwards_partial_update**](KubernetesApi.md#kubernetes_clusters_port_forwards_partial_update) | **PATCH** /api/kubernetes/clusters/{cluster_id}/port-forwards/{id}/ | 
[**kubernetes_clusters_port_forwards_retrieve**](KubernetesApi.md#kubernetes_clusters_port_forwards_retrieve) | **GET** /api/kubernetes/clusters/{cluster_id}/port-forwards/{id}/ | 
[**kubernetes_clusters_port_forwards_update**](KubernetesApi.md#kubernetes_clusters_port_forwards_update) | **PUT** /api/kubernetes/clusters/{cluster_id}/port-forwards/{id}/ | 
[**kubernetes_clusters_resource_pools_create**](KubernetesApi.md#kubernetes_clusters_resource_pools_create) | **POST** /api/kubernetes/clusters/{cluster_id}/resource-pools/ | 
[**kubernetes_clusters_resource_pools_destroy**](KubernetesApi.md#kubernetes_clusters_resource_pools_destroy) | **DELETE** /api/kubernetes/clusters/{cluster_id}/resource-pools/{id}/ | 
[**kubernetes_clusters_resource_pools_list**](KubernetesApi.md#kubernetes_clusters_resource_pools_list) | **GET** /api/kubernetes/clusters/{cluster_id}/resource-pools/ | 
[**kubernetes_clusters_resource_pools_nodes_destroy**](KubernetesApi.md#kubernetes_clusters_resource_pools_nodes_destroy) | **DELETE** /api/kubernetes/clusters/{cluster_id}/resource-pools/{pool_id}/nodes/{id}/ | 
[**kubernetes_clusters_resource_pools_nodes_list**](KubernetesApi.md#kubernetes_clusters_resource_pools_nodes_list) | **GET** /api/kubernetes/clusters/{cluster_id}/resource-pools/{pool_id}/nodes/ | 
[**kubernetes_clusters_resource_pools_nodes_metrics_retrieve**](KubernetesApi.md#kubernetes_clusters_resource_pools_nodes_metrics_retrieve) | **GET** /api/kubernetes/clusters/{cluster_id}/resource-pools/{pool_id}/nodes/{id}/metrics/ | 
[**kubernetes_clusters_resource_pools_nodes_reboot_create**](KubernetesApi.md#kubernetes_clusters_resource_pools_nodes_reboot_create) | **POST** /api/kubernetes/clusters/{cluster_id}/resource-pools/{pool_id}/nodes/{id}/reboot/ | 
[**kubernetes_clusters_resource_pools_nodes_retrieve**](KubernetesApi.md#kubernetes_clusters_resource_pools_nodes_retrieve) | **GET** /api/kubernetes/clusters/{cluster_id}/resource-pools/{pool_id}/nodes/{id}/ | 
[**kubernetes_clusters_resource_pools_nodes_rrd_retrieve**](KubernetesApi.md#kubernetes_clusters_resource_pools_nodes_rrd_retrieve) | **GET** /api/kubernetes/clusters/{cluster_id}/resource-pools/{pool_id}/nodes/{id}/rrd/ | 
[**kubernetes_clusters_resource_pools_partial_update**](KubernetesApi.md#kubernetes_clusters_resource_pools_partial_update) | **PATCH** /api/kubernetes/clusters/{cluster_id}/resource-pools/{id}/ | 
[**kubernetes_clusters_resource_pools_retrieve**](KubernetesApi.md#kubernetes_clusters_resource_pools_retrieve) | **GET** /api/kubernetes/clusters/{cluster_id}/resource-pools/{id}/ | 
[**kubernetes_clusters_resource_pools_update**](KubernetesApi.md#kubernetes_clusters_resource_pools_update) | **PUT** /api/kubernetes/clusters/{cluster_id}/resource-pools/{id}/ | 
[**kubernetes_clusters_retrieve**](KubernetesApi.md#kubernetes_clusters_retrieve) | **GET** /api/kubernetes/clusters/{id}/ | 
[**kubernetes_clusters_talos_version_upgrade_create**](KubernetesApi.md#kubernetes_clusters_talos_version_upgrade_create) | **POST** /api/kubernetes/clusters/{id}/talos-version-upgrade/ | 
[**kubernetes_clusters_tcproutes_create**](KubernetesApi.md#kubernetes_clusters_tcproutes_create) | **POST** /api/kubernetes/clusters/{cluster_id}/tcproutes/ | 
[**kubernetes_clusters_tcproutes_destroy**](KubernetesApi.md#kubernetes_clusters_tcproutes_destroy) | **DELETE** /api/kubernetes/clusters/{cluster_id}/tcproutes/{id}/ | 
[**kubernetes_clusters_tcproutes_list**](KubernetesApi.md#kubernetes_clusters_tcproutes_list) | **GET** /api/kubernetes/clusters/{cluster_id}/tcproutes/ | 
[**kubernetes_clusters_tcproutes_partial_update**](KubernetesApi.md#kubernetes_clusters_tcproutes_partial_update) | **PATCH** /api/kubernetes/clusters/{cluster_id}/tcproutes/{id}/ | 
[**kubernetes_clusters_tcproutes_retrieve**](KubernetesApi.md#kubernetes_clusters_tcproutes_retrieve) | **GET** /api/kubernetes/clusters/{cluster_id}/tcproutes/{id}/ | 
[**kubernetes_clusters_tcproutes_update**](KubernetesApi.md#kubernetes_clusters_tcproutes_update) | **PUT** /api/kubernetes/clusters/{cluster_id}/tcproutes/{id}/ | 
[**kubernetes_clusters_toggle_cloud_vm_access_create**](KubernetesApi.md#kubernetes_clusters_toggle_cloud_vm_access_create) | **POST** /api/kubernetes/clusters/{id}/toggle-cloud-vm-access/ | 
[**kubernetes_clusters_udproutes_create**](KubernetesApi.md#kubernetes_clusters_udproutes_create) | **POST** /api/kubernetes/clusters/{cluster_id}/udproutes/ | 
[**kubernetes_clusters_udproutes_destroy**](KubernetesApi.md#kubernetes_clusters_udproutes_destroy) | **DELETE** /api/kubernetes/clusters/{cluster_id}/udproutes/{id}/ | 
[**kubernetes_clusters_udproutes_list**](KubernetesApi.md#kubernetes_clusters_udproutes_list) | **GET** /api/kubernetes/clusters/{cluster_id}/udproutes/ | 
[**kubernetes_clusters_udproutes_partial_update**](KubernetesApi.md#kubernetes_clusters_udproutes_partial_update) | **PATCH** /api/kubernetes/clusters/{cluster_id}/udproutes/{id}/ | 
[**kubernetes_clusters_udproutes_retrieve**](KubernetesApi.md#kubernetes_clusters_udproutes_retrieve) | **GET** /api/kubernetes/clusters/{cluster_id}/udproutes/{id}/ | 
[**kubernetes_clusters_udproutes_update**](KubernetesApi.md#kubernetes_clusters_udproutes_update) | **PUT** /api/kubernetes/clusters/{cluster_id}/udproutes/{id}/ | 
[**kubernetes_clusters_update**](KubernetesApi.md#kubernetes_clusters_update) | **PUT** /api/kubernetes/clusters/{id}/ | 
[**kubernetes_clusters_upgrade_feature_create**](KubernetesApi.md#kubernetes_clusters_upgrade_feature_create) | **POST** /api/kubernetes/clusters/{id}/upgrade-feature/ | 
[**kubernetes_clusters_upgrade_lb_create**](KubernetesApi.md#kubernetes_clusters_upgrade_lb_create) | **POST** /api/kubernetes/clusters/{id}/upgrade-lb/ | 


# **kubernetes_cluster_types_list**
> PaginatedClusterTypeList kubernetes_cluster_types_list(page=page)

Adds :class:`~account.iam_enforcement.IAMActionPermission` as an
intersection with the route's existing permission classes (spec §6).

Detail routes (``self.detail``) defer the role/scope check to
``has_object_permission`` so the account-scoped ``get_object`` answers 404
for foreign IDs before any role denial; every other route enforces in
``has_permission``. A detail action that never calls ``get_object`` would
skip enforcement — the route probes pin the denial for each route.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

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

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

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

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

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

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

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

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

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

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_create**
> ClusterAddResponse kubernetes_clusters_create(cluster_add_request)

Create new k8s cluster

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.cluster_add_request import ClusterAddRequest
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_add_request = pidginhost_sdk.ClusterAddRequest() # ClusterAddRequest | 

    try:
        api_response = api_instance.kubernetes_clusters_create(cluster_add_request)
        print("The response of KubernetesApi->kubernetes_clusters_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_add_request** | [**ClusterAddRequest**](ClusterAddRequest.md)|  | 

### Return type

[**ClusterAddResponse**](ClusterAddResponse.md)

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

# **kubernetes_clusters_destroy**
> kubernetes_clusters_destroy(id)

Adds :class:`~account.iam_enforcement.IAMActionPermission` as an
intersection with the route's existing permission classes (spec §6).

Detail routes (``self.detail``) defer the role/scope check to
``has_object_permission`` so the account-scoped ``get_object`` answers 404
for foreign IDs before any role denial; every other route enforces in
``has_permission``. A detail action that never calls ``get_object`` would
skip enforcement — the route probes pin the denial for each route.

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

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

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

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

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

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

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

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

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

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_encryption_create**
> ClusterEncryptionOperation kubernetes_clusters_encryption_create(id, cluster_encryption_request)

Enable or disable WireGuard encryption for cluster traffic.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.cluster_encryption_operation import ClusterEncryptionOperation
from pidginhost_sdk.models.cluster_encryption_request import ClusterEncryptionRequest
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    id = 'id_example' # str | 
    cluster_encryption_request = pidginhost_sdk.ClusterEncryptionRequest() # ClusterEncryptionRequest | 

    try:
        api_response = api_instance.kubernetes_clusters_encryption_create(id, cluster_encryption_request)
        print("The response of KubernetesApi->kubernetes_clusters_encryption_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_encryption_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **cluster_encryption_request** | [**ClusterEncryptionRequest**](ClusterEncryptionRequest.md)|  | 

### Return type

[**ClusterEncryptionOperation**](ClusterEncryptionOperation.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  * Location - The cluster&#39;s encryption status resource, to poll for the outcome. <br>  |
**400** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_encryption_recheck_create**
> ClusterEncryption kubernetes_clusters_encryption_recheck_create(id)

Re-count the workloads that still predate the encryption change.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.cluster_encryption import ClusterEncryption
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.kubernetes_clusters_encryption_recheck_create(id)
        print("The response of KubernetesApi->kubernetes_clusters_encryption_recheck_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_encryption_recheck_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ClusterEncryption**](ClusterEncryption.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**503** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_encryption_reconcile_create**
> ClusterEncryptionOperation kubernetes_clusters_encryption_reconcile_create(id, cluster_encryption_reconcile_request)

Staff only: resolve a cluster whose encryption state is unknown.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.cluster_encryption_operation import ClusterEncryptionOperation
from pidginhost_sdk.models.cluster_encryption_reconcile_request import ClusterEncryptionReconcileRequest
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    id = 'id_example' # str | 
    cluster_encryption_reconcile_request = pidginhost_sdk.ClusterEncryptionReconcileRequest() # ClusterEncryptionReconcileRequest | 

    try:
        api_response = api_instance.kubernetes_clusters_encryption_reconcile_create(id, cluster_encryption_reconcile_request)
        print("The response of KubernetesApi->kubernetes_clusters_encryption_reconcile_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_encryption_reconcile_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **cluster_encryption_reconcile_request** | [**ClusterEncryptionReconcileRequest**](ClusterEncryptionReconcileRequest.md)|  | 

### Return type

[**ClusterEncryptionOperation**](ClusterEncryptionOperation.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  * Location - The cluster&#39;s encryption status resource, to poll for the outcome. <br>  |
**400** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_encryption_retrieve**
> ClusterEncryption kubernetes_clusters_encryption_retrieve(id)

Read the cluster's encryption state, restart gate and per-node verification evidence.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.cluster_encryption import ClusterEncryption
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.kubernetes_clusters_encryption_retrieve(id)
        print("The response of KubernetesApi->kubernetes_clusters_encryption_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_encryption_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ClusterEncryption**](ClusterEncryption.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_httproutes_create**
> HTTPRoute kubernetes_clusters_httproutes_create(cluster_id, http_route_request)

Create new HTTPRoute

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.http_route import HTTPRoute
from pidginhost_sdk.models.http_route_request import HTTPRouteRequest
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    http_route_request = pidginhost_sdk.HTTPRouteRequest() # HTTPRouteRequest | 

    try:
        api_response = api_instance.kubernetes_clusters_httproutes_create(cluster_id, http_route_request)
        print("The response of KubernetesApi->kubernetes_clusters_httproutes_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_httproutes_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **http_route_request** | [**HTTPRouteRequest**](HTTPRouteRequest.md)|  | 

### Return type

[**HTTPRoute**](HTTPRoute.md)

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

# **kubernetes_clusters_httproutes_destroy**
> kubernetes_clusters_httproutes_destroy(cluster_id, id)

ViewSet for managing HTTPRoute resources.

HTTPRoutes expose HTTP/HTTPS services through the Gateway with optional automatic TLS certificate issuance.

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

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_httproutes_list**
> PaginatedHTTPRouteList kubernetes_clusters_httproutes_list(cluster_id, page=page)

ViewSet for managing HTTPRoute resources.

HTTPRoutes expose HTTP/HTTPS services through the Gateway with optional automatic TLS certificate issuance.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.paginated_http_route_list import PaginatedHTTPRouteList
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.kubernetes_clusters_httproutes_list(cluster_id, page=page)
        print("The response of KubernetesApi->kubernetes_clusters_httproutes_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_httproutes_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedHTTPRouteList**](PaginatedHTTPRouteList.md)

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

# **kubernetes_clusters_httproutes_partial_update**
> HTTPRoute kubernetes_clusters_httproutes_partial_update(cluster_id, id, patched_http_route_request=patched_http_route_request)

Partially update HTTPRoute

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.http_route import HTTPRoute
from pidginhost_sdk.models.patched_http_route_request import PatchedHTTPRouteRequest
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 
    patched_http_route_request = pidginhost_sdk.PatchedHTTPRouteRequest() # PatchedHTTPRouteRequest |  (optional)

    try:
        api_response = api_instance.kubernetes_clusters_httproutes_partial_update(cluster_id, id, patched_http_route_request=patched_http_route_request)
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
 **patched_http_route_request** | [**PatchedHTTPRouteRequest**](PatchedHTTPRouteRequest.md)|  | [optional] 

### Return type

[**HTTPRoute**](HTTPRoute.md)

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

# **kubernetes_clusters_httproutes_retrieve**
> HTTPRoute kubernetes_clusters_httproutes_retrieve(cluster_id, id)

ViewSet for managing HTTPRoute resources.

HTTPRoutes expose HTTP/HTTPS services through the Gateway with optional automatic TLS certificate issuance.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 

    try:
        api_response = api_instance.kubernetes_clusters_httproutes_retrieve(cluster_id, id)
        print("The response of KubernetesApi->kubernetes_clusters_httproutes_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_httproutes_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 

### Return type

[**HTTPRoute**](HTTPRoute.md)

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

# **kubernetes_clusters_httproutes_update**
> HTTPRoute kubernetes_clusters_httproutes_update(cluster_id, id, http_route_request)

Update HTTPRoute

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.http_route import HTTPRoute
from pidginhost_sdk.models.http_route_request import HTTPRouteRequest
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 
    http_route_request = pidginhost_sdk.HTTPRouteRequest() # HTTPRouteRequest | 

    try:
        api_response = api_instance.kubernetes_clusters_httproutes_update(cluster_id, id, http_route_request)
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
 **http_route_request** | [**HTTPRouteRequest**](HTTPRouteRequest.md)|  | 

### Return type

[**HTTPRoute**](HTTPRoute.md)

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

# **kubernetes_clusters_kube_version_upgrade_create**
> KubeUpgradeResponse kubernetes_clusters_kube_version_upgrade_create(id)

Upgrade kubernetes to the next available version.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

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

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

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

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

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

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_lb_firewall_create**
> LBFirewallRule kubernetes_clusters_lb_firewall_create(cluster_id, lb_firewall_rule_request=lb_firewall_rule_request)

Adds :class:`~account.iam_enforcement.IAMActionPermission` as an
intersection with the route's existing permission classes (spec §6).

Detail routes (``self.detail``) defer the role/scope check to
``has_object_permission`` so the account-scoped ``get_object`` answers 404
for foreign IDs before any role denial; every other route enforces in
``has_permission``. A detail action that never calls ``get_object`` would
skip enforcement — the route probes pin the denial for each route.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.lb_firewall_rule import LBFirewallRule
from pidginhost_sdk.models.lb_firewall_rule_request import LBFirewallRuleRequest
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    lb_firewall_rule_request = pidginhost_sdk.LBFirewallRuleRequest() # LBFirewallRuleRequest |  (optional)

    try:
        api_response = api_instance.kubernetes_clusters_lb_firewall_create(cluster_id, lb_firewall_rule_request=lb_firewall_rule_request)
        print("The response of KubernetesApi->kubernetes_clusters_lb_firewall_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_lb_firewall_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **lb_firewall_rule_request** | [**LBFirewallRuleRequest**](LBFirewallRuleRequest.md)|  | [optional] 

### Return type

[**LBFirewallRule**](LBFirewallRule.md)

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

# **kubernetes_clusters_lb_firewall_destroy**
> kubernetes_clusters_lb_firewall_destroy(cluster_id, id)

Adds :class:`~account.iam_enforcement.IAMActionPermission` as an
intersection with the route's existing permission classes (spec §6).

Detail routes (``self.detail``) defer the role/scope check to
``has_object_permission`` so the account-scoped ``get_object`` answers 404
for foreign IDs before any role denial; every other route enforces in
``has_permission``. A detail action that never calls ``get_object`` would
skip enforcement — the route probes pin the denial for each route.

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

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

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

Adds :class:`~account.iam_enforcement.IAMActionPermission` as an
intersection with the route's existing permission classes (spec §6).

Detail routes (``self.detail``) defer the role/scope check to
``has_object_permission`` so the account-scoped ``get_object`` answers 404
for foreign IDs before any role denial; every other route enforces in
``has_permission``. A detail action that never calls ``get_object`` would
skip enforcement — the route probes pin the denial for each route.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

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

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_lb_firewall_partial_update**
> LBFirewallRule kubernetes_clusters_lb_firewall_partial_update(cluster_id, id, patched_lb_firewall_rule_request=patched_lb_firewall_rule_request)

Adds :class:`~account.iam_enforcement.IAMActionPermission` as an
intersection with the route's existing permission classes (spec §6).

Detail routes (``self.detail``) defer the role/scope check to
``has_object_permission`` so the account-scoped ``get_object`` answers 404
for foreign IDs before any role denial; every other route enforces in
``has_permission``. A detail action that never calls ``get_object`` would
skip enforcement — the route probes pin the denial for each route.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.lb_firewall_rule import LBFirewallRule
from pidginhost_sdk.models.patched_lb_firewall_rule_request import PatchedLBFirewallRuleRequest
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 
    patched_lb_firewall_rule_request = pidginhost_sdk.PatchedLBFirewallRuleRequest() # PatchedLBFirewallRuleRequest |  (optional)

    try:
        api_response = api_instance.kubernetes_clusters_lb_firewall_partial_update(cluster_id, id, patched_lb_firewall_rule_request=patched_lb_firewall_rule_request)
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
 **patched_lb_firewall_rule_request** | [**PatchedLBFirewallRuleRequest**](PatchedLBFirewallRuleRequest.md)|  | [optional] 

### Return type

[**LBFirewallRule**](LBFirewallRule.md)

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

# **kubernetes_clusters_lb_firewall_retrieve**
> LBFirewallRule kubernetes_clusters_lb_firewall_retrieve(cluster_id, id)

Adds :class:`~account.iam_enforcement.IAMActionPermission` as an
intersection with the route's existing permission classes (spec §6).

Detail routes (``self.detail``) defer the role/scope check to
``has_object_permission`` so the account-scoped ``get_object`` answers 404
for foreign IDs before any role denial; every other route enforces in
``has_permission``. A detail action that never calls ``get_object`` would
skip enforcement — the route probes pin the denial for each route.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

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

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_lb_firewall_update**
> LBFirewallRule kubernetes_clusters_lb_firewall_update(cluster_id, id, lb_firewall_rule_request=lb_firewall_rule_request)

Adds :class:`~account.iam_enforcement.IAMActionPermission` as an
intersection with the route's existing permission classes (spec §6).

Detail routes (``self.detail``) defer the role/scope check to
``has_object_permission`` so the account-scoped ``get_object`` answers 404
for foreign IDs before any role denial; every other route enforces in
``has_permission``. A detail action that never calls ``get_object`` would
skip enforcement — the route probes pin the denial for each route.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.lb_firewall_rule import LBFirewallRule
from pidginhost_sdk.models.lb_firewall_rule_request import LBFirewallRuleRequest
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 
    lb_firewall_rule_request = pidginhost_sdk.LBFirewallRuleRequest() # LBFirewallRuleRequest |  (optional)

    try:
        api_response = api_instance.kubernetes_clusters_lb_firewall_update(cluster_id, id, lb_firewall_rule_request=lb_firewall_rule_request)
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
 **lb_firewall_rule_request** | [**LBFirewallRuleRequest**](LBFirewallRuleRequest.md)|  | [optional] 

### Return type

[**LBFirewallRule**](LBFirewallRule.md)

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

# **kubernetes_clusters_list**
> PaginatedClusterDetailList kubernetes_clusters_list(page=page)

Adds :class:`~account.iam_enforcement.IAMActionPermission` as an
intersection with the route's existing permission classes (spec §6).

Detail routes (``self.detail``) defer the role/scope check to
``has_object_permission`` so the account-scoped ``get_object`` answers 404
for foreign IDs before any role denial; every other route enforces in
``has_permission``. A detail action that never calls ``get_object`` would
skip enforcement — the route probes pin the denial for each route.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

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

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_node_operations_cancel_create**
> NodeOperation kubernetes_clusters_node_operations_cancel_create(cluster_id, id)

Uncordon the node and abort a blocked operation.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.node_operation import NodeOperation
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 

    try:
        api_response = api_instance.kubernetes_clusters_node_operations_cancel_create(cluster_id, id)
        print("The response of KubernetesApi->kubernetes_clusters_node_operations_cancel_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_node_operations_cancel_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 

### Return type

[**NodeOperation**](NodeOperation.md)

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

# **kubernetes_clusters_node_operations_list**
> PaginatedNodeOperationList kubernetes_clusters_node_operations_list(cluster_id, page=page)

Operation history, status, and the three recovery actions.

Cluster-level rather than node-level on purpose: a successful delete
removes the VM row, so an operation addressable only through its node would
stop being readable exactly when the customer wants to see how it ended.

None of these routes is gated on `K8S_NODE_OPERATIONS_ENABLED`. Turning new
starts off must never strand an operation that is already running -- a
cluster with a blocked operation and no way to answer it is a cluster
nobody can mutate at all.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.paginated_node_operation_list import PaginatedNodeOperationList
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.kubernetes_clusters_node_operations_list(cluster_id, page=page)
        print("The response of KubernetesApi->kubernetes_clusters_node_operations_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_node_operations_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedNodeOperationList**](PaginatedNodeOperationList.md)

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

# **kubernetes_clusters_node_operations_resume_create**
> NodeOperation kubernetes_clusters_node_operations_resume_create(cluster_id, id)

Staff-only resume of an operation waiting for support.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.node_operation import NodeOperation
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 

    try:
        api_response = api_instance.kubernetes_clusters_node_operations_resume_create(cluster_id, id)
        print("The response of KubernetesApi->kubernetes_clusters_node_operations_resume_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_node_operations_resume_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 

### Return type

[**NodeOperation**](NodeOperation.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_node_operations_retrieve**
> NodeOperation kubernetes_clusters_node_operations_retrieve(cluster_id, id)

Operation history, status, and the three recovery actions.

Cluster-level rather than node-level on purpose: a successful delete
removes the VM row, so an operation addressable only through its node would
stop being readable exactly when the customer wants to see how it ended.

None of these routes is gated on `K8S_NODE_OPERATIONS_ENABLED`. Turning new
starts off must never strand an operation that is already running -- a
cluster with a blocked operation and no way to answer it is a cluster
nobody can mutate at all.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.node_operation import NodeOperation
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 

    try:
        api_response = api_instance.kubernetes_clusters_node_operations_retrieve(cluster_id, id)
        print("The response of KubernetesApi->kubernetes_clusters_node_operations_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_node_operations_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 

### Return type

[**NodeOperation**](NodeOperation.md)

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

# **kubernetes_clusters_node_operations_retry_create**
> NodeOperation kubernetes_clusters_node_operations_retry_create(cluster_id, id, node_operation_retry_request=node_operation_retry_request)

Retry a blocked operation with the overrides that answer its blocker.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.node_operation import NodeOperation
from pidginhost_sdk.models.node_operation_retry_request import NodeOperationRetryRequest
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 
    node_operation_retry_request = pidginhost_sdk.NodeOperationRetryRequest() # NodeOperationRetryRequest |  (optional)

    try:
        api_response = api_instance.kubernetes_clusters_node_operations_retry_create(cluster_id, id, node_operation_retry_request=node_operation_retry_request)
        print("The response of KubernetesApi->kubernetes_clusters_node_operations_retry_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_node_operations_retry_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 
 **node_operation_retry_request** | [**NodeOperationRetryRequest**](NodeOperationRetryRequest.md)|  | [optional] 

### Return type

[**NodeOperation**](NodeOperation.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_partial_update**
> ClusterDetail kubernetes_clusters_partial_update(id, patched_cluster_detail_request=patched_cluster_detail_request)

Adds :class:`~account.iam_enforcement.IAMActionPermission` as an
intersection with the route's existing permission classes (spec §6).

Detail routes (``self.detail``) defer the role/scope check to
``has_object_permission`` so the account-scoped ``get_object`` answers 404
for foreign IDs before any role denial; every other route enforces in
``has_permission``. A detail action that never calls ``get_object`` would
skip enforcement — the route probes pin the denial for each route.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.cluster_detail import ClusterDetail
from pidginhost_sdk.models.patched_cluster_detail_request import PatchedClusterDetailRequest
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    id = 'id_example' # str | 
    patched_cluster_detail_request = pidginhost_sdk.PatchedClusterDetailRequest() # PatchedClusterDetailRequest |  (optional)

    try:
        api_response = api_instance.kubernetes_clusters_partial_update(id, patched_cluster_detail_request=patched_cluster_detail_request)
        print("The response of KubernetesApi->kubernetes_clusters_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **patched_cluster_detail_request** | [**PatchedClusterDetailRequest**](PatchedClusterDetailRequest.md)|  | [optional] 

### Return type

[**ClusterDetail**](ClusterDetail.md)

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

# **kubernetes_clusters_pool_removal_journals_list**
> PaginatedPoolRemovalJournalList kubernetes_clusters_pool_removal_journals_list(cluster_id, page=page)

A downsize or pool deletion, its milestones, and its staff resume.

The list route is not in the spec's table and is here anyway: with retrieve
as the only route, a customer whose downsize parked has no way to learn the
journal id, and the panel's poll would be the sole path to a published REST
resource.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.paginated_pool_removal_journal_list import PaginatedPoolRemovalJournalList
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.kubernetes_clusters_pool_removal_journals_list(cluster_id, page=page)
        print("The response of KubernetesApi->kubernetes_clusters_pool_removal_journals_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_pool_removal_journals_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedPoolRemovalJournalList**](PaginatedPoolRemovalJournalList.md)

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

# **kubernetes_clusters_pool_removal_journals_resume_create**
> PoolRemovalJournal kubernetes_clusters_pool_removal_journals_resume_create(cluster_id, id)

Staff-only resume of a pool removal waiting for support.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.pool_removal_journal import PoolRemovalJournal
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 

    try:
        api_response = api_instance.kubernetes_clusters_pool_removal_journals_resume_create(cluster_id, id)
        print("The response of KubernetesApi->kubernetes_clusters_pool_removal_journals_resume_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_pool_removal_journals_resume_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 

### Return type

[**PoolRemovalJournal**](PoolRemovalJournal.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_pool_removal_journals_retrieve**
> PoolRemovalJournal kubernetes_clusters_pool_removal_journals_retrieve(cluster_id, id)

A downsize or pool deletion, its milestones, and its staff resume.

The list route is not in the spec's table and is here anyway: with retrieve
as the only route, a customer whose downsize parked has no way to learn the
journal id, and the panel's poll would be the sole path to a published REST
resource.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.pool_removal_journal import PoolRemovalJournal
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 

    try:
        api_response = api_instance.kubernetes_clusters_pool_removal_journals_retrieve(cluster_id, id)
        print("The response of KubernetesApi->kubernetes_clusters_pool_removal_journals_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_pool_removal_journals_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 

### Return type

[**PoolRemovalJournal**](PoolRemovalJournal.md)

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

# **kubernetes_clusters_port_forwards_create**
> K8sPortForward kubernetes_clusters_port_forwards_create(cluster_id, k8s_port_forward_request)

Adds :class:`~account.iam_enforcement.IAMActionPermission` as an
intersection with the route's existing permission classes (spec §6).

Detail routes (``self.detail``) defer the role/scope check to
``has_object_permission`` so the account-scoped ``get_object`` answers 404
for foreign IDs before any role denial; every other route enforces in
``has_permission``. A detail action that never calls ``get_object`` would
skip enforcement — the route probes pin the denial for each route.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.k8s_port_forward import K8sPortForward
from pidginhost_sdk.models.k8s_port_forward_request import K8sPortForwardRequest
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    k8s_port_forward_request = pidginhost_sdk.K8sPortForwardRequest() # K8sPortForwardRequest | 

    try:
        api_response = api_instance.kubernetes_clusters_port_forwards_create(cluster_id, k8s_port_forward_request)
        print("The response of KubernetesApi->kubernetes_clusters_port_forwards_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_port_forwards_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **k8s_port_forward_request** | [**K8sPortForwardRequest**](K8sPortForwardRequest.md)|  | 

### Return type

[**K8sPortForward**](K8sPortForward.md)

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

# **kubernetes_clusters_port_forwards_destroy**
> kubernetes_clusters_port_forwards_destroy(cluster_id, id)

Adds :class:`~account.iam_enforcement.IAMActionPermission` as an
intersection with the route's existing permission classes (spec §6).

Detail routes (``self.detail``) defer the role/scope check to
``has_object_permission`` so the account-scoped ``get_object`` answers 404
for foreign IDs before any role denial; every other route enforces in
``has_permission``. A detail action that never calls ``get_object`` would
skip enforcement — the route probes pin the denial for each route.

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

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_port_forwards_list**
> PaginatedK8sPortForwardList kubernetes_clusters_port_forwards_list(cluster_id, page=page)

Adds :class:`~account.iam_enforcement.IAMActionPermission` as an
intersection with the route's existing permission classes (spec §6).

Detail routes (``self.detail``) defer the role/scope check to
``has_object_permission`` so the account-scoped ``get_object`` answers 404
for foreign IDs before any role denial; every other route enforces in
``has_permission``. A detail action that never calls ``get_object`` would
skip enforcement — the route probes pin the denial for each route.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.paginated_k8s_port_forward_list import PaginatedK8sPortForwardList
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.kubernetes_clusters_port_forwards_list(cluster_id, page=page)
        print("The response of KubernetesApi->kubernetes_clusters_port_forwards_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_port_forwards_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedK8sPortForwardList**](PaginatedK8sPortForwardList.md)

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

# **kubernetes_clusters_port_forwards_partial_update**
> K8sPortForward kubernetes_clusters_port_forwards_partial_update(cluster_id, id, patched_k8s_port_forward_request=patched_k8s_port_forward_request)

Adds :class:`~account.iam_enforcement.IAMActionPermission` as an
intersection with the route's existing permission classes (spec §6).

Detail routes (``self.detail``) defer the role/scope check to
``has_object_permission`` so the account-scoped ``get_object`` answers 404
for foreign IDs before any role denial; every other route enforces in
``has_permission``. A detail action that never calls ``get_object`` would
skip enforcement — the route probes pin the denial for each route.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.k8s_port_forward import K8sPortForward
from pidginhost_sdk.models.patched_k8s_port_forward_request import PatchedK8sPortForwardRequest
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 
    patched_k8s_port_forward_request = pidginhost_sdk.PatchedK8sPortForwardRequest() # PatchedK8sPortForwardRequest |  (optional)

    try:
        api_response = api_instance.kubernetes_clusters_port_forwards_partial_update(cluster_id, id, patched_k8s_port_forward_request=patched_k8s_port_forward_request)
        print("The response of KubernetesApi->kubernetes_clusters_port_forwards_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_port_forwards_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 
 **patched_k8s_port_forward_request** | [**PatchedK8sPortForwardRequest**](PatchedK8sPortForwardRequest.md)|  | [optional] 

### Return type

[**K8sPortForward**](K8sPortForward.md)

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

# **kubernetes_clusters_port_forwards_retrieve**
> K8sPortForward kubernetes_clusters_port_forwards_retrieve(cluster_id, id)

Adds :class:`~account.iam_enforcement.IAMActionPermission` as an
intersection with the route's existing permission classes (spec §6).

Detail routes (``self.detail``) defer the role/scope check to
``has_object_permission`` so the account-scoped ``get_object`` answers 404
for foreign IDs before any role denial; every other route enforces in
``has_permission``. A detail action that never calls ``get_object`` would
skip enforcement — the route probes pin the denial for each route.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.k8s_port_forward import K8sPortForward
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 

    try:
        api_response = api_instance.kubernetes_clusters_port_forwards_retrieve(cluster_id, id)
        print("The response of KubernetesApi->kubernetes_clusters_port_forwards_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_port_forwards_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 

### Return type

[**K8sPortForward**](K8sPortForward.md)

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

# **kubernetes_clusters_port_forwards_update**
> K8sPortForward kubernetes_clusters_port_forwards_update(cluster_id, id, k8s_port_forward_request)

Adds :class:`~account.iam_enforcement.IAMActionPermission` as an
intersection with the route's existing permission classes (spec §6).

Detail routes (``self.detail``) defer the role/scope check to
``has_object_permission`` so the account-scoped ``get_object`` answers 404
for foreign IDs before any role denial; every other route enforces in
``has_permission``. A detail action that never calls ``get_object`` would
skip enforcement — the route probes pin the denial for each route.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.k8s_port_forward import K8sPortForward
from pidginhost_sdk.models.k8s_port_forward_request import K8sPortForwardRequest
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 
    k8s_port_forward_request = pidginhost_sdk.K8sPortForwardRequest() # K8sPortForwardRequest | 

    try:
        api_response = api_instance.kubernetes_clusters_port_forwards_update(cluster_id, id, k8s_port_forward_request)
        print("The response of KubernetesApi->kubernetes_clusters_port_forwards_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_port_forwards_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 
 **k8s_port_forward_request** | [**K8sPortForwardRequest**](K8sPortForwardRequest.md)|  | 

### Return type

[**K8sPortForward**](K8sPortForward.md)

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

# **kubernetes_clusters_resource_pools_create**
> ResourcePoolAddResponse kubernetes_clusters_resource_pools_create(cluster_id, resource_pool_add_request)

Create new resource pool

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.resource_pool_add_request import ResourcePoolAddRequest
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    resource_pool_add_request = pidginhost_sdk.ResourcePoolAddRequest() # ResourcePoolAddRequest | 

    try:
        api_response = api_instance.kubernetes_clusters_resource_pools_create(cluster_id, resource_pool_add_request)
        print("The response of KubernetesApi->kubernetes_clusters_resource_pools_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_resource_pools_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **resource_pool_add_request** | [**ResourcePoolAddRequest**](ResourcePoolAddRequest.md)|  | 

### Return type

[**ResourcePoolAddResponse**](ResourcePoolAddResponse.md)

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

# **kubernetes_clusters_resource_pools_destroy**
> kubernetes_clusters_resource_pools_destroy(cluster_id, id)

Adds :class:`~account.iam_enforcement.IAMActionPermission` as an
intersection with the route's existing permission classes (spec §6).

Detail routes (``self.detail``) defer the role/scope check to
``has_object_permission`` so the account-scoped ``get_object`` answers 404
for foreign IDs before any role denial; every other route enforces in
``has_permission``. A detail action that never calls ``get_object`` would
skip enforcement — the route probes pin the denial for each route.

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

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

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

Adds :class:`~account.iam_enforcement.IAMActionPermission` as an
intersection with the route's existing permission classes (spec §6).

Detail routes (``self.detail``) defer the role/scope check to
``has_object_permission`` so the account-scoped ``get_object`` answers 404
for foreign IDs before any role denial; every other route enforces in
``has_permission``. A detail action that never calls ``get_object`` would
skip enforcement — the route probes pin the denial for each route.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

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

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_resource_pools_nodes_destroy**
> NodeOperation kubernetes_clusters_resource_pools_nodes_destroy(cluster_id, id, pool_id)

Start a safe delete of one worker node.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.node_operation import NodeOperation
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 
    pool_id = 56 # int | 

    try:
        api_response = api_instance.kubernetes_clusters_resource_pools_nodes_destroy(cluster_id, id, pool_id)
        print("The response of KubernetesApi->kubernetes_clusters_resource_pools_nodes_destroy:\n")
        pprint(api_response)
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

[**NodeOperation**](NodeOperation.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_resource_pools_nodes_list**
> PaginatedResourcePoolNodeList kubernetes_clusters_resource_pools_nodes_list(cluster_id, pool_id, page=page)

Adds :class:`~account.iam_enforcement.IAMActionPermission` as an
intersection with the route's existing permission classes (spec §6).

Detail routes (``self.detail``) defer the role/scope check to
``has_object_permission`` so the account-scoped ``get_object`` answers 404
for foreign IDs before any role denial; every other route enforces in
``has_permission``. A detail action that never calls ``get_object`` would
skip enforcement — the route probes pin the denial for each route.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

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

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

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

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

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

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_resource_pools_nodes_reboot_create**
> NodeOperation kubernetes_clusters_resource_pools_nodes_reboot_create(cluster_id, id, pool_id, node_operation_reboot_request=node_operation_reboot_request)

Restart one worker node, draining it first.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.node_operation import NodeOperation
from pidginhost_sdk.models.node_operation_reboot_request import NodeOperationRebootRequest
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 
    pool_id = 56 # int | 
    node_operation_reboot_request = pidginhost_sdk.NodeOperationRebootRequest() # NodeOperationRebootRequest |  (optional)

    try:
        api_response = api_instance.kubernetes_clusters_resource_pools_nodes_reboot_create(cluster_id, id, pool_id, node_operation_reboot_request=node_operation_reboot_request)
        print("The response of KubernetesApi->kubernetes_clusters_resource_pools_nodes_reboot_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_resource_pools_nodes_reboot_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 
 **pool_id** | **int**|  | 
 **node_operation_reboot_request** | [**NodeOperationRebootRequest**](NodeOperationRebootRequest.md)|  | [optional] 

### Return type

[**NodeOperation**](NodeOperation.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_resource_pools_nodes_retrieve**
> ResourcePoolNode kubernetes_clusters_resource_pools_nodes_retrieve(cluster_id, id, pool_id)

Adds :class:`~account.iam_enforcement.IAMActionPermission` as an
intersection with the route's existing permission classes (spec §6).

Detail routes (``self.detail``) defer the role/scope check to
``has_object_permission`` so the account-scoped ``get_object`` answers 404
for foreign IDs before any role denial; every other route enforces in
``has_permission``. A detail action that never calls ``get_object`` would
skip enforcement — the route probes pin the denial for each route.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

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

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_resource_pools_nodes_rrd_retrieve**
> NodeRRDResponse kubernetes_clusters_resource_pools_nodes_rrd_retrieve(cluster_id, id, pool_id, timeframe=timeframe)

Get RRD (historical) metrics data for a node VM.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 
    pool_id = 56 # int | 
    timeframe = 'hour' # str | Window of recorded data to return. (optional) (default to 'hour')

    try:
        api_response = api_instance.kubernetes_clusters_resource_pools_nodes_rrd_retrieve(cluster_id, id, pool_id, timeframe=timeframe)
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
 **timeframe** | **str**| Window of recorded data to return. | [optional] [default to &#39;hour&#39;]

### Return type

[**NodeRRDResponse**](NodeRRDResponse.md)

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

# **kubernetes_clusters_resource_pools_partial_update**
> ResourcePool kubernetes_clusters_resource_pools_partial_update(cluster_id, id, patched_resource_pool_request=patched_resource_pool_request)

Adds :class:`~account.iam_enforcement.IAMActionPermission` as an
intersection with the route's existing permission classes (spec §6).

Detail routes (``self.detail``) defer the role/scope check to
``has_object_permission`` so the account-scoped ``get_object`` answers 404
for foreign IDs before any role denial; every other route enforces in
``has_permission``. A detail action that never calls ``get_object`` would
skip enforcement — the route probes pin the denial for each route.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.patched_resource_pool_request import PatchedResourcePoolRequest
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 
    patched_resource_pool_request = pidginhost_sdk.PatchedResourcePoolRequest() # PatchedResourcePoolRequest |  (optional)

    try:
        api_response = api_instance.kubernetes_clusters_resource_pools_partial_update(cluster_id, id, patched_resource_pool_request=patched_resource_pool_request)
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
 **patched_resource_pool_request** | [**PatchedResourcePoolRequest**](PatchedResourcePoolRequest.md)|  | [optional] 

### Return type

[**ResourcePool**](ResourcePool.md)

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

# **kubernetes_clusters_resource_pools_retrieve**
> ResourcePool kubernetes_clusters_resource_pools_retrieve(cluster_id, id)

Adds :class:`~account.iam_enforcement.IAMActionPermission` as an
intersection with the route's existing permission classes (spec §6).

Detail routes (``self.detail``) defer the role/scope check to
``has_object_permission`` so the account-scoped ``get_object`` answers 404
for foreign IDs before any role denial; every other route enforces in
``has_permission``. A detail action that never calls ``get_object`` would
skip enforcement — the route probes pin the denial for each route.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

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

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_resource_pools_update**
> ResourcePool kubernetes_clusters_resource_pools_update(cluster_id, id, resource_pool_request=resource_pool_request)

Adds :class:`~account.iam_enforcement.IAMActionPermission` as an
intersection with the route's existing permission classes (spec §6).

Detail routes (``self.detail``) defer the role/scope check to
``has_object_permission`` so the account-scoped ``get_object`` answers 404
for foreign IDs before any role denial; every other route enforces in
``has_permission``. A detail action that never calls ``get_object`` would
skip enforcement — the route probes pin the denial for each route.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.resource_pool import ResourcePool
from pidginhost_sdk.models.resource_pool_request import ResourcePoolRequest
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 
    resource_pool_request = pidginhost_sdk.ResourcePoolRequest() # ResourcePoolRequest |  (optional)

    try:
        api_response = api_instance.kubernetes_clusters_resource_pools_update(cluster_id, id, resource_pool_request=resource_pool_request)
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
 **resource_pool_request** | [**ResourcePoolRequest**](ResourcePoolRequest.md)|  | [optional] 

### Return type

[**ResourcePool**](ResourcePool.md)

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

# **kubernetes_clusters_retrieve**
> ClusterDetail kubernetes_clusters_retrieve(id)

Adds :class:`~account.iam_enforcement.IAMActionPermission` as an
intersection with the route's existing permission classes (spec §6).

Detail routes (``self.detail``) defer the role/scope check to
``has_object_permission`` so the account-scoped ``get_object`` answers 404
for foreign IDs before any role denial; every other route enforces in
``has_permission``. A detail action that never calls ``get_object`` would
skip enforcement — the route probes pin the denial for each route.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

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

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

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

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

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

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_tcproutes_create**
> TCPRoute kubernetes_clusters_tcproutes_create(cluster_id, tcp_route_request)

Create new TCPRoute

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.tcp_route import TCPRoute
from pidginhost_sdk.models.tcp_route_request import TCPRouteRequest
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    tcp_route_request = pidginhost_sdk.TCPRouteRequest() # TCPRouteRequest | 

    try:
        api_response = api_instance.kubernetes_clusters_tcproutes_create(cluster_id, tcp_route_request)
        print("The response of KubernetesApi->kubernetes_clusters_tcproutes_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_tcproutes_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **tcp_route_request** | [**TCPRouteRequest**](TCPRouteRequest.md)|  | 

### Return type

[**TCPRoute**](TCPRoute.md)

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

# **kubernetes_clusters_tcproutes_destroy**
> kubernetes_clusters_tcproutes_destroy(cluster_id, id)

ViewSet for managing TCPRoute resources.

TCPRoutes expose TCP services through the Gateway on specific external ports.
Reserved ports (22, 6443, 50000, 50001) cannot be exposed.

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

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_tcproutes_list**
> PaginatedTCPRouteList kubernetes_clusters_tcproutes_list(cluster_id, page=page)

ViewSet for managing TCPRoute resources.

TCPRoutes expose TCP services through the Gateway on specific external ports.
Reserved ports (22, 6443, 50000, 50001) cannot be exposed.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.paginated_tcp_route_list import PaginatedTCPRouteList
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.kubernetes_clusters_tcproutes_list(cluster_id, page=page)
        print("The response of KubernetesApi->kubernetes_clusters_tcproutes_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_tcproutes_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedTCPRouteList**](PaginatedTCPRouteList.md)

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

# **kubernetes_clusters_tcproutes_partial_update**
> TCPRoute kubernetes_clusters_tcproutes_partial_update(cluster_id, id, patched_tcp_route_request=patched_tcp_route_request)

Partially update TCPRoute

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.patched_tcp_route_request import PatchedTCPRouteRequest
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 
    patched_tcp_route_request = pidginhost_sdk.PatchedTCPRouteRequest() # PatchedTCPRouteRequest |  (optional)

    try:
        api_response = api_instance.kubernetes_clusters_tcproutes_partial_update(cluster_id, id, patched_tcp_route_request=patched_tcp_route_request)
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
 **patched_tcp_route_request** | [**PatchedTCPRouteRequest**](PatchedTCPRouteRequest.md)|  | [optional] 

### Return type

[**TCPRoute**](TCPRoute.md)

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

# **kubernetes_clusters_tcproutes_retrieve**
> TCPRoute kubernetes_clusters_tcproutes_retrieve(cluster_id, id)

ViewSet for managing TCPRoute resources.

TCPRoutes expose TCP services through the Gateway on specific external ports.
Reserved ports (22, 6443, 50000, 50001) cannot be exposed.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 

    try:
        api_response = api_instance.kubernetes_clusters_tcproutes_retrieve(cluster_id, id)
        print("The response of KubernetesApi->kubernetes_clusters_tcproutes_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_tcproutes_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 

### Return type

[**TCPRoute**](TCPRoute.md)

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

# **kubernetes_clusters_tcproutes_update**
> TCPRoute kubernetes_clusters_tcproutes_update(cluster_id, id, tcp_route_request)

Update TCPRoute

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.tcp_route import TCPRoute
from pidginhost_sdk.models.tcp_route_request import TCPRouteRequest
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 
    tcp_route_request = pidginhost_sdk.TCPRouteRequest() # TCPRouteRequest | 

    try:
        api_response = api_instance.kubernetes_clusters_tcproutes_update(cluster_id, id, tcp_route_request)
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
 **tcp_route_request** | [**TCPRouteRequest**](TCPRouteRequest.md)|  | 

### Return type

[**TCPRoute**](TCPRoute.md)

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

# **kubernetes_clusters_toggle_cloud_vm_access_create**
> ToggleCloudVMAccessResponse kubernetes_clusters_toggle_cloud_vm_access_create(id)

Toggle cloud VM access for this cluster.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

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

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_udproutes_create**
> UDPRoute kubernetes_clusters_udproutes_create(cluster_id, udp_route_request)

Create new UDPRoute

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.udp_route import UDPRoute
from pidginhost_sdk.models.udp_route_request import UDPRouteRequest
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    udp_route_request = pidginhost_sdk.UDPRouteRequest() # UDPRouteRequest | 

    try:
        api_response = api_instance.kubernetes_clusters_udproutes_create(cluster_id, udp_route_request)
        print("The response of KubernetesApi->kubernetes_clusters_udproutes_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_udproutes_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **udp_route_request** | [**UDPRouteRequest**](UDPRouteRequest.md)|  | 

### Return type

[**UDPRoute**](UDPRoute.md)

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

# **kubernetes_clusters_udproutes_destroy**
> kubernetes_clusters_udproutes_destroy(cluster_id, id)

ViewSet for managing UDPRoute resources.

UDPRoutes expose UDP services through the Gateway on specific external ports.

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

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_udproutes_list**
> PaginatedUDPRouteList kubernetes_clusters_udproutes_list(cluster_id, page=page)

ViewSet for managing UDPRoute resources.

UDPRoutes expose UDP services through the Gateway on specific external ports.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.paginated_udp_route_list import PaginatedUDPRouteList
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    page = 56 # int | A page number within the paginated result set. (optional)

    try:
        api_response = api_instance.kubernetes_clusters_udproutes_list(cluster_id, page=page)
        print("The response of KubernetesApi->kubernetes_clusters_udproutes_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_udproutes_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **page** | **int**| A page number within the paginated result set. | [optional] 

### Return type

[**PaginatedUDPRouteList**](PaginatedUDPRouteList.md)

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

# **kubernetes_clusters_udproutes_partial_update**
> UDPRoute kubernetes_clusters_udproutes_partial_update(cluster_id, id, patched_udp_route_request=patched_udp_route_request)

Partially update UDPRoute

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.patched_udp_route_request import PatchedUDPRouteRequest
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 
    patched_udp_route_request = pidginhost_sdk.PatchedUDPRouteRequest() # PatchedUDPRouteRequest |  (optional)

    try:
        api_response = api_instance.kubernetes_clusters_udproutes_partial_update(cluster_id, id, patched_udp_route_request=patched_udp_route_request)
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
 **patched_udp_route_request** | [**PatchedUDPRouteRequest**](PatchedUDPRouteRequest.md)|  | [optional] 

### Return type

[**UDPRoute**](UDPRoute.md)

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

# **kubernetes_clusters_udproutes_retrieve**
> UDPRoute kubernetes_clusters_udproutes_retrieve(cluster_id, id)

ViewSet for managing UDPRoute resources.

UDPRoutes expose UDP services through the Gateway on specific external ports.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 

    try:
        api_response = api_instance.kubernetes_clusters_udproutes_retrieve(cluster_id, id)
        print("The response of KubernetesApi->kubernetes_clusters_udproutes_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_udproutes_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **int**|  | 
 **id** | **str**|  | 

### Return type

[**UDPRoute**](UDPRoute.md)

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

# **kubernetes_clusters_udproutes_update**
> UDPRoute kubernetes_clusters_udproutes_update(cluster_id, id, udp_route_request)

Update UDPRoute

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.udp_route import UDPRoute
from pidginhost_sdk.models.udp_route_request import UDPRouteRequest
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    cluster_id = 56 # int | 
    id = 'id_example' # str | 
    udp_route_request = pidginhost_sdk.UDPRouteRequest() # UDPRouteRequest | 

    try:
        api_response = api_instance.kubernetes_clusters_udproutes_update(cluster_id, id, udp_route_request)
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
 **udp_route_request** | [**UDPRouteRequest**](UDPRouteRequest.md)|  | 

### Return type

[**UDPRoute**](UDPRoute.md)

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

# **kubernetes_clusters_update**
> ClusterDetail kubernetes_clusters_update(id, cluster_detail_request)

Adds :class:`~account.iam_enforcement.IAMActionPermission` as an
intersection with the route's existing permission classes (spec §6).

Detail routes (``self.detail``) defer the role/scope check to
``has_object_permission`` so the account-scoped ``get_object`` answers 404
for foreign IDs before any role denial; every other route enforces in
``has_permission``. A detail action that never calls ``get_object`` would
skip enforcement — the route probes pin the denial for each route.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.cluster_detail import ClusterDetail
from pidginhost_sdk.models.cluster_detail_request import ClusterDetailRequest
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    id = 'id_example' # str | 
    cluster_detail_request = pidginhost_sdk.ClusterDetailRequest() # ClusterDetailRequest | 

    try:
        api_response = api_instance.kubernetes_clusters_update(id, cluster_detail_request)
        print("The response of KubernetesApi->kubernetes_clusters_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **cluster_detail_request** | [**ClusterDetailRequest**](ClusterDetailRequest.md)|  | 

### Return type

[**ClusterDetail**](ClusterDetail.md)

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

# **kubernetes_clusters_upgrade_feature_create**
> FeatureUpgradeResponse kubernetes_clusters_upgrade_feature_create(id, feature_upgrade_request)

Upgrade a cluster feature to the latest compatible version.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

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

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_clusters_upgrade_lb_create**
> LBUpgradePlanResponse kubernetes_clusters_upgrade_lb_create(id, lb_upgrade_request=lb_upgrade_request)

Inspect or perform the load-balancer upgrade the server computes for this cluster. The caller never selects a level.

### Example

* Api Key Authentication (tokenAuth):
* Api Key Authentication (cookieAuth):

```python
import pidginhost_sdk
from pidginhost_sdk.models.lb_upgrade_plan_response import LBUpgradePlanResponse
from pidginhost_sdk.models.lb_upgrade_request import LBUpgradeRequest
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
    api_instance = pidginhost_sdk.KubernetesApi(api_client)
    id = 'id_example' # str | 
    lb_upgrade_request = pidginhost_sdk.LBUpgradeRequest() # LBUpgradeRequest |  (optional)

    try:
        api_response = api_instance.kubernetes_clusters_upgrade_lb_create(id, lb_upgrade_request=lb_upgrade_request)
        print("The response of KubernetesApi->kubernetes_clusters_upgrade_lb_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_clusters_upgrade_lb_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **lb_upgrade_request** | [**LBUpgradeRequest**](LBUpgradeRequest.md)|  | [optional] 

### Return type

[**LBUpgradePlanResponse**](LBUpgradePlanResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

