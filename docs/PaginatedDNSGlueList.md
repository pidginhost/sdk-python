# PaginatedDNSGlueList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[DNSGlue]**](DNSGlue.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_dns_glue_list import PaginatedDNSGlueList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedDNSGlueList from a JSON string
paginated_dns_glue_list_instance = PaginatedDNSGlueList.from_json(json)
# print the JSON string representation of the object
print(PaginatedDNSGlueList.to_json())

# convert the object into a dict
paginated_dns_glue_list_dict = paginated_dns_glue_list_instance.to_dict()
# create an instance of PaginatedDNSGlueList from a dict
paginated_dns_glue_list_from_dict = PaginatedDNSGlueList.from_dict(paginated_dns_glue_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


