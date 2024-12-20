from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import LoginModel, ScoreModel
from app.services.score_service import ScoreService
import os

router = APIRouter()

THRESHOLD_SCORE = float(os.getenv("THRESHOLD_SCORE", 0.5))

@router.post("/score")
def get_score(data: LoginModel, db: Session = Depends(get_db)):

    score_service = ScoreService(db)

    if score_service.is_admin(data):
        raise HTTPException(status_code=403, detail="Forbidden")
    
    user = score_service.get_user(data)

    return {
        "login": user["login"],
        "message": user.get("message", ""),
        "score": user["score"],
        "valid": user["valid"]
    }

@router.post("/getpwd")
def get_password(data: LoginModel, db: Session = Depends(get_db)):

    score_service = ScoreService(db)

    if score_service.is_admin(data):
        raise HTTPException(status_code=403, detail="Forbidden")

    user = score_service.get_password(data)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {"login": data.login, "password": user["password"]}

#Чтобы не роллить 0.5
@router.post("/getgud")
def get_gud(data: LoginModel, db: Session = Depends(get_db)):
    score_service = ScoreService(db)
    user = score_service.reset_score(data, good=True)
    return ScoreModel(
        login=user["login"],
        message="Score reset to a good value.",
        score=user["score"],
        valid=user["score"] > THRESHOLD_SCORE
    )