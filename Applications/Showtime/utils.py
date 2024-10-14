import random
import string

def generate_ticket_code():
    characters = string.ascii_uppercase + string.digits  # Letras mayúsculas y dígitos
    return ''.join(random.choices(characters, k=8))  # Genera una cadena de 8 caracteres
