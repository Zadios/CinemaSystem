import random
import string
import uuid

def generate_ticket_code():
    return str(uuid.uuid4()).split('-')[0].upper()  # Código único, ejemplo: 'A1B2C3'
