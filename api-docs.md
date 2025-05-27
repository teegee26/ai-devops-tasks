# GET `/api/users`

Retrieves a paginated list of users. Supports optional filtering by user role.

## Query Parameters

| Name   | Type   | Description                        | Default | Notes         |
|--------|--------|------------------------------------|---------|---------------|
| page   | int    | Page number                        | 1       |               |
| limit  | int    | Number of results per page         | 10      | Max: 100      |
| role   | string | Filter users by their role         |         | Optional      |

## Example Request

```
GET /api/users?page=2&limit=20&role=admin
```

## Example Response

```json
{
    "page": 2,
    "limit": 20,
    "total": 45,
    "users": [
        {
            "id": 101,
            "name": "Alice Smith",
            "email": "alice@example.com",
            "role": "admin"
        },
        {
            "id": 102,
            "name": "Bob Jones",
            "email": "bob@example.com",
            "role": "admin"
        }
        // ...
    ]
}
```