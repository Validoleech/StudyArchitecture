from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User, LoginModel
from app.utils import generate_password
import random

router = APIRouter()

@router.post("/score")
def get_score(login: LoginModel, db: Session = Depends(get_db)):

    # Колхозная проверка на привелигированного пользователя
    if login.login == "auth_admin":
        raise HTTPException(status_code=403, detail="Modification of 'auth_admin' is not allowed.")

    user = db.query(User).filter(User.login == login.login).first()

    # При отсутствии пользователя с таким логином создаём новый логин и пароль, возвращаем логин-пароль-score
    if not user:
        password = generate_password()
        user = User(login=login.login, password=password, score=random.uniform(0.0, 1.0))
        db.add(user)
        db.commit()
        return {
            "login": user.login,
            "password": password,
            "score": user.score
        }

    return {
        "login": user.login,
        "score": user.score
    }