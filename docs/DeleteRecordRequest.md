# DeleteRecordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line** | **int** | Line number of the DNS record to delete. | 

## Example

```python
from pidginhost_sdk.models.delete_record_request import DeleteRecordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteRecordRequest from a JSON string
delete_record_request_instance = DeleteRecordRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteRecordRequest.to_json())

# convert the object into a dict
delete_record_request_dict = delete_record_request_instance.to_dict()
# create an instance of DeleteRecordRequest from a dict
delete_record_request_from_dict = DeleteRecordRequest.from_dict(delete_record_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


