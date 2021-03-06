// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export function getSection(args?: GetSectionArgs, opts?: pulumi.InvokeOptions): Promise<GetSectionResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("phpipam:index/getSection:getSection", {
        "name": args.name,
        "sectionId": args.sectionId,
    }, opts);
}

/**
 * A collection of arguments for invoking getSection.
 */
export interface GetSectionArgs {
    readonly name?: string;
    readonly sectionId?: number;
}

/**
 * A collection of values returned by getSection.
 */
export interface GetSectionResult {
    readonly description: string;
    readonly displayOrder: number;
    readonly dnsResolverId: number;
    readonly editDate: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly masterSectionId: number;
    readonly name: string;
    readonly permissions: string;
    readonly sectionId: number;
    readonly showSupernetOnly: boolean;
    readonly showVlanInSubnetListing: boolean;
    readonly showVrfInSubnetListing: boolean;
    readonly strictMode: boolean;
    readonly subnetOrdering: string;
}
