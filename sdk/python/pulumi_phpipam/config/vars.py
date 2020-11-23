# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = [
    'app_id',
    'endpoint',
    'insecure',
    'password',
    'username',
]

__config__ = pulumi.Config('phpipam')

app_id = __config__.get('appId')
"""
The application ID required for API requests
"""

endpoint = __config__.get('endpoint')
"""
The full URL (plus path) to the API endpoint
"""

insecure = __config__.get('insecure')
"""
Whether server should be accessed without verifying the TLS certificate.
"""

password = __config__.get('password')
"""
The password of the PHPIPAM account
"""

username = __config__.get('username')
"""
The username of the PHPIPAM account
"""
