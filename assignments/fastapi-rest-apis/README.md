# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build REST API endpoints using the FastAPI framework in Python. In this assignment, you will create simple HTTP endpoints, work with JSON responses, and use path and query parameters to handle requests.

## 📝 Tasks

### 🛠️ Create Basic API Endpoints

#### Description
Set up a FastAPI application and define your first GET endpoints that return JSON responses.

#### Requirements
Completed program should:

- Import and initialize a `FastAPI` app instance
- Define a root endpoint (`GET /`) that returns a welcome message as JSON
- Define a `GET /items` endpoint that returns a list of at least 3 sample items
- Run the app using `uvicorn` and confirm the endpoints respond correctly


### 🛠️ Add Path and Query Parameters

#### Description
Extend your API to accept dynamic input through path parameters and optional query parameters.

#### Requirements
Completed program should:

- Define a `GET /items/{item_id}` endpoint that returns a single item by its ID
- Return a descriptive error message when the requested item ID does not exist
- Add an optional query parameter `search` to the `GET /items` endpoint to filter items by name
- Demonstrate requests using both a valid item ID and an invalid item ID

### 🛠️ Create a POST Endpoint

#### Description
Add a `POST /items` endpoint that accepts JSON data from the client and adds a new item to the list.

#### Requirements
Completed program should:

- Define a Pydantic model for the item with at least `id` and `name` fields
- Accept a JSON request body and validate it using the Pydantic model
- Append the new item to the items list and return it in the response
- Return appropriate status codes (use `status_code=201` for successful creation)
