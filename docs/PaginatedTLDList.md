# PaginatedTLDList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[TLD]**](TLD.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_tld_list import PaginatedTLDList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedTLDList from a JSON string
paginated_tld_list_instance = PaginatedTLDList.from_json(json)
# print the JSON string representation of the object
print(PaginatedTLDList.to_json())

# convert the object into a dict
paginated_tld_list_dict = paginated_tld_list_instance.to_dict()
# create an instance of PaginatedTLDList from a dict
paginated_tld_list_from_dict = PaginatedTLDList.from_dict(paginated_tld_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


