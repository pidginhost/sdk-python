# PaginatedSSHKeyList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[SSHKey]**](SSHKey.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_ssh_key_list import PaginatedSSHKeyList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSSHKeyList from a JSON string
paginated_ssh_key_list_instance = PaginatedSSHKeyList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSSHKeyList.to_json())

# convert the object into a dict
paginated_ssh_key_list_dict = paginated_ssh_key_list_instance.to_dict()
# create an instance of PaginatedSSHKeyList from a dict
paginated_ssh_key_list_from_dict = PaginatedSSHKeyList.from_dict(paginated_ssh_key_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


