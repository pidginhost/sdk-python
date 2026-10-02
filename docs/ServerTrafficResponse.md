# ServerTrafficResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**year** | **int** |  | 
**month** | **int** |  | 
**as_of** | **date** |  | 
**status** | **str** |  | 
**bytes_in** | **int** |  | 
**bytes_out** | **int** |  | 
**bytes_total** | **int** |  | 
**included_tb** | **int** |  | 
**used_units** | **int** |  | 
**used_tb** | **str** | Usage rounded up to six decimal places; bytes_total is exact. | 
**billable_bytes** | **int** | Of bytes_total, the part that may be charged. | 
**billable_units** | **int** |  | 
**billable_tb** | **str** | Billable usage rounded up to six decimal places; billable_bytes is exact. | 
**billable_from** | **date** | First fully billable day, when one date describes the usage. May fall after the reported month. Null when all usage is billable or streams have different boundaries; use billable_bytes for the billable total. | 
**charged_tb** | **int** |  | 
**charged_amount** | **str** |  | 
**price_per_tb** | **str** |  | 
**currency** | **str** |  | 
**unit_bytes** | **int** |  | 
**remaining_bytes** | **int** |  | 
**last_sample_at** | **date** |  | 
**daily** | **List[Dict[str, object]]** |  | 

## Example

```python
from pidginhost_sdk.models.server_traffic_response import ServerTrafficResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServerTrafficResponse from a JSON string
server_traffic_response_instance = ServerTrafficResponse.from_json(json)
# print the JSON string representation of the object
print(ServerTrafficResponse.to_json())

# convert the object into a dict
server_traffic_response_dict = server_traffic_response_instance.to_dict()
# create an instance of ServerTrafficResponse from a dict
server_traffic_response_from_dict = ServerTrafficResponse.from_dict(server_traffic_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


