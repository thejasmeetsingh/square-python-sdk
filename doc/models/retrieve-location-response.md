
# Retrieve Location Response

Defines the fields that the [RetrieveLocation](../../doc/api/locations.md#retrieve-location)
endpoint returns in a response.

## Structure

`Retrieve Location Response`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`List Error`](../../doc/models/error.md) | Optional | Information about errors encountered during the request. |
| `location` | [`Location`](../../doc/models/location.md) | Optional | Represents one of a business' [locations](https://developer.squareup.com/docs/locations-api). |

## Example (as JSON)

```json
{
  "location": {
    "address": {
      "address_line_1": "123 Main St",
      "administrative_district_level_1": "CA",
      "country": "US",
      "locality": "San Francisco",
      "postal_code": "94114",
      "address_line_2": "address_line_20",
      "address_line_3": "address_line_36",
      "sublocality": "sublocality0"
    },
    "business_name": "Jet Fuel Coffee",
    "capabilities": [
      "CREDIT_CARD_PROCESSING"
    ],
    "country": "US",
    "created_at": "2016-09-19T17:33:12Z",
    "currency": "USD",
    "id": "18YC4JDH91E1H",
    "language_code": "en-US",
    "merchant_id": "3MYCJG5GVYQ8Q",
    "name": "Grant Park",
    "phone_number": "+1 650-354-7217",
    "status": "ACTIVE",
    "timezone": "America/Los_Angeles"
  },
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

