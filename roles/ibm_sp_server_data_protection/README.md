# ibm_sp_server_data_protection

Configure the Storage Protect server for 
* configure data deduplication, 
* configure data replication, 
* configure data copy, 
* configure data tiering, 
* configure data retention.


## Role Variables

| Variable              | Type          | Description                                                            |
|-----------------------|---------------|------------------------------------------------------------------------|
|                       |               |                                                                        |


## Return Variables

| Variable              | Type          | Description                                                       |
|-----------------------|---------------|-------------------------------------------------------------------|
| sp_server_data_copy   | list          |                                                                   |
| sp_server_data_tiering | list         |                                                                   |
| sp_server_data_retention_set | list   |                                                                   |

## Example Playbook

```
- name: 
  hosts: testhost

  vars:
    

  tasks:
    - name: Configure the Storage Protect server with data-copy, data-tiering & retention settings
      include_role:
        name: ibm_sp_server_data_protection
```


## Example Returned Variables

```
"sp_server_data_copy": [
        {
          
        }
    ]
"sp_server_data_tiering": [
        {
          
        }
    ]
"sp_server_data_retention_set": [
        {
          
        }
    ]

```

## License

[Apache-2.0](../../LICENSE)
