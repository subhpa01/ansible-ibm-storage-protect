#!/usr/bin/python
# coding: utf-8 -*-

# (c) 2024,Tom page <tpage@redhat.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# ibm.spectrum_protect.register:
#    server: "{{ physical_server }}"
#    url: "{{ tcp_server_address }}"
#    username: "{{ username }}"
#    password: "{{ password }}"
#    state: present

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1', 'status': ['preview'], 'supported_by': 'community'}


DOCUMENTATION = '''
---
module: register
author: "Tom page (@Tompage1994)"
short_description: Register or Deregister a server from IBM Spectrum Protect
description:
    - Register or Deregister a server from IBM Spectrum Protect
options:
    server:
      description:
        - The Server to register or deregister
      required: True
      type: str
      aliases:
        - name
    state:
      description:
        - Desired state of the registration.
        - 'present' and 'registered' have the same effect.
        - 'absent' and 'deregistered' have the same effect.
      default: "registered"
      choices: ["present", "absent", "registered", "deregistered"]
      type: str

extends_documentation_fragment: ibm.spectrum_protect.auth
'''


EXAMPLES = '''
- name: Register server
  ibm.spectrum_protect.register:
   server: "{{ physical_server }}"
   url: "{{ tcp_server_address }}"
   username: "{{ username }}"
   password: "{{ password }}"
   state: registered

- name: Deregister server
  ibm.spectrum_protect.register:
   server: "{{ physical_server }}" 
   url: "{{ tcp_server_address }}"
   username: "{{ username }}"
   password: "{{ password }}"
   state: deregistered
'''

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
