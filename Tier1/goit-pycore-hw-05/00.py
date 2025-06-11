import pickle

# Define the Person class
class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __eq__(self, other):
        if isinstance(other, Person):
            return (self.name == other.name and 
                    self.email == other.email and 
                    self.phone == other.phone and 
                    self.favorite == other.favorite)
        return False

# Define the Contacts class
class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts

    def save_to_file(self):
        """Serializes the Contacts instance to a binary file."""
        with open(self.filename, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def read_from_file(filename: str):
        """Deserializes a Contacts instance from a binary file."""
        with open(filename, 'rb') as file:
            return pickle.load(file)

    def __eq__(self, other):
        if isinstance(other, Contacts):
            # Compare only contacts, not filename or object references
            return self.contacts == other.contacts
        return False

# Example usage:
contacts = [
    Person("Allen Raymond", "nulla.ante@vestibul.co.uk", "(992) 914-3792", True),
    Person("Chaim Lewis", "dui.in@egetlacus.ca", "(294) 840-6685", True),
]

# Creating Contacts object
persons = Contacts("user_class.dat", contacts)

# Saving the object to a file
persons.save_to_file()

# Reading the object back from the file
person_from_file = Contacts.read_from_file("user_class.dat")

# Print comparison results
print(persons == person_from_file)  # This should now print False, since it's comparing by contacts list
print(persons.contacts[0] == person_from_file.contacts[0])  # True, both Person objects match
print(persons.contacts[0].name == person_from_file.contacts[0].name)  # True
print(persons.contacts[0].email == person_from_file.contacts[0].email)  # True
print(persons.contacts[0].phone == person_from_file.contacts[0].phone)  # True

