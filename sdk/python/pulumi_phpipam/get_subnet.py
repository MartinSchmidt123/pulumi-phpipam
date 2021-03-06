# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = [
    'GetSubnetResult',
    'AwaitableGetSubnetResult',
    'get_subnet',
]

@pulumi.output_type
class GetSubnetResult:
    """
    A collection of values returned by getSubnet.
    """
    def __init__(__self__, allow_ip_requests=None, create_ptr_records=None, custom_field_filter=None, custom_fields=None, description=None, description_match=None, display_hostnames=None, edit_date=None, gateway=None, gateway_id=None, host_discovery_enabled=None, id=None, include_in_ping=None, is_folder=None, is_full=None, linked_subnet_id=None, location_id=None, master_subnet_id=None, nameserver_id=None, parent_subnet_id=None, permissions=None, scan_agent_id=None, section_id=None, show_name=None, subnet_address=None, subnet_id=None, subnet_mask=None, utilization_threshold=None, vlan_id=None, vrf_id=None):
        if allow_ip_requests and not isinstance(allow_ip_requests, bool):
            raise TypeError("Expected argument 'allow_ip_requests' to be a bool")
        pulumi.set(__self__, "allow_ip_requests", allow_ip_requests)
        if create_ptr_records and not isinstance(create_ptr_records, bool):
            raise TypeError("Expected argument 'create_ptr_records' to be a bool")
        pulumi.set(__self__, "create_ptr_records", create_ptr_records)
        if custom_field_filter and not isinstance(custom_field_filter, dict):
            raise TypeError("Expected argument 'custom_field_filter' to be a dict")
        pulumi.set(__self__, "custom_field_filter", custom_field_filter)
        if custom_fields and not isinstance(custom_fields, dict):
            raise TypeError("Expected argument 'custom_fields' to be a dict")
        pulumi.set(__self__, "custom_fields", custom_fields)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if description_match and not isinstance(description_match, str):
            raise TypeError("Expected argument 'description_match' to be a str")
        pulumi.set(__self__, "description_match", description_match)
        if display_hostnames and not isinstance(display_hostnames, bool):
            raise TypeError("Expected argument 'display_hostnames' to be a bool")
        pulumi.set(__self__, "display_hostnames", display_hostnames)
        if edit_date and not isinstance(edit_date, str):
            raise TypeError("Expected argument 'edit_date' to be a str")
        pulumi.set(__self__, "edit_date", edit_date)
        if gateway and not isinstance(gateway, dict):
            raise TypeError("Expected argument 'gateway' to be a dict")
        pulumi.set(__self__, "gateway", gateway)
        if gateway_id and not isinstance(gateway_id, str):
            raise TypeError("Expected argument 'gateway_id' to be a str")
        pulumi.set(__self__, "gateway_id", gateway_id)
        if host_discovery_enabled and not isinstance(host_discovery_enabled, bool):
            raise TypeError("Expected argument 'host_discovery_enabled' to be a bool")
        pulumi.set(__self__, "host_discovery_enabled", host_discovery_enabled)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if include_in_ping and not isinstance(include_in_ping, bool):
            raise TypeError("Expected argument 'include_in_ping' to be a bool")
        pulumi.set(__self__, "include_in_ping", include_in_ping)
        if is_folder and not isinstance(is_folder, bool):
            raise TypeError("Expected argument 'is_folder' to be a bool")
        pulumi.set(__self__, "is_folder", is_folder)
        if is_full and not isinstance(is_full, bool):
            raise TypeError("Expected argument 'is_full' to be a bool")
        pulumi.set(__self__, "is_full", is_full)
        if linked_subnet_id and not isinstance(linked_subnet_id, int):
            raise TypeError("Expected argument 'linked_subnet_id' to be a int")
        pulumi.set(__self__, "linked_subnet_id", linked_subnet_id)
        if location_id and not isinstance(location_id, int):
            raise TypeError("Expected argument 'location_id' to be a int")
        pulumi.set(__self__, "location_id", location_id)
        if master_subnet_id and not isinstance(master_subnet_id, int):
            raise TypeError("Expected argument 'master_subnet_id' to be a int")
        pulumi.set(__self__, "master_subnet_id", master_subnet_id)
        if nameserver_id and not isinstance(nameserver_id, int):
            raise TypeError("Expected argument 'nameserver_id' to be a int")
        pulumi.set(__self__, "nameserver_id", nameserver_id)
        if parent_subnet_id and not isinstance(parent_subnet_id, int):
            raise TypeError("Expected argument 'parent_subnet_id' to be a int")
        pulumi.set(__self__, "parent_subnet_id", parent_subnet_id)
        if permissions and not isinstance(permissions, str):
            raise TypeError("Expected argument 'permissions' to be a str")
        pulumi.set(__self__, "permissions", permissions)
        if scan_agent_id and not isinstance(scan_agent_id, int):
            raise TypeError("Expected argument 'scan_agent_id' to be a int")
        pulumi.set(__self__, "scan_agent_id", scan_agent_id)
        if section_id and not isinstance(section_id, int):
            raise TypeError("Expected argument 'section_id' to be a int")
        pulumi.set(__self__, "section_id", section_id)
        if show_name and not isinstance(show_name, bool):
            raise TypeError("Expected argument 'show_name' to be a bool")
        pulumi.set(__self__, "show_name", show_name)
        if subnet_address and not isinstance(subnet_address, str):
            raise TypeError("Expected argument 'subnet_address' to be a str")
        pulumi.set(__self__, "subnet_address", subnet_address)
        if subnet_id and not isinstance(subnet_id, int):
            raise TypeError("Expected argument 'subnet_id' to be a int")
        pulumi.set(__self__, "subnet_id", subnet_id)
        if subnet_mask and not isinstance(subnet_mask, int):
            raise TypeError("Expected argument 'subnet_mask' to be a int")
        pulumi.set(__self__, "subnet_mask", subnet_mask)
        if utilization_threshold and not isinstance(utilization_threshold, int):
            raise TypeError("Expected argument 'utilization_threshold' to be a int")
        pulumi.set(__self__, "utilization_threshold", utilization_threshold)
        if vlan_id and not isinstance(vlan_id, int):
            raise TypeError("Expected argument 'vlan_id' to be a int")
        pulumi.set(__self__, "vlan_id", vlan_id)
        if vrf_id and not isinstance(vrf_id, int):
            raise TypeError("Expected argument 'vrf_id' to be a int")
        pulumi.set(__self__, "vrf_id", vrf_id)

    @property
    @pulumi.getter(name="allowIpRequests")
    def allow_ip_requests(self) -> bool:
        return pulumi.get(self, "allow_ip_requests")

    @property
    @pulumi.getter(name="createPtrRecords")
    def create_ptr_records(self) -> bool:
        return pulumi.get(self, "create_ptr_records")

    @property
    @pulumi.getter(name="customFieldFilter")
    def custom_field_filter(self) -> Optional[Mapping[str, Any]]:
        return pulumi.get(self, "custom_field_filter")

    @property
    @pulumi.getter(name="customFields")
    def custom_fields(self) -> Mapping[str, Any]:
        return pulumi.get(self, "custom_fields")

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="descriptionMatch")
    def description_match(self) -> Optional[str]:
        return pulumi.get(self, "description_match")

    @property
    @pulumi.getter(name="displayHostnames")
    def display_hostnames(self) -> bool:
        return pulumi.get(self, "display_hostnames")

    @property
    @pulumi.getter(name="editDate")
    def edit_date(self) -> str:
        return pulumi.get(self, "edit_date")

    @property
    @pulumi.getter
    def gateway(self) -> Mapping[str, Any]:
        return pulumi.get(self, "gateway")

    @property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> str:
        return pulumi.get(self, "gateway_id")

    @property
    @pulumi.getter(name="hostDiscoveryEnabled")
    def host_discovery_enabled(self) -> bool:
        return pulumi.get(self, "host_discovery_enabled")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="includeInPing")
    def include_in_ping(self) -> bool:
        return pulumi.get(self, "include_in_ping")

    @property
    @pulumi.getter(name="isFolder")
    def is_folder(self) -> bool:
        return pulumi.get(self, "is_folder")

    @property
    @pulumi.getter(name="isFull")
    def is_full(self) -> bool:
        return pulumi.get(self, "is_full")

    @property
    @pulumi.getter(name="linkedSubnetId")
    def linked_subnet_id(self) -> int:
        return pulumi.get(self, "linked_subnet_id")

    @property
    @pulumi.getter(name="locationId")
    def location_id(self) -> int:
        return pulumi.get(self, "location_id")

    @property
    @pulumi.getter(name="masterSubnetId")
    def master_subnet_id(self) -> int:
        return pulumi.get(self, "master_subnet_id")

    @property
    @pulumi.getter(name="nameserverId")
    def nameserver_id(self) -> int:
        return pulumi.get(self, "nameserver_id")

    @property
    @pulumi.getter(name="parentSubnetId")
    def parent_subnet_id(self) -> int:
        return pulumi.get(self, "parent_subnet_id")

    @property
    @pulumi.getter
    def permissions(self) -> str:
        return pulumi.get(self, "permissions")

    @property
    @pulumi.getter(name="scanAgentId")
    def scan_agent_id(self) -> int:
        return pulumi.get(self, "scan_agent_id")

    @property
    @pulumi.getter(name="sectionId")
    def section_id(self) -> int:
        return pulumi.get(self, "section_id")

    @property
    @pulumi.getter(name="showName")
    def show_name(self) -> bool:
        return pulumi.get(self, "show_name")

    @property
    @pulumi.getter(name="subnetAddress")
    def subnet_address(self) -> str:
        return pulumi.get(self, "subnet_address")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> int:
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter(name="subnetMask")
    def subnet_mask(self) -> int:
        return pulumi.get(self, "subnet_mask")

    @property
    @pulumi.getter(name="utilizationThreshold")
    def utilization_threshold(self) -> int:
        return pulumi.get(self, "utilization_threshold")

    @property
    @pulumi.getter(name="vlanId")
    def vlan_id(self) -> int:
        return pulumi.get(self, "vlan_id")

    @property
    @pulumi.getter(name="vrfId")
    def vrf_id(self) -> int:
        return pulumi.get(self, "vrf_id")


