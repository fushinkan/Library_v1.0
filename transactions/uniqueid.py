#This function generates a unique identifier for an instance of the Book class

import uuid

def generate_id():
    return str(uuid.uuid4())