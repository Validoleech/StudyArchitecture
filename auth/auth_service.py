from sqlalchemy.orm import Session
from fastapi import HTTPException
from .crud import create_user, read_user, delete_user, update_password
from .models import UserModel
from .utils import generate_password

class AuthService:

    def authorize(db: Session, login: str, password: str) -> dict:
        user = read_user(db, login)
        if user and user.password == password:
            return {"authorized": True}
        return {"authorized": False}

    def create_user_service(db: Session, login: str) -> UserModel:
        try:
            return create_user(db, login)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def read_user_service(db: Session, login: str) -> UserModel:
        user = read_user(db, login)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    def delete_user_service(db: Session, login: str) -> None:
        user = read_user(db, login)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        delete_user(db, login)
        return {"message": f"User {login} deleted"}

    def change_password(db: Session, login: str, old_password: str, new_password: str = None) -> UserModel:
        user = read_user(db, login)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        if user.password != old_password:
            raise HTTPException(status_code=400, detail="Old password is incorrect")
        if new_password is None:
            new_password = generate_password()
        return update_password(db, login, new_password)