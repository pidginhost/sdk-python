# ServerAdd


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | **str** | ID or slug | 
**package** | **str** | ID or slug | 
**hostname** | **str** |  | [optional] 
**project** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**ssh_pub_key** | **str** | New SSH key | [optional] 
**ssh_pub_key_id** | **str** | ID or fingerprint | [optional] 
**public_ip** | **str** | ID or slug | [optional] 
**new_ipv4** | **bool** |  | [optional] 
**public_ipv6** | **str** | ID or slug | [optional] 
**new_ipv6** | **bool** |  | [optional] 
**fw_rules_set** | **str** | ID or slug | [optional] 
**fw_policy_in** | [**FwPolicyOutEnum**](FwPolicyOutEnum.md) |  | [optional] 
**fw_policy_out** | [**FwPolicyOutEnum**](FwPolicyOutEnum.md) |  | [optional] 
**private_network** | **str** | ID or slug | [optional] 
**private_address** | **str** | Leave empty for auto-assign | [optional] 
**extra_volume_product** | **str** | ID or slug | [optional] 
**extra_volume_size** | **int** |  | [optional] [default to 0]
**no_network_acknowledged** | **bool** |  | [optional] 
**enable_ha** | **bool** |  | [optional] [default to False]

## Example

```python
from pidginhost_sdk.models.server_add import ServerAdd

# TODO update the JSON string below
json = "{}"
# create an instance of ServerAdd from a JSON string
server_add_instance = ServerAdd.from_json(json)
# print the JSON string representation of the object
print(ServerAdd.to_json())

# convert the object into a dict
server_add_dict = server_add_instance.to_dict()
# create an instance of ServerAdd from a dict
server_add_from_dict = ServerAdd.from_dict(server_add_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