class AwaitableGetSubnetResult(GetSubnetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSubnetResult(
            allow_ip_requests=self.allow_ip_requests,
            create_ptr_records=self.create_ptr_records,
            custom_field_filter=self.custom_field_filter,
            custom_fields=self.custom_fields,
            description=self.description,
            description_match=self.description_match,
            display_hostnames=self.display_hostnames,
            edit_date=self.edit_date,
            gateway=self.gateway,
            gateway_id=self.gateway_id,
            host_discovery_enabled=self.host_discovery_enabled,
            id=self.id,
            include_in_ping=self.include_in_ping,
            is_folder=self.is_folder,
            is_full=self.is_full,
            linked_subnet_id=self.linked_subnet_id,
            location_id=self.location_id,
            master_subnet_id=self.master_subnet_id,
            nameserver_id=self.nameserver_id,
            parent_subnet_id=self.parent_subnet_id,
            permissions=self.permissions,
            scan_agent_id=self.scan_agent_id,
            section_id=self.section_id,
            show_name=self.show_name,
            subnet_address=self.subnet_address,
            subnet_id=self.subnet_id,
            subnet_mask=self.subnet_mask,
            utilization_threshold=self.utilization_threshold,
            vlan_id=self.vlan_id,
            vrf_id=self.vrf_id)


def get_subnet(custom_field_filter: Optional[Mapping[str, Any]] = None,
               description: Optional[str] = None,
               description_match: Optional[str] = None,
               section_id: Optional[int] = None,
               subnet_address: Optional[str] = None,
               subnet_id: Optional[int] = None,
               subnet_mask: Optional[int] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSubnetResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['customFieldFilter'] = custom_field_filter
    __args__['description'] = description
    __args__['descriptionMatch'] = description_match
    __args__['sectionId'] = section_id
    __args__['subnetAddress'] = subnet_address
    __args__['subnetId'] = subnet_id
    __args__['subnetMask'] = subnet_mask
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('phpipam:index/getSubnet:getSubnet', __args__, opts=opts, typ=GetSubnetResult).value

    return AwaitableGetSubnetResult(
        allow_ip_requests=__ret__.allow_ip_requests,
        create_ptr_records=__ret__.create_ptr_records,
        custom_field_filter=__ret__.custom_field_filter,
        custom_fields=__ret__.custom_fields,
        description=__ret__.description,
        description_match=__ret__.description_match,
        display_hostnames=__ret__.display_hostnames,
        edit_date=__ret__.edit_date,
        gateway=__ret__.gateway,
        gateway_id=__ret__.gateway_id,
        host_discovery_enabled=__ret__.host_discovery_enabled,
        id=__ret__.id,
        include_in_ping=__ret__.include_in_ping,
        is_folder=__ret__.is_folder,
        is_full=__ret__.is_full,
        linked_subnet_id=__ret__.linked_subnet_id,
        location_id=__ret__.location_id,
        master_subnet_id=__ret__.master_subnet_id,
        nameserver_id=__ret__.nameserver_id,
        parent_subnet_id=__ret__.parent_subnet_id,
        permissions=__ret__.permissions,
        scan_agent_id=__ret__.scan_agent_id,
        section_id=__ret__.section_id,
        show_name=__ret__.show_name,
        subnet_address=__ret__.subnet_address,
        subnet_id=__ret__.subnet_id,
        subnet_mask=__ret__.subnet_mask,
        utilization_threshold=__ret__.utilization_threshold,
        vlan_id=__ret__.vlan_id,
        vrf_id=__ret__.vrf_id)
