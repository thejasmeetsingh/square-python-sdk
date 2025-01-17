
# Bulk Create Team Members Request

Represents a bulk create request for `TeamMember` objects.

## Structure

`Bulk Create Team Members Request`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `team_members` | [`Dict Str Create Team Member Request`](../../doc/models/create-team-member-request.md) | Required | The data used to create the `TeamMember` objects. Each key is the `idempotency_key` that maps to the `CreateTeamMemberRequest`. The maximum number of create objects is 25. |

## Example (as JSON)

```json
{
  "team_members": {
    "idempotency-key-1": {
      "team_member": {
        "assigned_locations": {
          "assignment_type": "EXPLICIT_LOCATIONS",
          "location_ids": [
            "YSGH2WBKG94QZ",
            "GA2Y9HSJ8KRYT"
          ]
        },
        "email_address": "joe_doe@gmail.com",
        "family_name": "Doe",
        "given_name": "Joe",
        "phone_number": "+14159283333",
        "reference_id": "reference_id_1",
        "id": "id3",
        "is_owner": true,
        "status": "INACTIVE"
      },
      "idempotency_key": "idempotency_key3"
    },
    "idempotency-key-2": {
      "team_member": {
        "assigned_locations": {
          "assignment_type": "ALL_CURRENT_AND_FUTURE_LOCATIONS"
        },
        "email_address": "jane_smith@gmail.com",
        "family_name": "Smith",
        "given_name": "Jane",
        "phone_number": "+14159223334",
        "reference_id": "reference_id_2",
        "id": "id4",
        "is_owner": false,
        "status": "ACTIVE"
      },
      "idempotency_key": "idempotency_key4"
    }
  }
}
```

