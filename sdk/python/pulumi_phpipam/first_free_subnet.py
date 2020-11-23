# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['FirstFreeSubnet']


class FirstFreeSubnet(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_ip_requests: Optional[pulumi.Input[bool]] = None,
                 create_ptr_records: Optional[pulumi.Input[bool]] = None,
                 custom_fields: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_hostnames: Optional[pulumi.Input[bool]] = None,
                 include_in_ping: Optional[pulumi.Input[bool]] = None,
                 is_full: Optional[pulumi.Input[bool]] = None,
                 linked_subnet_id: Optional[pulumi.Input[int]] = None,
                 master_subnet_id: Optional[pulumi.Input[int]] = None,
                 nameserver_id: Optional[pulumi.Input[int]] = None,
                 parent_subnet_id: Optional[pulumi.Input[int]] = None,
                 scan_agent_id: Optional[pulumi.Input[int]] = None,
                 show_name: Optional[pulumi.Input[bool]] = None,
                 subnet_mask: Optional[pulumi.Input[int]] = None,
                 utilization_threshold: Optional[pulumi.Input[int]] = None,
                 vlan_id: Optional[pulumi.Input[int]] = None,
                 vrf_id: Optional[pulumi.Input[int]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Create a FirstFreeSubnet resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['allow_ip_requests'] = allow_ip_requests
            __props__['create_ptr_records'] = create_ptr_records
            __props__['custom_fields'] = custom_fields
            __props__['description'] = description
            __props__['display_hostnames'] = display_hostnames
            __props__['include_in_ping'] = include_in_ping
            __props__['is_full'] = is_full
            __props__['linked_subnet_id'] = linked_subnet_id
            __props__['master_subnet_id'] = master_subnet_id
            __props__['nameserver_id'] = nameserver_id
            if parent_subnet_id is None:
                raise TypeError("Missing required property 'parent_subnet_id'")
            __props__['parent_subnet_id'] = parent_subnet_id
            __props__['scan_agent_id'] = scan_agent_id
            __props__['show_name'] = show_name
            if subnet_mask is None:
                raise TypeError("Missing required property 'subnet_mask'")
            __props__['subnet_mask'] = subnet_mask
            __props__['utilization_threshold'] = utilization_threshold
            __props__['vlan_id'] = vlan_id
            __props__['vrf_id'] = vrf_id
            __props__['edit_date'] = None
            __props__['gateway'] = None
            __props__['gateway_id'] = None
            __props__['host_discovery_enabled'] = None
            __props__['is_folder'] = None
            __props__['location_id'] = None
            __props__['permissions'] = None
            __props__['section_id'] = None
            __props__['subnet_address'] = None
            __props__['subnet_id'] = None
        super(FirstFreeSubnet, __self__).__init__(
            'phpipam:index/firstFreeSubnet:FirstFreeSubnet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            allow_ip_requests: Optional[pulumi.Input[bool]] = None,
            create_ptr_records: Optional[pulumi.Input[bool]] = None,
            custom_fields: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            display_hostnames: Optional[pulumi.Input[bool]] = None,
            edit_date: Optional[pulumi.Input[str]] = None,
            gateway: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            gateway_id: Optional[pulumi.Input[str]] = None,
            host_discovery_enabled: Optional[pulumi.Input[bool]] = None,
            include_in_ping: Optional[pulumi.Input[bool]] = None,
            is_folder: Optional[pulumi.Input[bool]] = None,
            is_full: Optional[pulumi.Input[bool]] = None,
            linked_subnet_id: Optional[pulumi.Input[int]] = None,
            location_id: Optional[pulumi.Input[int]] = None,
            master_subnet_id: Optional[pulumi.Input[int]] = None,
            nameserver_id: Optional[pulumi.Input[int]] = None,
            parent_subnet_id: Optional[pulumi.Input[int]] = None,
            permissions: Optional[pulumi.Input[str]] = None,
            scan_agent_id: Optional[pulumi.Input[int]] = None,
            section_id: Optional[pulumi.Input[int]] = None,
            show_name: Optional[pulumi.Input[bool]] = None,
            subnet_address: Optional[pulumi.Input[str]] = None,
            subnet_id: Optional[pulumi.Input[int]] = None,
            subnet_mask: Optional[pulumi.Input[int]] = None,
            utilization_threshold: Optional[pulumi.Input[int]] = None,
            vlan_id: Optional[pulumi.Input[int]] = None,
            vrf_id: Optional[pulumi.Input[int]] = None) -> 'FirstFreeSubnet':
        """
        Get an existing FirstFreeSubnet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["allow_ip_requests"] = allow_ip_requests
        __props__["create_ptr_records"] = create_ptr_records
        __props__["custom_fields"] = custom_fields
        __props__["description"] = description
        __props__["display_hostnames"] = display_hostnames
        __props__["edit_date"] = edit_date
        __props__["gateway"] = gateway
        __props__["gateway_id"] = gateway_id
        __props__["host_discovery_enabled"] = host_discovery_enabled
        __props__["include_in_ping"] = include_in_ping
        __props__["is_folder"] = is_folder
        __props__["is_full"] = is_full
        __props__["linked_subnet_id"] = linked_subnet_id
        __props__["location_id"] = location_id
        __props__["master_subnet_id"] = master_subnet_id
        __props__["nameserver_id"] = nameserver_id
        __props__["parent_subnet_id"] = parent_subnet_id
        __props__["permissions"] = permissions
        __props__["scan_agent_id"] = scan_agent_id
        __props__["section_id"] = section_id
        __props__["show_name"] = show_name
        __props__["subnet_address"] = subnet_address
        __props__["subnet_id"] = subnet_id
        __props__["subnet_mask"] = subnet_mask
        __props__["utilization_threshold"] = utilization_threshold
        __props__["vlan_id"] = vlan_id
        __props__["vrf_id"] = vrf_id
        return FirstFreeSubnet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allowIpRequests")
    def allow_ip_requests(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "allow_ip_requests")

    @property
    @pulumi.getter(name="createPtrRecords")
    def create_ptr_records(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "create_ptr_records")

    @property
    @pulumi.getter(name="customFields")
    def custom_fields(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        return pulumi.get(self, "custom_fields")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayHostnames")
    def display_hostnames(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "display_hostnames")

    @property
    @pulumi.getter(name="editDate")
    def edit_date(self) -> pulumi.Output[str]:
        return pulumi.get(self, "edit_date")

    @property
    @pulumi.getter
    def gateway(self) -> pulumi.Output[Mapping[str, Any]]:
        return pulumi.get(self, "gateway")

    @property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "gateway_id")

    @property
    @pulumi.getter(name="hostDiscoveryEnabled")
    def host_discovery_enabled(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "host_discovery_enabled")

    @property
    @pulumi.getter(name="includeInPing")
    def include_in_ping(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "include_in_ping")

    @property
    @pulumi.getter(name="isFolder")
    def is_folder(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "is_folder")

    @property
    @pulumi.getter(name="isFull")
    def is_full(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "is_full")

    @property
    @pulumi.getter(name="linkedSubnetId")
    def linked_subnet_id(self) -> pulumi.Output[int]:
        return pulumi.get(self, "linked_subnet_id")

    @property
    @pulumi.getter(name="locationId")
    def location_id(self) -> pulumi.Output[int]:
        return pulumi.get(self, "location_id")

    @property
    @pulumi.getter(name="masterSubnetId")
    def master_subnet_id(self) -> pulumi.Output[int]:
        return pulumi.get(self, "master_subnet_id")

    @property
    @pulumi.getter(name="nameserverId")
    def nameserver_id(self) -> pulumi.Output[int]:
        return pulumi.get(self, "nameserver_id")

    @property
    @pulumi.getter(name="parentSubnetId")
    def parent_subnet_id(self) -> pulumi.Output[int]:
        return pulumi.get(self, "parent_subnet_id")

    @property
    @pulumi.getter
    def permissions(self) -> pulumi.Output[str]:
        return pulumi.get(self, "permissions")

    @property
    @pulumi.getter(name="scanAgentId")
    def scan_agent_id(self) -> pulumi.Output[int]:
        return pulumi.get(self, "scan_agent_id")

    @property
    @pulumi.getter(name="sectionId")
    def section_id(self) -> pulumi.Output[int]:
        return pulumi.get(self, "section_id")

    @property
    @pulumi.getter(name="showName")
    def show_name(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "show_name")

    @property
    @pulumi.getter(name="subnetAddress")
    def subnet_address(self) -> pulumi.Output[str]:
        return pulumi.get(self, "subnet_address")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[int]:
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter(name="subnetMask")
    def subnet_mask(self) -> pulumi.Output[int]:
        return pulumi.get(self, "subnet_mask")

    @property
    @pulumi.getter(name="utilizationThreshold")
    def utilization_threshold(self) -> pulumi.Output[int]:
        return pulumi.get(self, "utilization_threshold")

    @property
    @pulumi.getter(name="vlanId")
    def vlan_id(self) -> pulumi.Output[int]:
        return pulumi.get(self, "vlan_id")

    @property
    @pulumi.getter(name="vrfId")
    def vrf_id(self) -> pulumi.Output[int]:
        return pulumi.get(self, "vrf_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

