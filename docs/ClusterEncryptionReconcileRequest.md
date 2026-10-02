# ClusterEncryptionReconcileRequest

The staff reconcile body, which alone may carry the override.  A SEPARATE component rather than an optional field on the shared one. The toggle route ignores the flag entirely, so declaring it in one body would hand a generated client an argument that silently does nothing on half the routes carrying it -- the same class of published untruth the rest of this feature's schema work exists to prevent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | [**EncryptionModeEnum**](EncryptionModeEnum.md) | Target encryption mode: no encryption, or WireGuard.  * &#x60;none&#x60; - none * &#x60;wireguard&#x60; - wireguard | 
**acknowledge_workload_restart** | **bool** | Confirms the caller accepts that workloads must be restarted after the change. | [optional] [default to False]
**override_unverifiable** | **bool** | Record this mode even if verification refuses, together with what was observed. Only the unencrypted mode can be asserted this way: an encrypted state always requires positive per-node evidence. | [optional] [default to False]

## Example

```python
from pidginhost_sdk.models.cluster_encryption_reconcile_request import ClusterEncryptionReconcileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterEncryptionReconcileRequest from a JSON string
cluster_encryption_reconcile_request_instance = ClusterEncryptionReconcileRequest.from_json(json)
# print the JSON string representation of the object
print(ClusterEncryptionReconcileRequest.to_json())

# convert the object into a dict
cluster_encryption_reconcile_request_dict = cluster_encryption_reconcile_request_instance.to_dict()
# create an instance of ClusterEncryptionReconcileRequest from a dict
cluster_encryption_reconcile_request_from_dict = ClusterEncryptionReconcileRequest.from_dict(cluster_encryption_reconcile_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


