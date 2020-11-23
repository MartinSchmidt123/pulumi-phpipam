# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = [
    'GetSubnetsResult',
    'AwaitableGetSubnetsResult',
    'get_subnets',
]

@pulumi.output_type
class GetSubnetsResult:
    """
    A collection of values returned by getSubnets.
    """
    def __init__(__self__, custom_field_filter=None, description=None, description_match=None, id=None, section_id=None, subnet_ids=None):
        if custom_field_filter and not isinstance(custom_field_filter, dict):
            raise TypeError("Expected argument 'custom_field_filter' to be a dict")
        pulumi.set(__self__, "custom_field_filter", custom_field_filter)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if description_match and not isinstance(description_match, str):
            raise TypeError("Expected argument 'description_match' to be a str")
        pulumi.set(__self__, "description_match", description_match)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if section_id and not isinstance(section_id, int):
            raise TypeError("Expected argument 'section_id' to be a int")
        pulumi.set(__self__, "section_id", section_id)
        if subnet_ids and not isinstance(subnet_ids, list):
            raise TypeError("Expected argument 'subnet_ids' to be a list")
        pulumi.set(__self__, "subnet_ids", subnet_ids)

    @property
    @pulumi.getter(name="customFieldFilter")
    def custom_field_filter(self) -> Optional[Mapping[str, Any]]:
        return pulumi.get(self, "custom_field_filter")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="descriptionMatch")
    def description_match(self) -> Optional[str]:
        return pulumi.get(self, "description_match")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="sectionId")
    def section_id(self) -> int:
        return pulumi.get(self, "section_id")

    @property
    @pulumi.getter(name="subnetIds")
    def subnet_ids(self) -> Sequence[int]:
        return pulumi.get(self, "subnet_ids")


class AwaitableGetSubnetsResult(GetSubnetsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSubnetsResult(
            custom_field_filter=self.custom_field_filter,
            description=self.description,
            description_match=self.description_match,
            id=self.id,
            section_id=self.section_id,
            subnet_ids=self.subnet_ids)


def get_subnets(custom_field_filter: Optional[Mapping[str, Any]] = None,
                description: Optional[str] = None,
                description_match: Optional[str] = None,
                section_id: Optional[int] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSubnetsResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['customFieldFilter'] = custom_field_filter
    __args__['description'] = description
    __args__['descriptionMatch'] = description_match
    __args__['sectionId'] = section_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('phpipam:index/getSubnets:getSubnets', __args__, opts=opts, typ=GetSubnetsResult).value

    return AwaitableGetSubnetsResult(
        custom_field_filter=__ret__.custom_field_filter,
        description=__ret__.description,
        description_match=__ret__.description_match,
        id=__ret__.id,
        section_id=__ret__.section_id,
        subnet_ids=__ret__.subnet_ids)
