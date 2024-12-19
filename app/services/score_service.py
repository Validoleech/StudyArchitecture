from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import LoginModel
from app.crud import get_or_create_user
from app.utils import generate_score
import os
THRESHOLD_SCORE = float(os.getenv("THRESHOLD_SCORE", 0.5))

class ScoreService:
    def __init__(self, db: Session):
        self.db = db

    def get_user(self, auth: LoginModel) -> dict:
        user = get_or_create_user(self.db, auth.login)
        return {"login": user.login, "password": user.password, "score": user.score}
    
    def reset_score(self, auth: LoginModel, good: bool = False) -> dict:
        user = get_or_create_user(self.db, auth.login)
        user.score = generate_score(good)
        self.db.commit()
        return {"login": user.login, "score": user.score, "message": "Score reset."}
    
    def is_admin(self, auth: LoginModel) -> bool:
        return auth.login == "auth_admin"