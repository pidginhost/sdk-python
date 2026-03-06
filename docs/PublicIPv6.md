# PublicIPv6


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**slug** | **str** |  | [readonly] 
**address** | **str** |  | [readonly] 
**gateway** | **str** |  | [readonly] 
**prefix** | **int** |  | [readonly] 
**attached** | **bool** |  | [readonly] 
**server** | **str** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.public_ipv6 import PublicIPv6

# TODO update the JSON string below
json = "{}"
# create an instance of PublicIPv6 from a JSON string
public_ipv6_instance = PublicIPv6.from_json(json)
# print the JSON string representation of the object
print(PublicIPv6.to_json())

# convert the object into a dict
public_ipv6_dict = public_ipv6_instance.to_dict()
# create an instance of PublicIPv6 from a dict
public_ipv6_from_dict = PublicIPv6.from_dict(public_ipv6_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


