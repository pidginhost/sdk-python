# PaginatedSubscriptionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[Subscription]**](Subscription.md) |  | 

## Example

```python
from pidginhost_sdk.models.paginated_subscription_list import PaginatedSubscriptionList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedSubscriptionList from a JSON string
paginated_subscription_list_instance = PaginatedSubscriptionList.from_json(json)
# print the JSON string representation of the object
print(PaginatedSubscriptionList.to_json())

# convert the object into a dict
paginated_subscription_list_dict = paginated_subscription_list_instance.to_dict()
# create an instance of PaginatedSubscriptionList from a dict
paginated_subscription_list_from_dict = PaginatedSubscriptionList.from_dict(paginated_subscription_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


