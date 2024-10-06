#!/usr/bin/python


 ibm.spectrum_protect.configure:
    server: "{{ physical_server }}" 
    instance_fqdn: "{{ tcp_server_address }}"
    port: "{{ admin_port }}"
    username: "{{ username }}"
    password: "{{ password }}"
    state: register

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule

def run_module():
    module_args = dict(
        server=dict(type='str', required=True),
        instance_fqdn=dict(type='str', required=True)
        port=dict(type='str', required=True)
        username=dict(type='str', required=True)
        password=dict(type='str', required=True)
        state=dict(type='str', required=True)
    )

    result = dict(
        changed=False,
        message=''
    )

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    script = module.params['server']
    instance_fqdn = module.params['instance_fqdn']
    port = module.params['port']
    username = module.params['username']
    password = module.params['password']
    state = module.params['state']
    changed = False

    result["changed"] = True
    result["message"] = script

    module.exit_json(**result)

def main():
    run_module()


if __name__ == "__main__":
    main()