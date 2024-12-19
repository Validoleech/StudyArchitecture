from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.routers.score import get_score
from app.routers.auth import authenticate
from app.models import User, AuthModel
from dotenv import load_dotenv
import os

load_dotenv()
THRESHOLD_SCORE = os.getenv("THRESHOLD_SCORE")

router = APIRouter()

@router.post("/composition")
def composition(auth: AuthModel, db: Session = Depends(get_db)):
    # Получение пользователя из БД
    user = db.query(User).filter(User.login == auth.login).first()

    if user.password != auth.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not user:
        # Если пользователя нет, создаём его с рандомным score
        response = get_score(login=auth.login, db=db)
        response.update({"action": "User created with random score"})
        return response

    # Проверяем пороговое значение
    if user.score < THRESHOLD_SCORE:
        return {"action": "Score below threshold", **get_score(login=auth.login, db=db)}

    # Если score выше порога, выполняем auth
    return authenticate(login=auth.login, password=auth.password, db=db)
