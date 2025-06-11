import json


def write_contacts_to_file(filename, contacts):
    """
    Writes a list of contacts to a specified file in JSON format under the "contacts" key.
    
    Args:
        filename (str): The name of the file to write to.
        contacts (list): A list of contact dictionaries.
    """
    data = {"contacts": contacts}
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def read_contacts_from_file(filename):
    """
    Reads contacts from a JSON file and returns them as a list of dictionaries.
    
    Args:
        filename (str): The name of the file to read from.
    
    Returns:
        list: A list of contact dictionaries.
    """
    with open(filename, 'r') as file:
        data = json.load(file)
    return data.get("contacts", [])

    contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False
    },
    {
        "name": "Jane Doe",
        "email": "jane.doe@example.com",
        "phone": "(123) 456-7890",
        "favorite": True
    }
]
    
write_contacts_to_file("contacts.json", "contacts") 

loaded_contacts = read_contacts_from_file("contacts.json")

print(loaded_contacts)