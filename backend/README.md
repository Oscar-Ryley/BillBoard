Run with `python3 -m api`
Install dependencies with `pip3 install -r requirements.txt`

## API
### GET /api/search?query=\<query\>
Search for a query in the database. Returns a list of objects with the following structure:
```json
{
    "results": [
        {
            "id": "1", // ISBN
            "title": "Example Listing",
            "description": "This is an example listing.",
            "price": 100.00,
            "image": "https://example.com/image.jpg",
            "date": "2021-01-01T12:00:00Z"
        },

        {
            "id": "2", // ISBN
            "title": "Example Listing 2",
            "description": "This is another example listing.",
            "price": 90.00,
            "image": "https://example.com/image2.jpg",
            "date": "2021-01-01T12:00:00Z"
        }
    ]
}
```

### GET /api/listing/\<id\>
Get a listing by its ID. Returns an object with the following structure:
```json
{
    "id": "1", // ISBN
    "title": "Example Listing",
    "description": "This is an example listing.",
    "image": "https://example.com/image.jpg",
    "marketPrize": 120.00,
    "prices": [
        {
            "date": "2021-01-01T12:00:00Z",
            "new": 100.00,
            "used": 90.00,
            "average": 95.00
        },
        {
            "date": "2021-01-01T12:00:00Z",
            "new": 100.00,
            "used": 90.00,
            "average": 95.00
        }
    ],
    "offers": [
        {
            "id": "1",
            "price": 100.00,
            "date": "2021-01-01T12:00:00Z",
            "seller": {
                "id": "1", // This ID is currently not assosiated with a user
                "username": "example"
            },
            "conition": "new",
            "notes": null,
            "location": "Sheffield"
        },
        {
            "id": "2",
            "price": 90.00,
            "date": "2021-01-01T12:00:00Z",
            "seller": {
                "id": 2, // This ID is currently not assosiated with a user
                "username": "example2"
            },
            "conition": "used",
            "notes": "This is a note.",
            "location": "Newcastle"
        }
    ],
    "editions": [ // These will be different ISBNs which are just newer editions of the same book
        2, 
        3,
        5
    ]
    }
```

### POST /api/create
Creates a new offer in a listing. Requires the following request body:
```json
{
    "bookID": 2, // ISBN
    "price": 80,
    "condition": "new",
    "notes": null, // null or string
    "location": "Sheffield",
    "date": "2021-01-01T12:00:00Z",
    "seller": 1
}
```
