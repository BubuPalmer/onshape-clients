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

import { BTConnection } from './bTConnection';

export class BTGraphicsAppearance {
    'nonTrivial'?: boolean;
    'reset'?: boolean;
    'color'?: Array<string>;
    'opacity'?: number;
    'typeId'?: number;
    'exportTypeName'?: string;
    'connectionSource'?: BTConnection;
    'unknownClass'?: boolean;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "nonTrivial",
            "baseName": "nonTrivial",
            "type": "boolean"
        },
        {
            "name": "reset",
            "baseName": "reset",
            "type": "boolean"
        },
        {
            "name": "color",
            "baseName": "color",
            "type": "Array<string>"
        },
        {
            "name": "opacity",
            "baseName": "opacity",
            "type": "number"
        },
        {
            "name": "typeId",
            "baseName": "typeId",
            "type": "number"
        },
        {
            "name": "exportTypeName",
            "baseName": "exportTypeName",
            "type": "string"
        },
        {
            "name": "connectionSource",
            "baseName": "connectionSource",
            "type": "BTConnection"
        },
        {
            "name": "unknownClass",
            "baseName": "unknownClass",
            "type": "boolean"
        }    ];

    static getAttributeTypeMap() {
        return BTGraphicsAppearance.attributeTypeMap;
    }
}

