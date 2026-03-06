# PublicIPv4


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
from pidginhost_sdk.models.public_ipv4 import PublicIPv4

# TODO update the JSON string below
json = "{}"
# create an instance of PublicIPv4 from a JSON string
public_ipv4_instance = PublicIPv4.from_json(json)
# print the JSON string representation of the object
print(PublicIPv4.to_json())

# convert the object into a dict
public_ipv4_dict = public_ipv4_instance.to_dict()
# create an instance of PublicIPv4 from a dict
public_ipv4_from_dict = PublicIPv4.from_dict(public_ipv4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


