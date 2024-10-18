from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule, env_fallback
from ansible.module_utils.urls import Request, SSLValidationError, ConnectionError
from ansible.module_utils.parsing.convert_bool import boolean as strtobool
from ansible.module_utils.six import PY2
from ansible.module_utils.six import raise_from, string_types
from ansible.module_utils.six.moves import StringIO
from ansible.module_utils.six.moves.urllib.error import HTTPError
from ansible.module_utils.six.moves.http_cookiejar import CookieJar
from ansible.module_utils.six.moves.urllib.parse import urlparse, urlencode, quote
from ansible.module_utils.six.moves.configparser import ConfigParser, NoOptionError
from socket import getaddrinfo, IPPROTO_TCP
import time
import re
import subprocess
from json import loads, dumps
from os.path import isfile, expanduser, split, join, exists, isdir
from os import access, R_OK, getcwd, environ
try:
    from ansible.module_utils.compat.version import LooseVersion as Version
except ImportError:
    try:
        from distutils.version import LooseVersion as Version
    except ImportError:
        raise AssertionError('To use this plugin or module with ansible-core 2.11, you need to use Python < 3.12 with distutils.version present')

try:
    import yaml

    HAS_YAML = True
except ImportError:
    HAS_YAML = False

class StorageProtectModule(AnsibleModule):
    url = None
    AUTH_ARGSPEC = dict(
        hostname=dict(required=False, fallback=(env_fallback, ['SPECTRUM_PROTECT_HOST'])),
        username=dict(required=False, fallback=(env_fallback, ['SPECTRUM_PROTECT_USERNAME'])),
        password=dict(no_log=True, required=False, fallback=(env_fallback, ['SPECTRUM_PROTECT_PASSWORD'])),
        validate_certs=dict(type='bool', aliases=['tower_verify_ssl'], required=False, fallback=(env_fallback, ['SPECTRUM_PROTECT_VERIFY_SSL'])),
        request_timeout=dict(type='float', required=False, fallback=(env_fallback, ['SPECTRUM_PROTECT_REQUEST_TIMEOUT'])),
    )
    hostname = '127.0.0.1'
    username = None
    password = None
    verify_ssl = True
    request_timeout = 10
    authenticated = False
    version_checked = False
    error_callback = None
    warn_callback = None

    def __init__(self, argument_spec=None, direct_params=None, error_callback=None, warn_callback=None, **kwargs):
        full_argspec = {}
        full_argspec.update(StorageProtectModule.AUTH_ARGSPEC)
        full_argspec.update(argument_spec)
        kwargs['supports_check_mode'] = True

        self.error_callback = error_callback
        self.warn_callback = warn_callback

        self.json_output = {'changed': False}

        if direct_params is not None:
            self.params = direct_params
        else:
            super().__init__(argument_spec=full_argspec, **kwargs)

    def run_command(self, command):
        try:
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return result.stdout.decode('utf-8'), None
        except subprocess.CalledProcessError as e:
            return None, e.stderr.decode('utf-8')

    # TODO - This will get split out into more common pieces but for now lets get it working for the register
    def register(self, server):
        # home = os.environ ['HOME']
        # gsk = '/usr/bin/gsk8capicmd_64'
        # kdb = '{home}/IBM/SpectrumProtect/certs/dsmcert.kdb'.format(home=home)
        # label = f*'TSM server (name) self-signed key'
        # fn = f'(home)/IBM/SpectrumProtect/certs/[name}.txt'
        # (gsk) -cert -delete -db (kdb} -stashed -label flabel)
        # (gsk)-cert -add -db (kdb) -stashed -label (labelf-file {fn) -format ascil
        # (gsk) -cert -list -db (kdb) -stashed
        command = "dsmadmc -se={hostname} -id={username} -pass={password} register node {server}".format(hostname=self.hostname, username=self.username, password=self.password, server=server)
        output, error = self.run_command(command)
        if error:
            #  Check if its an idempotency error, in which case contine and mark {changed: false}
            if error == "already exists":
                self.json_output['changed'] = False
                self.exit_json(**self.json_output)
            else:
                self.fail_json(msg=error)
        self.json_output['changed'] = True
        self.exit_json(**self.json_output)