# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = [
    'GetVlanResult',
    'AwaitableGetVlanResult',
    'get_vlan',
]

@pulumi.output_type
class GetVlanResult:
    """
    A collection of values returned by getVlan.
    """
    def __init__(__self__, custom_fields=None, description=None, edit_date=None, id=None, l2_domain_id=None, name=None, number=None, vlan_id=None):
        if custom_fields and not isinstance(custom_fields, dict):
            raise TypeError("Expected argument 'custom_fields' to be a dict")
        pulumi.set(__self__, "custom_fields", custom_fields)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if edit_date and not isinstance(edit_date, str):
            raise TypeError("Expected argument 'edit_date' to be a str")
        pulumi.set(__self__, "edit_date", edit_date)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if l2_domain_id and not isinstance(l2_domain_id, int):
            raise TypeError("Expected argument 'l2_domain_id' to be a int")
        pulumi.set(__self__, "l2_domain_id", l2_domain_id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if number and not isinstance(number, int):
            raise TypeError("Expected argument 'number' to be a int")
        pulumi.set(__self__, "number", number)
        if vlan_id and not isinstance(vlan_id, int):
            raise TypeError("Expected argument 'vlan_id' to be a int")
        pulumi.set(__self__, "vlan_id", vlan_id)

    @property
    @pulumi.getter(name="customFields")
    def custom_fields(self) -> Mapping[str, Any]:
        return pulumi.get(self, "custom_fields")

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="editDate")
    def edit_date(self) -> str:
        return pulumi.get(self, "edit_date")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="l2DomainId")
    def l2_domain_id(self) -> int:
        return pulumi.get(self, "l2_domain_id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def number(self) -> int:
        return pulumi.get(self, "number")

    @property
    @pulumi.getter(name="vlanId")
    def vlan_id(self) -> int:
        return pulumi.get(self, "vlan_id")


class AwaitableGetVlanResult(GetVlanResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVlanResult(
            custom_fields=self.custom_fields,
            description=self.description,
            edit_date=self.edit_date,
            id=self.id,
            l2_domain_id=self.l2_domain_id,
            name=self.name,
            number=self.number,
            vlan_id=self.vlan_id)


def get_vlan(number: Optional[int] = None,
             vlan_id: Optional[int] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVlanResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['number'] = number
    __args__['vlanId'] = vlan_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('phpipam:index/getVlan:getVlan', __args__, opts=opts, typ=GetVlanResult).value

    return AwaitableGetVlanResult(
        custom_fields=__ret__.custom_fields,
        description=__ret__.description,
        edit_date=__ret__.edit_date,
        id=__ret__.id,
        l2_domain_id=__ret__.l2_domain_id,
        name=__ret__.name,
        number=__ret__.number,
        vlan_id=__ret__.vlan_id)
