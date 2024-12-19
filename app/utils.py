from sqlalchemy.orm import Session
from app.models import User
from passlib.hash import bcrypt
import random
import string

def generate_password(length=8):
    """Создание пароля длиной length символов из букв и цифр."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_score(good=False):
    """Создание случайного score."""
    if good:
        return random.uniform(0.5, 1.0)
    return random.uniform(0.0, 0.5)

def authenticate_user(db: Session, login: str, password: str):
    """Аутентификация пользователя по логину и паролю."""
    user = db.query(User).filter(User.login == login).first()
    if user and bcrypt.verify(password, user.password):
        return user
    return None