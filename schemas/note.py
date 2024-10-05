# Function to convert a single MongoDB document (note) into a dictionary
def noteEntity(item) -> dict:
    return {
        "id": str(item["_id"]),  # Convert MongoDB ObjectId to a string
        "title": item["title"],
        "desc": item["desc"],
        "important": item["important"]
    }

# Function to convert a list of MongoDB documents (notes) into a list of dictionaries
def notesEntity(items) -> list:
    return [noteEntity(item) for item in items]  # Use 'items' consistently
