from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import LoginModel, ScoreModel
from app.services.score_service import ScoreService
from dotenv import load_dotenv
import os

router = APIRouter()

load_dotenv()
THRESHOLD_SCORE = float(os.getenv("THRESHOLD_SCORE", 0.5))

@router.post("/score")
def get_score(data: LoginModel, db: Session = Depends(get_db)):

    score_service = ScoreService(db)
    user = score_service.get_user(data)

    if score_service.is_admin(data):
        raise HTTPException(status_code=403, detail="Forbidden")

    if user["score"] < THRESHOLD_SCORE:
        user = score_service.reset_score(data)
        return ScoreModel(
            login=user["login"],
            message="Score reset due to low value.",
            score=user["score"]
        )

    return ScoreModel(
        login=user["login"],
        score=user["score"],
        valid=user["score"] > THRESHOLD_SCORE
    )

@router.post("/getpwd")
def get_password(data: LoginModel, db: Session = Depends(get_db)):

    score_service = ScoreService(db)
    user = score_service.get_user(data)

    return {"login": user["login"], "password": user["password"]}

#Чтобы не роллить 0.5
@router.post("/getgud")
def get_gud(data: LoginModel, db: Session = Depends(get_db)):
    score_service = ScoreService(db)
    user = score_service.reset_score(data, good=True)
    return ScoreModel(
        login=user["login"],
        message="Score reset to a good value.",
        score=user["score"]
    )