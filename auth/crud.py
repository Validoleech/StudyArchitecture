from sqlalchemy.orm import Session
from models import UserModel

def create_user(db: Session, login: str, password: str, score: float) -> UserModel:
    user = UserModel(login=login, password=password, score=score)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def read_user(db: Session, login: str) -> UserModel:
    return db.query(UserModel).filter(UserModel.login == login).first()

def delete_user(db: Session, login: str) -> None:
    user = db.query(UserModel).filter(UserModel.login == login).first()
    if user:
        db.delete(user)
        db.commit()

def update_password(db: Session, login: str, new_password: str) -> UserModel:
    user = db.query(UserModel).filter(UserModel.login == login).first()
    if user:
        user.password = new_password
        db.commit()
        db.refresh(user)
    return user
