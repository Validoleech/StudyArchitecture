import random
import string

def generate_password(length=8):
    """Создание пароля длиной length символов из букв и цифр."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))