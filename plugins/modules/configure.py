#!/usr/bin/python


# ibm.spectrum_protect.register:
#    server: "{{ physical_server }}" 
#    url: "{{ tcp_server_address }}"
#    username: "{{ username }}"
#    password: "{{ password }}"
#    state: present

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ..module_utils.storage_protect_api import StorageProtectModule

def main():
    argument_spec = dict(
        server=dict(required=True, aliases=['name']),
        state=dict(choices=['present', 'absent', 'registered', 'deregistered'], default='present'),
    )

    module = StorageProtectModule(argument_spec=argument_spec, supports_check_mode=True)

    state = module.params.get('state')

    if state == 'absent' or state == 'deregistered':
        # Deregister(server)
    else:
        # Register(server)


if __name__ == "__main__":
    main()
