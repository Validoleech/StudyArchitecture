from sqlalchemy.orm import Session
from app.models import User
from app.utils import generate_score, generate_password

def get_or_create_user(db: Session, login: str):
    """
    Получает существующего пользователя или создаёт нового.
    """
    user = db.query(User).filter(User.login == login).first()
    if not user:
        user = User(login=login, password=generate_password(), score=generate_score())
        db.add(user)
        db.commit()
        db.refresh(user)
    return user

def get_user_login(db: Session, login: str):
    """
    Получает пользователя по логину.
    """
    return db.query(User).filter(User.login == login).first()