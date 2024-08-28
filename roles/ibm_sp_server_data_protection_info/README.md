# ibm_sp_server_data_protection_info

Get information about the data protection settings made the Storage Protect server and clients. It includes the following for 
* data deduplication settings, 
* data replication settings, 
* data copy settings, 
* data tiering settings, 
* data retention settings.


## Role Variables

| Variable              | Type          | Description                                                            |
|-----------------------|---------------|------------------------------------------------------------------------|
|                       |               |                                                                        |


## Return Variables

| Variable              | Type          | Description                                                       |
|-----------------------|---------------|-------------------------------------------------------------------|
| sp_server_data_dedup_info | list      |                                                                   |
| sp_server_data_replication_info | list |                                                                  |
| sp_server_data_copy_info | list       |                                                                   |
| sp_server_data_tiering_info | list    |                                                                   |
| sp_server_data_retention_info | list  |                                                                   |

## Example Playbook

```
- name: 
  hosts: testhost

  vars:
    

  tasks:
    - name: Get information about the data protection settings
      include_role:
        name: ibm_sp_server_data_protection_info
```


## Example Returned Variables

```
"sp_server_data_dedup_info": [
        {
          
        }
    ]
"sp_server_data_replication_info": [
        {
          
        }
    ]
"sp_server_data_copy_info": [
        {
          
        }
    ]
"sp_server_data_tiering_info": [
        {
          
        }
    ]
"sp_server_data_retention_info": [
        {
          
        }
    ]

```

## License

[Apache-2.0](../../LICENSE)
