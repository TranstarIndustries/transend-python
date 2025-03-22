# transend-python
Python Client for the Transend APIs

## Usage
```python

from transend_python import TransendAPIClient



client = TransendAPIClient("your_api_key_here")
sort_types = client.product.get_all_sort_types()
branches = client.branch.get_all_branches()
dtcs = client.vehicle.get_all_dtcs()
print(sort_types, branches, dtcs)
```