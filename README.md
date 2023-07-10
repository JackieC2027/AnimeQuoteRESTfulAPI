# Flask Quote API
The Anime Quote API adheres to the RESTful architecture by treating quotes as resources that can be accessed and manipulated using standard HTTP methods. Clients can retrieve quotes by making GET requests to the appropriate endpoints, creating new quotes with POST requests, updating existing quotes with PUT requests, and deleting quotes with DELETE requests. This resource-centric approach ensures that the API follows the principles of statelessness, uniform interface, and scalability, allowing clients to interact with anime quotes in a consistent and efficient manner.

# Requirements
Make sure you have the following dependencies installed before running the application:

- Python 3.x
- Flask
- Flask-RESTful
  
You can install the dependencies by running the following command:

```pip install flask flask_restful```

# Getting Started
To run the Flask Quote API, perform the following steps:

- Clone the repository or download the source code files.

- Navigate to the project directory using the command line.

- Run the following command to start the application:
```python app.py```

Once the application is running, you can access the API at http://localhost:5000.

# Endpoints
The API provides the following endpoints:

- GET /quotes: Retrieves all the quotes.

- POST /quotes: Creates a new quote.

- GET /quotes/<quote_id>: Retrieves a specific quote by ID.

- PUT /quotes/<quote_id>: Updates a specific quote by ID.

- DELETE /quotes/<quote_id>: Deletes a specific quote by ID.

# API Usage
GET /quotes
Retrieves all the quotes available in the collection.

# GET /quotes
```
{
    "quote1": {
        "content": "People died when they are killed",
        "character": "Shirou",
        "origin": "Fate/Stay Night"
    },
    "quote2": {
        "content": "Believe it!",
        "character": "Naruto",
        "origin": "Naruto Series"
    },
    ...
}
```

# POST /quotes
Creates a new quote and adds it to the collection.
```
{
    "quote": "New quote content",
    "character": "Character name",
    "origin": "Quote origin"
}


{
    "quote21": {
        "content": "New quote content",
        "character": "Character name",
        "origin": "Quote origin"
    }
}
```

# GET /quotes/<quote_id>
Retrieves a specific quote by its ID.
```
{
    "content": "People died when they are killed",
    "character": "Shirou",
    "origin": "Fate/Stay Night"
}
```

# PUT /quotes/<quote_id>
Updates a specific quote by its ID.

PUT /quotes/quote1
```
{
    "quote": "Updated quote content"
}
```

# Conclusion
The Flask Quote API allows you to manage a collection of quotes from various sources and characters. You can retrieve all the quotes, create new quotes, update existing quotes, and delete quotes using the provided endpoints. Feel free to explore and modify the API according to your requirements.
