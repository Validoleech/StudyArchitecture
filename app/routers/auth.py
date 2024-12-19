from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User, AuthModel
from app.utils import authenticate_user

router = APIRouter()

@router.post("/auth")
def authenticate(auth: AuthModel, password: str, db: Session = Depends(get_db)):

    user = authenticate_user(db, login, password)

    if user:
        return {"login": user.login, "authenticated": True}
    
    raise HTTPException(status_code=401, detail="Unauthorized")