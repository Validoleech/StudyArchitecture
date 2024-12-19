from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import AuthModel
from app.services.auth_service import AuthService

router = APIRouter()

@router.post("/auth")
def authenticate(auth: AuthModel, db: Session = Depends(get_db)):
    result = AuthService.authorize(db, auth)
    if not result["authorized"]:
        raise HTTPException(status_code=401, detail="Invalid login or password")
    return result