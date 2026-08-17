# ServiceCompany


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 

## Example

```python
from pidginhost_sdk.models.service_company import ServiceCompany

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceCompany from a JSON string
service_company_instance = ServiceCompany.from_json(json)
# print the JSON string representation of the object
print(ServiceCompany.to_json())

# convert the object into a dict
service_company_dict = service_company_instance.to_dict()
# create an instance of ServiceCompany from a dict
service_company_from_dict = ServiceCompany.from_dict(service_company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


