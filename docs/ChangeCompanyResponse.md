# ChangeCompanyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**company** | **Dict[str, object]** |  | 

## Example

```python
from pidginhost_sdk.models.change_company_response import ChangeCompanyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeCompanyResponse from a JSON string
change_company_response_instance = ChangeCompanyResponse.from_json(json)
# print the JSON string representation of the object
print(ChangeCompanyResponse.to_json())

# convert the object into a dict
change_company_response_dict = change_company_response_instance.to_dict()
# create an instance of ChangeCompanyResponse from a dict
change_company_response_from_dict = ChangeCompanyResponse.from_dict(change_company_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


