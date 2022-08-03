# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator 2.3.33.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ComputeInstanceSshSettings(Model):
    """Specifies policy and settings for SSH access.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param ssh_public_access: Access policy for SSH. State of the public SSH
     port. Possible values are: Disabled - Indicates that the public ssh port
     is closed on this instance. Enabled - Indicates that the public ssh port
     is open and accessible according to the VNet/subnet policy if applicable.
     Possible values include: 'Enabled', 'Disabled'. Default value: "Disabled"
     .
    :type ssh_public_access: str or ~_restclient.models.SshPublicAccess
    :ivar admin_user_name: Describes the admin user name.
    :vartype admin_user_name: str
    :ivar ssh_port: Describes the port for connecting through SSH.
    :vartype ssh_port: int
    :param admin_public_key: Specifies the SSH rsa public key file as a
     string. Use "ssh-keygen -t rsa -b 2048" to generate your SSH key pairs.
    :type admin_public_key: str
    """

    _validation = {
        'admin_user_name': {'readonly': True},
        'ssh_port': {'readonly': True},
    }

    _attribute_map = {
        'ssh_public_access': {'key': 'sshPublicAccess', 'type': 'str'},
        'admin_user_name': {'key': 'adminUserName', 'type': 'str'},
        'ssh_port': {'key': 'sshPort', 'type': 'int'},
        'admin_public_key': {'key': 'adminPublicKey', 'type': 'str'},
    }

    def __init__(self, ssh_public_access="Disabled", admin_public_key=None):
        super(ComputeInstanceSshSettings, self).__init__()
        self.ssh_public_access = ssh_public_access
        self.admin_user_name = None
        self.ssh_port = None
        self.admin_public_key = admin_public_key
