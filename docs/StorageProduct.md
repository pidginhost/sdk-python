# StorageProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**slug** | **str** |  | 
**name** | **str** |  | [readonly] 
**type** | **str** |  | [readonly] 
**unit** | **str** |  | [readonly] 
**price** | **decimal.Decimal** | price per quantity units per month (if applicable) | 
**min_size** | **str** |  | [readonly] 
**max_size** | **str** |  | [readonly] 

## Example

```python
from pidginhost_sdk.models.storage_product import StorageProduct

# TODO update the JSON string below
json = "{}"
# create an instance of StorageProduct from a JSON string
storage_product_instance = StorageProduct.from_json(json)
# print the JSON string representation of the object
print(StorageProduct.to_json())

# convert the object into a dict
storage_product_dict = storage_product_instance.to_dict()
# create an instance of StorageProduct from a dict
storage_product_from_dict = StorageProduct.from_dict(storage_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


