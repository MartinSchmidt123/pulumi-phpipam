# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['FirstFreeAddress']


class FirstFreeAddress(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 custom_fields: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 device_id: Optional[pulumi.Input[int]] = None,
                 exclude_ping: Optional[pulumi.Input[bool]] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 is_gateway: Optional[pulumi.Input[bool]] = None,
                 mac_address: Optional[pulumi.Input[str]] = None,
                 note: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 ptr_record_id: Optional[pulumi.Input[int]] = None,
                 skip_ptr_record: Optional[pulumi.Input[bool]] = None,
                 state_tag_id: Optional[pulumi.Input[int]] = None,
                 subnet_id: Optional[pulumi.Input[int]] = None,
                 switch_port_label: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Create a FirstFreeAddress resource with the given unique name, props, and options.
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

            __props__['custom_fields'] = custom_fields
            __props__['description'] = description
            __props__['device_id'] = device_id
            __props__['exclude_ping'] = exclude_ping
            __props__['hostname'] = hostname
            __props__['is_gateway'] = is_gateway
            __props__['mac_address'] = mac_address
            __props__['note'] = note
            __props__['owner'] = owner
            __props__['ptr_record_id'] = ptr_record_id
            __props__['skip_ptr_record'] = skip_ptr_record
            __props__['state_tag_id'] = state_tag_id
            if subnet_id is None:
                raise TypeError("Missing required property 'subnet_id'")
            __props__['subnet_id'] = subnet_id
            __props__['switch_port_label'] = switch_port_label
            __props__['address_id'] = None
            __props__['edit_date'] = None
            __props__['ip_address'] = None
            __props__['last_seen'] = None
        super(FirstFreeAddress, __self__).__init__(
            'phpipam:index/firstFreeAddress:FirstFreeAddress',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            address_id: Optional[pulumi.Input[int]] = None,
            custom_fields: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            device_id: Optional[pulumi.Input[int]] = None,
            edit_date: Optional[pulumi.Input[str]] = None,
            exclude_ping: Optional[pulumi.Input[bool]] = None,
            hostname: Optional[pulumi.Input[str]] = None,
            ip_address: Optional[pulumi.Input[str]] = None,
            is_gateway: Optional[pulumi.Input[bool]] = None,
            last_seen: Optional[pulumi.Input[str]] = None,
            mac_address: Optional[pulumi.Input[str]] = None,
            note: Optional[pulumi.Input[str]] = None,
            owner: Optional[pulumi.Input[str]] = None,
            ptr_record_id: Optional[pulumi.Input[int]] = None,
            skip_ptr_record: Optional[pulumi.Input[bool]] = None,
            state_tag_id: Optional[pulumi.Input[int]] = None,
            subnet_id: Optional[pulumi.Input[int]] = None,
            switch_port_label: Optional[pulumi.Input[str]] = None) -> 'FirstFreeAddress':
        """
        Get an existing FirstFreeAddress resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["address_id"] = address_id
        __props__["custom_fields"] = custom_fields
        __props__["description"] = description
        __props__["device_id"] = device_id
        __props__["edit_date"] = edit_date
        __props__["exclude_ping"] = exclude_ping
        __props__["hostname"] = hostname
        __props__["ip_address"] = ip_address
        __props__["is_gateway"] = is_gateway
        __props__["last_seen"] = last_seen
        __props__["mac_address"] = mac_address
        __props__["note"] = note
        __props__["owner"] = owner
        __props__["ptr_record_id"] = ptr_record_id
        __props__["skip_ptr_record"] = skip_ptr_record
        __props__["state_tag_id"] = state_tag_id
        __props__["subnet_id"] = subnet_id
        __props__["switch_port_label"] = switch_port_label
        return FirstFreeAddress(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="addressId")
    def address_id(self) -> pulumi.Output[int]:
        return pulumi.get(self, "address_id")

    @property
    @pulumi.getter(name="customFields")
    def custom_fields(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        return pulumi.get(self, "custom_fields")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="deviceId")
    def device_id(self) -> pulumi.Output[int]:
        return pulumi.get(self, "device_id")

    @property
    @pulumi.getter(name="editDate")
    def edit_date(self) -> pulumi.Output[str]:
        return pulumi.get(self, "edit_date")

    @property
    @pulumi.getter(name="excludePing")
    def exclude_ping(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "exclude_ping")

    @property
    @pulumi.getter
    def hostname(self) -> pulumi.Output[str]:
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> pulumi.Output[str]:
        return pulumi.get(self, "ip_address")

    @property
    @pulumi.getter(name="isGateway")
    def is_gateway(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "is_gateway")

    @property
    @pulumi.getter(name="lastSeen")
    def last_seen(self) -> pulumi.Output[str]:
        return pulumi.get(self, "last_seen")

    @property
    @pulumi.getter(name="macAddress")
    def mac_address(self) -> pulumi.Output[str]:
        return pulumi.get(self, "mac_address")

    @property
    @pulumi.getter
    def note(self) -> pulumi.Output[str]:
        return pulumi.get(self, "note")

    @property
    @pulumi.getter
    def owner(self) -> pulumi.Output[str]:
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter(name="ptrRecordId")
    def ptr_record_id(self) -> pulumi.Output[int]:
        return pulumi.get(self, "ptr_record_id")

    @property
    @pulumi.getter(name="skipPtrRecord")
    def skip_ptr_record(self) -> pulumi.Output[bool]:
        return pulumi.get(self, "skip_ptr_record")

    @property
    @pulumi.getter(name="stateTagId")
    def state_tag_id(self) -> pulumi.Output[int]:
        return pulumi.get(self, "state_tag_id")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[int]:
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter(name="switchPortLabel")
    def switch_port_label(self) -> pulumi.Output[str]:
        return pulumi.get(self, "switch_port_label")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

