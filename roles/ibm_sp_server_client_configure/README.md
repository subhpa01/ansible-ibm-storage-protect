# ibm_sp_server_client_configure

Configure Storage Protect server with client nodes - for the following:
* register the clients
* configure the clients - backup schedules,
* configure the policy for the clients - policy-domain, policy-set, management-class


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
    - name: Register clients to the Storage Protect server, and configure policies
      include_role:
        name: ibm_sp_server_client_configure
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
