import requests

# Base URL for the json-server bots endpoint
BASE_URL = "http://localhost:3000/bots"


# Create a new bot
def create_bot(bot_data):
    response = requests.post(BASE_URL, json=bot_data)
    return response.json()


# Get all bots or a specific bot by ID
def get_bots(bot_id=None):
    url = BASE_URL if bot_id is None else f"{BASE_URL}/{bot_id}"
    response = requests.get(url)
    return response.json()


# Update an existing bot by ID
def update_bot(bot_id, bot_data):
    response = requests.put(f"{BASE_URL}/{bot_id}", json=bot_data)
    return response.json()


# Delete a bot by ID
def delete_bot(bot_id):
    response = requests.delete(f"{BASE_URL}/{bot_id}")
    return response.status_code
