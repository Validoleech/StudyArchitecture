from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import AuthModel, AuthResponseModel
from app.services.composition_service import CompositionService

router = APIRouter()

@router.post("/composition", response_model=AuthResponseModel, status_code=status.HTTP_200_OK)
def composition(data: AuthModel, db: Session = Depends(get_db)):
    composition_service = CompositionService(db)
    auth_response = composition_service.check_and_authorize(data)
    if not auth_response.get("authorized"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=auth_response.get("message", "Unauthorized")
        )
    return auth_response