// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export function getSubnets(args: GetSubnetsArgs, opts?: pulumi.InvokeOptions): Promise<GetSubnetsResult> {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("phpipam:index/getSubnets:getSubnets", {
        "customFieldFilter": args.customFieldFilter,
        "description": args.description,
        "descriptionMatch": args.descriptionMatch,
        "sectionId": args.sectionId,
    }, opts);
}

/**
 * A collection of arguments for invoking getSubnets.
 */
export interface GetSubnetsArgs {
    readonly customFieldFilter?: {[key: string]: any};
    readonly description?: string;
    readonly descriptionMatch?: string;
    readonly sectionId: number;
}

/**
 * A collection of values returned by getSubnets.
 */
export interface GetSubnetsResult {
    readonly customFieldFilter?: {[key: string]: any};
    readonly description?: string;
    readonly descriptionMatch?: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly sectionId: number;
    readonly subnetIds: number[];
}
