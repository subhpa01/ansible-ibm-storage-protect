# -*- coding: utf-8 -*-

# Copyright: (c) 2024, Tom page <tpage@redhat.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class ModuleDocFragment(object):

    # IBM Spectrum Protect documentation fragment
    DOCUMENTATION = r'''
options:
  hostname:
    description:
    - URL to your IBM Spectrum Protect instance.
    - If value not set, will try environment variable C(SPECTRUM_PROTECT_HOST)
    - If value not specified by any means, the value of C(127.0.0.1) will be used
    type: str
  username:
    description:
    - Username for your IBM Spectrum Protect instance.
    - If value not set, will try environment variable C(SPECTRUM_PROTECT_USERNAME)
    type: str
  password:
    description:
    - Password for your IBM Spectrum Protect instance.
    - If value not set, will try environment variable C(SPECTRUM_PROTECT_PASSWORD)
    type: str
  validate_certs:
    description:
    - Whether to allow insecure connections to IBM Spectrum Protect.
    - If C(no), SSL certificates will not be validated.
    - This should only be used on personally controlled sites using self-signed certificates.
    - If value not set, will try environment variable C(SPECTRUM_PROTECT_VERIFY_SSL)
    type: bool
  request_timeout:
    description:
    - Specify the timeout Ansible should use in requests to the IBM Spectrum Protect host.
    - Defaults to 10s, but this is handled by the shared module_utils code
    - If value not set, will try environment variable C(SPECTRUM_PROTECT_REQUEST_TIMEOUT)
    type: float
'''
