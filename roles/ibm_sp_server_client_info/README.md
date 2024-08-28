# ibm_sp_server_client_info

Get information about the client nodes registered with the Storage Protect server, along with the following:
* backup schedules,
* policy details (policy-domain, policy-set, management-class)

## Role Variables

| Variable              | Type          | Description                                                            |
|-----------------------|---------------|------------------------------------------------------------------------|
|                       |               |                                                                        |


## Return Variables

| Variable              | Type          | Description                                                       |
|-----------------------|---------------|-------------------------------------------------------------------|
| sp_server_client_info | list          |                                                                   |
| sp_server_client_schedule | list      |                                                                   |
| sp_server_client_policy  | list       |                                                                   |


## Example Playbook

```
- name: 
  hosts: testhost

  vars:
    

  tasks:
    - name: Get information about the clients registered to the Storage Protect server, its schedule, and policies
      include_role:
        name: ibm_sp_server_client_info
```


## Example Returned Variables

```
"sp_server_client_info": [
        {
            "key-1": "val-1",
            "key-2": "val-2"
        }
    ]
"sp_server_client_schedule": [
        {
            "key-1": "val-1",
            "key-2": "val-2"
        }
    ]
"sp_server_client_policy": [
        {
            "key-1": "val-1",
            "key-2": "val-2"
        }
    ]
```

## License

[Apache-2.0](../../LICENSE)
