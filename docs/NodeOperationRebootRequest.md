# NodeOperationRebootRequest

A reboot destroys the same local data a delete does, and says so.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_data_loss_accepted** | **bool** | Acknowledge that data kept on the node itself is destroyed. The drain always deletes emptyDir. | [optional] [default to False]

## Example

```python
from pidginhost_sdk.models.node_operation_reboot_request import NodeOperationRebootRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NodeOperationRebootRequest from a JSON string
node_operation_reboot_request_instance = NodeOperationRebootRequest.from_json(json)
# print the JSON string representation of the object
print(NodeOperationRebootRequest.to_json())

# convert the object into a dict
node_operation_reboot_request_dict = node_operation_reboot_request_instance.to_dict()
# create an instance of NodeOperationRebootRequest from a dict
node_operation_reboot_request_from_dict = NodeOperationRebootRequest.from_dict(node_operation_reboot_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


