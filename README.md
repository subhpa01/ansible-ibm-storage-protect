# Ansible collection for IBM Storage Protect

This collection provides a series of Ansible modules and plugins for interacting with the IBM Storage Protect.  For more information regarding these products, see [IBM Documentation](https://www.ibm.com/docs/en/storage-protect).

## Features

#### Inventory support

- [x] Static inventory file
- [ ] Dynamic inventory file

#### OS support

- [x] Support for RHEL 8 on x86_64

#### IBM Storage Protect Server features

- [ ] Prepare Linux VM for installing IBM Storage Protect Server
- [ ] Verify Linux VM for installing IBM Storage Protect Server
- [ ] Install IBM Storage Protect server on Linux nodes
- [ ] Format the new Storage Protect server instance and DB2 instance
- [ ] Configure DB backup for the IBM Storage Protect server instance
- [ ] Configure Storage Protect server instance to register admin, define storage-pool, policy-domain and register node.
- [ ] Configure Tape library, define tape-pool, policy-doamin, and register node.
- [ ] Start Storage Protect server instance
- [ ] Stop Storage Protect server instance
- [ ] Start Operations Center
- [ ] Stop Operations Center
- [ ] Uninstall IBM Storage Protect server instance
- [ ] Cleanup Linux VM after uninstalling IBM Storage Protect server

#### IBM Storage Protect Client features

- [ ] Prepare Linux VM for installing IBM Storage Protect Client (or B/A Client)
- [ ] Verify Linux VM for installing IBM Storage Protect Client
- [ ] Install IBM Storage Protect Client
- [ ] Configure IBM Storage Protect Client
- [ ] Start IBM Storage Protect Client service
- [ ] Stop IBM Storage Protect Client service
- [ ] Start IBM Storage Protect Client GUI webserver
- [ ] Stop IBM Storage Protect Client GUI webserver
- [ ] Uninstall IBM Storage Protect Client


## Requirements
* Ansible version 2.14 or higher
* Python 3.9 or higher for controller nodes

### Prerequisite
* WORK IN PROGRESS

## Installation
To install the IBM Storage Protect collection hosted in Galaxy:

```
ansible-galaxy collection install ibm.storage_protect
```
To upgrade to the latest version of the IBM Storage Protect collection:
```
ansible-galaxy collection install ibm.storage_protect --force
```

## Usage

### Playbooks
To use a module from the IBM Storage Protect collection, please reference the full namespace, collection name, and module name that you want to use:

```
---
- name: Using the IBM Storage Protect collection
  collections:
    - ibm.storage_protect
  hosts: sp_server_01
  vars:
    - sp_server_servername: server1
    - sp_server_admin_username: admin
    - sp_server_admin_password: sp@easydeploy123
    - sp_server_tcpport: 1500
  pre_tasks:
    - include_vars: sp_vars.yml
  roles:
    - ibm_sp_server_info
```

## Supported Resources

### Modules
* **ibm_sp_server** - Use this module to prepare, install, configure, verify or uninstall an IBM Spectrum Protect server, and/or retrieve information about the SP server.
* **ibm_sp_oc** - Use this module to prepare, install, configure, verify or uninstall an IBM Spectrum Protect Operations Center, and/or retrieve information about the Operations Center.
* **ibm_sp_client** - Use this module to prepare, install, configure, verify or uninstall an IBM Spectrum Protect client (or Backup-Archive client) and/or retrieve information about the BA client.

### Roles
* **ibm_sp_server_prepare** - Use this role to prepare the VM for installing Storage Protect server
* **ibm_sp_server_install** - Use this role to install the Storage Protect server
* **ibm_sp_server_configure** - Use this role to configure the Storage Protect server instance
* **ibm_sp_server_info** - Use this role to get information about the Storage Protect server instance
* **ibm_sp_server_verify** - Use this role to verify the the Storage Protect server instance
* **ibm_sp_server_upgrade** - Use this role to upgrade the Storage Protect server instance
* **ibm_sp_server_uninstall** - Use this role to uninstall the Storage Protect server instance
* **ibm_sp_server_start** - Use this role to start the the Storage Protect server instance
* **ibm_sp_server_stop** - Use this role to stop the the Storage Protect server instance
* **ibm_sp_server_backup** - Use this role to backup the the Storage Protect server instance
* **ibm_sp_server_restore** - Use this role to restore the the Storage Protect server instance
* **ibm_sp_oc_prepare** - Use this role to prepare the VM for installing Storage Protect Operations Center
* **ibm_sp_oc_install** - Use this role to install the Storage Protect Operations Center
* **ibm_sp_oc_configure** - Use this role to configure the Storage Protect Operations Center
* **ibm_sp_oc_info** - Use this role to get information about the Storage Protect Operations Center
* **ibm_sp_oc_verify** - Use this role to verify the the Storage Protect Operations Center
* **ibm_sp_oc_start** - Use this role to start the the Storage Protect Operations Center service
* **ibm_sp_oc_stop** - Use this role to stop the the Storage Protect Operations Center service
* **ibm_sp_oc_upgrade** - Use this role to upgrade the Storage Protect Operations Center
* **ibm_sp_oc_uninstall** - Use this role to uninstall the Storage Protect Operations Center
* **ibm_sp_client_prepare** - Use this role to prepare the VM for installing Storage Protect client or BA Client
* **ibm_sp_client_install** - Use this role to install the Storage Protect client or BA Client
* **ibm_sp_client_configure** - Use this role to configure the Storage Protect client or BA Client
* **ibm_sp_client_info** - Use this role to get information about the Storage Protect client or BA Client
* **ibm_sp_client_verify** - Use this role to verify the the Storage Protect client
* **ibm_sp_client_start** - Use this role to start the the Storage Protect client services
* **ibm_sp_client_stop** - Use this role to stop the the Storage Protect client services
* **ibm_sp_client_upgrade** - Use this role to upgrade the Storage Protect client
* **ibm_sp_client_uninstall** - Use this role to uninstall the Storage Protect client


## Limitation
The modules in the IBM Storage Protect Ansible collection leverage CLIs to connect to the IBM Storage Protect server and client. This has following limitations:

1. WORK IN PROGRESS

## Releasing, Versioning, and Deprecation
* IBM Storage Protect Ansible Collection releases follow a quarterly release cycle.
* IBM Storage Protect Ansible Collection releases follow semantic versioning.
* IBM Storage Protect Ansible modules deprecation cycle is aligned with Ansible.

## Contributing
We welcome contributions to this project, see [CONTRIBUTING.md](./CONTRIBUTING.md) for more details. 


## License
Copyright IBM Corporation, released under the terms of the [Apache License 2.0](./LICENSE).