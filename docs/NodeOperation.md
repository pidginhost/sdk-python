# NodeOperation

What a customer may see about their own node operation.  The omissions are the point. Private address, Node UID, VMID, Proxmox placement, and every request/task/lease field stay on the staff serializer: they name internal topology, and a status endpoint is not where that becomes public.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**kind** | [**NodeOperationKindEnum**](NodeOperationKindEnum.md) |  | [readonly] 
**source** | [**NodeOperationSourceEnum**](NodeOperationSourceEnum.md) |  | [readonly] 
**target_hostname** | **str** |  | [readonly] 
**status** | [**NodeOperationStatusEnum**](NodeOperationStatusEnum.md) |  | [readonly] 
**reason** | **str** |  | [readonly] 
**message** | **str** |  | [readonly] 
**bypass_pdb** | **bool** |  | [readonly] 
**delete_unmanaged_pods** | **bool** |  | [readonly] 
**local_data_loss_accepted** | **bool** |  | [readonly] 
**bypass_pdb_confirmed_at** | **str** |  | [readonly] 
**unmanaged_pods_confirmed_at** | **str** |  | [readonly] 
**actor_label** | **str** | Who requested the operation (user email or staff name). Never token material. | [readonly] 
**created_at** | **str** |  | [readonly] 
**updated_at** | **str** |  | [readonly] 
**finished_at** | **str** |  | [readonly] 
**allowed_actions** | **List[str]** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.node_operation import NodeOperation

# TODO update the JSON string below
json = "{}"
# create an instance of NodeOperation from a JSON string
node_operation_instance = NodeOperation.from_json(json)
# print the JSON string representation of the object
print(NodeOperation.to_json())

# convert the object into a dict
node_operation_dict = node_operation_instance.to_dict()
# create an instance of NodeOperation from a dict
node_operation_from_dict = NodeOperation.from_dict(node_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


