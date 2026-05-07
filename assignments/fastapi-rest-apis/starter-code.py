# Starter Code: Building REST APIs with FastAPI

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

# Sample in-memory items list
items = [
    {"id": 1, "name": "Notebook"},
    {"id": 2, "name": "Pencil"},
    {"id": 3, "name": "Ruler"},
]


# --- Task 1: Basic Endpoints ---

# TODO: Define a root GET endpoint (/) that returns a welcome message
# Example response: {"message": "Welcome to the Items API!"}


# TODO: Define a GET /items endpoint that returns the full items list
# Hint: return the items list directly


# --- Task 2: Path and Query Parameters ---

# TODO: Define GET /items/{item_id} that returns a single item by ID
# Hint: search the items list for a matching id
# If not found, raise HTTPException(status_code=404, detail="Item not found")


# TODO: Add an optional `search` query parameter to GET /items
# Hint: def get_items(search: str = None): ...
# If search is provided, filter items where search appears in the name


# --- Task 3: POST Endpoint ---

# TODO: Define a Pydantic model called Item with fields: id (int) and name (str)
class Item(BaseModel):
    pass  # Replace with your fields


# TODO: Define POST /items that accepts an Item body, appends it to the list,
# and returns the new item with status_code=201
# Hint: use @app.post("/items", status_code=status.HTTP_201_CREATED)


# Run with: uvicorn starter-code:app --reload
