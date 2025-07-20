import requests
import json
from langchain.tools import tool
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from typing import List, Optional
import random
from pydantic import BaseModel, Field

# ---- Constants ----

#BASE_URL = "https://petstore3.swagger.io/api/v3" # Newer (beta) Pet Store API - v3
BASE_URL = "https://petstore.swagger.io/v2" # Current Pet Store API - v2
HEADERS = {"Content-Type": "application/json"}

# ---- Args Schemas ----

class AddPetInput(BaseModel):
    name: str = Field(..., description="Name of the pet.")
    photoUrls: Optional[List[str]] = Field(default=None, description="List of photo URLs.")
    tags: Optional[List[dict]] = Field(default=None, description="List of tag dictionaries (with 'id' and 'name').")
    status: str = Field(default="available", description="Pet status (available, pending, sold).")

class UpdatePetInput(BaseModel):
    id: int = Field(..., description="ID of the pet to update.")
    name: str = Field(..., description="Name of the pet.")
    photoUrls: Optional[List[str]] = Field(default=None, description="List of photo URLs.")
    tags: Optional[List[dict]] = Field(default=None, description="List of tag dicts.")
    status: str = Field(default="available", description="Pet status (default 'available').")

class GetPetByIdInput(BaseModel):
    pet_id: int = Field(..., description="Pet ID.")

class DeletePetInput(BaseModel):
    pet_id: int = Field(..., description="Pet ID to delete.")

class FindPetsByStatusInput(BaseModel):
    status: str = Field(default="available", description="Pet status (available, pending, sold).")

class FindPetsByTagsInput(BaseModel):
    tags: str = Field(..., description='Comma-separated string, e.g. "tag1,tag2"')


# ---- Tools ----

# Pet Store Tools
# These tools interact with the Pet Store API.

@tool("add_pet", args_schema=AddPetInput)
def add_pet(
    name: str,
    photoUrls: Optional[List[str]] = None,
    tags: Optional[List[dict]] = None,
    status: str = "available",
) -> str:
    """
    Adds a new pet to the Pet Store.
    """
    print(f"Adding pet: {name}, Status: {status}, Tags: {tags}, Photo URLs: {photoUrls}")

    url = f"{BASE_URL}/pet"
    payload = {
        "id": 4444000000 + random.randint(0, 99999),
        "name": name,
        "photoUrls": photoUrls or [],
        "status": status,
        "tags": tags or []
    }
    response = requests.post(url, json=payload, headers=HEADERS)
    response.raise_for_status()
    return "Added pet successfully - ID: {}".format(payload["id"])


@tool("update_pet", args_schema=UpdatePetInput)
def update_pet(
    id: int,
    name: str,
    photoUrls: Optional[List[str]] = None,
    tags: Optional[List[dict]] = None,
    status: str = "available",
) -> str:
    """
    Update an existing pet's information in the Pet Store.
    """
    url = f"{BASE_URL}/pet"
    payload = {
        "id": id,
        "name": name,
        "photoUrls": photoUrls or [],
        "status": status,
        "tags": tags or [],
    }
    response = requests.put(url, json=payload, headers=HEADERS)
    response.raise_for_status()
    return "Pet updated successfully"


@tool("get_pet_by_id", args_schema=GetPetByIdInput)
def get_pet_by_id(pet_id: int) -> str:
    """
    Gets a pet by its ID.
    """
    url = f"{BASE_URL}/pet/{pet_id}"
    # Try 5 times to handle potential 404 errors
    for _ in range(5):
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            break

    if response.status_code == 404:
        return f"Pet with ID {pet_id} not found"
    
    response.raise_for_status()
    return json.dumps(response.json(), indent=2)


@tool("delete_pet", args_schema=DeletePetInput)
def delete_pet(pet_id: int) -> str:
    """
    Deletes a pet by its ID.
    """
    url = f"{BASE_URL}/pet/{pet_id}"
    response = requests.delete(url, headers=HEADERS)
    if response.status_code == 404:
        return f"Pet with ID {pet_id} not found"
    response.raise_for_status()
    return "Pet deleted successfully"


@tool("find_pets_by_status", args_schema=FindPetsByStatusInput)
def find_pets_by_status(status: str = "available") -> str:
    """
    Finds pets by status.
    """
    print(f"Finding pets with status: {status}")
    url = f"{BASE_URL}/pet/findByStatus"
    for _ in range(5):
        response = requests.get(url, params={"status": status}, headers=HEADERS)
        if response.status_code == 200:
            break
    response.raise_for_status()
    return json.dumps(response.json(), indent=2)


# @tool("find_pets_by_tags", args_schema=FindPetsByTagsInput)
# def find_pets_by_tags(tags: str) -> str:
#     """
#     Finds pets by comma-separated tags.
#     """
#     url = f"{BASE_URL}/pet/findByTags"
#     tag_list = [t.strip() for t in tags.split(",") if t.strip()]
#     response = requests.get(url, params=[('tags', t) for t in tag_list], headers=HEADERS)
#     response.raise_for_status()
#     return json.dumps(response.json(), indent=2)


# Wikipedia tool
wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

# List of all petstore tools
petstore_tools = [
    add_pet,
    update_pet,
    get_pet_by_id,
    delete_pet,
    find_pets_by_status,
    # find_pets_by_tags,
    wikipedia,
]
