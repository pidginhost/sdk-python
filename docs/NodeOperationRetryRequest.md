# NodeOperationRetryRequest

The two independent overrides, and the acknowledgement each one needs.  Both flags are tri-state and the third state is what matters: `null`/absent means \"leave it as it is\". A plain boolean default would turn every request that names one flag into a request that silently un-forces the other, and `retry_node_operation` refuses an un-force rather than applying it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bypass_pdb** | **bool** |  | [optional] 
**delete_unmanaged_pods** | **bool** |  | [optional] 
**acknowledge_pdb_bypass** | **bool** |  | [optional] [default to False]
**acknowledge_unmanaged_pod_deletion** | **bool** |  | [optional] [default to False]

## Example

```python
from pidginhost_sdk.models.node_operation_retry_request import NodeOperationRetryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NodeOperationRetryRequest from a JSON string
node_operation_retry_request_instance = NodeOperationRetryRequest.from_json(json)
# print the JSON string representation of the object
print(NodeOperationRetryRequest.to_json())

# convert the object into a dict
node_operation_retry_request_dict = node_operation_retry_request_instance.to_dict()
# create an instance of NodeOperationRetryRequest from a dict
node_operation_retry_request_from_dict = NodeOperationRetryRequest.from_dict(node_operation_retry_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


