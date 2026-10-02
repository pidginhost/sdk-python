# ClusterEncryptionRequest

The body of a toggle or a staff reconcile.  Field errors are re-raised as ``EncryptionConflict`` rather than left as DRF validation errors: the endpoint answers every refusal with the feature's stable reason code, and a body that switched shape depending on WHICH refusal it was would force a client to parse two.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | [**EncryptionModeEnum**](EncryptionModeEnum.md) | Target encryption mode: no encryption, or WireGuard.  * &#x60;none&#x60; - none * &#x60;wireguard&#x60; - wireguard | 
**acknowledge_workload_restart** | **bool** | Confirms the caller accepts that workloads must be restarted after the change. | [optional] [default to False]

## Example

```python
from pidginhost_sdk.models.cluster_encryption_request import ClusterEncryptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterEncryptionRequest from a JSON string
cluster_encryption_request_instance = ClusterEncryptionRequest.from_json(json)
# print the JSON string representation of the object
print(ClusterEncryptionRequest.to_json())

# convert the object into a dict
cluster_encryption_request_dict = cluster_encryption_request_instance.to_dict()
# create an instance of ClusterEncryptionRequest from a dict
cluster_encryption_request_from_dict = ClusterEncryptionRequest.from_dict(cluster_encryption_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


