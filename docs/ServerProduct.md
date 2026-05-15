# ServerProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**slug** | **str** |  | 
**name** | **str** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.server_product import ServerProduct

# TODO update the JSON string below
json = "{}"
# create an instance of ServerProduct from a JSON string
server_product_instance = ServerProduct.from_json(json)
# print the JSON string representation of the object
print(ServerProduct.to_json())

# convert the object into a dict
server_product_dict = server_product_instance.to_dict()
# create an instance of ServerProduct from a dict
server_product_from_dict = ServerProduct.from_dict(server_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


