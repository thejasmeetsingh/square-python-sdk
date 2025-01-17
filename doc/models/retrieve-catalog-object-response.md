
# Retrieve Catalog Object Response

## Structure

`Retrieve Catalog Object Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List Error`](../../doc/models/error.md) | Optional | Any errors that occurred during the request. |
| `object` | [`Catalog Object`](../../doc/models/catalog-object.md) | Optional | The wrapper object for the catalog entries of a given object type.<br><br>Depending on the `type` attribute value, a `CatalogObject` instance assumes a type-specific data to yield the corresponding type of catalog object.<br><br>For example, if `type=ITEM`, the `CatalogObject` instance must have the ITEM-specific data set on the `item_data` attribute. The resulting `CatalogObject` instance is also a `CatalogItem` instance.<br><br>In general, if `type=<OBJECT_TYPE>`, the `CatalogObject` instance must have the `<OBJECT_TYPE>`-specific data set on the `<object_type>_data` attribute. The resulting `CatalogObject` instance is also a `Catalog<ObjectType>` instance.<br><br>For a more detailed discussion of the Catalog data model, please see the<br>[Design a Catalog](https://developer.squareup.com/docs/catalog-api/design-a-catalog) guide. |
| `related_objects` | [`List Catalog Object`](../../doc/models/catalog-object.md) | Optional | A list of `CatalogObject`s referenced by the object in the `object` field. |

## Example (as JSON)

```json
{
  "object": {
    "id": "W62UWFY35CWMYGVWK6TWJDNI",
    "is_deleted": false,
    "item_data": {
      "category_id": "BJNQCF2FJ6S6UIDT65ABHLRX",
      "description": "Hot Leaf Juice",
      "name": "Tea",
      "tax_ids": [
        "HURXQOOAIC4IZSI2BEXQRYFY"
      ],
      "variations": [
        {
          "id": "2TZFAOHWGG7PAK2QEXWYPZSP",
          "is_deleted": false,
          "item_variation_data": {
            "item_id": "W62UWFY35CWMYGVWK6TWJDNI",
            "name": "Mug",
            "ordinal": 0,
            "price_money": {
              "amount": 150,
              "currency": "USD"
            },
            "pricing_type": "FIXED_PRICING"
          },
          "present_at_all_locations": true,
          "type": "ITEM_VARIATION",
          "updated_at": "2016-11-16T22:25:24.878Z",
          "version": 1479335124878
        }
      ]
    },
    "present_at_all_locations": true,
    "type": "ITEM",
    "updated_at": "2016-11-16T22:25:24.878Z",
    "version": 1479335124878,
    "custom_attribute_values": {
      "key0": {
        "name": "name3",
        "string_value": "string_value7",
        "custom_attribute_definition_id": "custom_attribute_definition_id9",
        "type": "SELECTION",
        "number_value": "number_value3"
      },
      "key1": {
        "name": "name2",
        "string_value": "string_value6",
        "custom_attribute_definition_id": "custom_attribute_definition_id0",
        "type": "STRING",
        "number_value": "number_value2"
      }
    },
    "catalog_v1_ids": [
      {
        "catalog_v1_id": "catalog_v1_id6",
        "location_id": "location_id6"
      }
    ]
  },
  "related_objects": [
    {
      "category_data": {
        "name": "Beverages"
      },
      "id": "BJNQCF2FJ6S6UIDT65ABHLRX",
      "is_deleted": false,
      "present_at_all_locations": true,
      "type": "CATEGORY",
      "updated_at": "2016-11-16T22:25:24.878Z",
      "version": 1479335124878,
      "custom_attribute_values": {
        "key0": {
          "name": "name1",
          "string_value": "string_value5",
          "custom_attribute_definition_id": "custom_attribute_definition_id1",
          "type": "SELECTION",
          "number_value": "number_value1"
        }
      },
      "catalog_v1_ids": [
        {
          "catalog_v1_id": "catalog_v1_id2",
          "location_id": "location_id2"
        },
        {
          "catalog_v1_id": "catalog_v1_id3",
          "location_id": "location_id3"
        }
      ]
    },
    {
      "id": "HURXQOOAIC4IZSI2BEXQRYFY",
      "is_deleted": false,
      "present_at_all_locations": true,
      "tax_data": {
        "calculation_phase": "TAX_SUBTOTAL_PHASE",
        "enabled": true,
        "inclusion_type": "ADDITIVE",
        "name": "Sales Tax",
        "percentage": "5.0"
      },
      "type": "TAX",
      "updated_at": "2016-11-16T22:25:24.878Z",
      "version": 1479335124878,
      "custom_attribute_values": {
        "key0": {
          "name": "name0",
          "string_value": "string_value4",
          "custom_attribute_definition_id": "custom_attribute_definition_id2",
          "type": "STRING",
          "number_value": "number_value0"
        },
        "key1": {
          "name": "name1",
          "string_value": "string_value5",
          "custom_attribute_definition_id": "custom_attribute_definition_id1",
          "type": "SELECTION",
          "number_value": "number_value1"
        },
        "key2": {
          "name": "name2",
          "string_value": "string_value6",
          "custom_attribute_definition_id": "custom_attribute_definition_id0",
          "type": "NUMBER",
          "number_value": "number_value2"
        }
      },
      "catalog_v1_ids": [
        {
          "catalog_v1_id": "catalog_v1_id3",
          "location_id": "location_id3"
        },
        {
          "catalog_v1_id": "catalog_v1_id4",
          "location_id": "location_id4"
        },
        {
          "catalog_v1_id": "catalog_v1_id5",
          "location_id": "location_id5"
        }
      ]
    }
  ],
  "errors": [
    {
      "category": "REFUND_ERROR",
      "code": "MERCHANT_SUBSCRIPTION_NOT_FOUND",
      "detail": "detail1",
      "field": "field9"
    },
    {
      "category": "MERCHANT_SUBSCRIPTION_ERROR",
      "code": "BAD_REQUEST",
      "detail": "detail2",
      "field": "field0"
    },
    {
      "category": "EXTERNAL_VENDOR_ERROR",
      "code": "MISSING_REQUIRED_PARAMETER",
      "detail": "detail3",
      "field": "field1"
    }
  ]
}
```

