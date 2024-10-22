from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.module_utils.basic import AnsibleModule, env_fallback
import subprocess


class StorageProtectModule(AnsibleModule):
    url = None
    AUTH_ARGSPEC = dict(
        server_name=dict(required=False, fallback=(env_fallback, ['SPECTRUM_PROTECT_SERVERNAME'])),
        username=dict(required=False, fallback=(env_fallback, ['SPECTRUM_PROTECT_USERNAME'])),
        password=dict(no_log=True, required=False, fallback=(env_fallback, ['SPECTRUM_PROTECT_PASSWORD'])),
        request_timeout=dict(type='float', required=False, fallback=(env_fallback, ['SPECTRUM_PROTECT_REQUEST_TIMEOUT'])),
    )
    server_name = 'local'
    username = None
    password = None
    validate_certs = True
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

        for param, _ in list(StorageProtectModule.AUTH_ARGSPEC.items()):
            setattr(self, param, self.params.get(param))

    def run_command(self, command, auto_exit=True):
        try:
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if auto_exit and result.returncode == 10:
                self.json_output['changed'] = False
                self.exit_json(**self.json_output)
            if auto_exit and result.returncode == 0:
                self.json_output['changed'] = True
                self.json_output['output'] = result.stdout.decode('utf-8')
                self.exit_json(**self.json_output)
            return result.returncode, result.stdout.decode('utf-8'), None
        except subprocess.CalledProcessError as e:
            if auto_exit and e.returncode == 10:
                self.json_output['changed'] = False
                self.exit_json(**self.json_output)
            return e.returncode, e.stdout.decode('utf-8'), e

    def find_one(self, object_type, name):
        command = (
            f"dsmadmc -server_name={self.server_name} "
            f"-id={self.username} -pass={self.password} -dataonly=yes -comma "
            f"q {object_type} {name} format=detailed"
        )
        rc, out, _ = self.run_command(command, auto_exit=False)
        self.json_output['exists'] = rc == 0
        return rc == 0, out

    def register(self, node, options=None, exists=False, existing=None):
        action = 'update' if exists else 'register'
        command = f"dsmadmc -server_name={self.server_name} -id={self.username} -pass={self.password} {action} node {node} {options}"
        self.json_output['command'] = command
        rc, output, error = self.run_command(command, auto_exit=False)
        if rc != 0 and rc != 10:
            self.fail_json(msg=output, rc=rc, **self.json_output)
        if exists or rc == 10:
            # Check if idempotent
            _, new_node = self.find_one('node', node)
            self.json_output['changed'] = existing != new_node
            self.exit_json(**self.json_output)
        self.json_output['changed'] = True
        self.exit_json(**self.json_output)

    def deregister_node(self, node, options=None, exists=False, existing=None):
        if not exists:
            self.exit_json(**self.json_output)
        command = "dsmadmc -id={username} -pass={password} remove node {node}".format(username=self.username, password=self.password, node=node)
        self.json_output['command'] = command
        _, errmsg, _ = self.run_command(command)
        self.fail_json(msg=errmsg, **self.json_output)
