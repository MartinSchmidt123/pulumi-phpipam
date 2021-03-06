// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export function getAddresses(args: GetAddressesArgs, opts?: pulumi.InvokeOptions): Promise<GetAddressesResult> {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("phpipam:index/getAddresses:getAddresses", {
        "customFieldFilter": args.customFieldFilter,
        "description": args.description,
        "hostname": args.hostname,
        "subnetId": args.subnetId,
    }, opts);
}

/**
 * A collection of arguments for invoking getAddresses.
 */
export interface GetAddressesArgs {
    readonly customFieldFilter?: {[key: string]: any};
    readonly description?: string;
    readonly hostname?: string;
    readonly subnetId: number;
}

/**
 * A collection of values returned by getAddresses.
 */
export interface GetAddressesResult {
    readonly addressIds: number[];
    readonly customFieldFilter?: {[key: string]: any};
    readonly description?: string;
    readonly hostname?: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly subnetId: number;
}
