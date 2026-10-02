# ChangeCompanyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company_id** | **int** |  | [optional] 

## Example

```python
from pidginhost_sdk.models.change_company_request import ChangeCompanyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeCompanyRequest from a JSON string
change_company_request_instance = ChangeCompanyRequest.from_json(json)
# print the JSON string representation of the object
print(ChangeCompanyRequest.to_json())

# convert the object into a dict
change_company_request_dict = change_company_request_instance.to_dict()
# create an instance of ChangeCompanyRequest from a dict
change_company_request_from_dict = ChangeCompanyRequest.from_dict(change_company_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


