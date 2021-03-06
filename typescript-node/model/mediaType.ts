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

import { Encoding } from './encoding';
import { Example } from './example';
import { Schema } from './schema';

export class MediaType {
    'schema'?: Schema;
    'examples'?: { [key: string]: Example; };
    'example'?: any;
    'encoding'?: { [key: string]: Encoding; };
    'extensions'?: { [key: string]: any; };

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "schema",
            "baseName": "schema",
            "type": "Schema"
        },
        {
            "name": "examples",
            "baseName": "examples",
            "type": "{ [key: string]: Example; }"
        },
        {
            "name": "example",
            "baseName": "example",
            "type": "any"
        },
        {
            "name": "encoding",
            "baseName": "encoding",
            "type": "{ [key: string]: Encoding; }"
        },
        {
            "name": "extensions",
            "baseName": "extensions",
            "type": "{ [key: string]: any; }"
        }    ];

    static getAttributeTypeMap() {
        return MediaType.attributeTypeMap;
    }
}

