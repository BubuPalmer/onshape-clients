/**
 * Onshape REST API
 * The Onshape REST API consumed by all clients.
 *
 * OpenAPI spec version: 1.93
 * Contact: api-support@onshape.zendesk.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { BTReleasePackageItemParams } from './bTReleasePackageItemParams';

export class BTReleasePackageParams {
    'items'?: Array<BTReleasePackageItemParams>;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "items",
            "baseName": "items",
            "type": "Array<BTReleasePackageItemParams>"
        }    ];

    static getAttributeTypeMap() {
        return BTReleasePackageParams.attributeTypeMap;
    }
}

