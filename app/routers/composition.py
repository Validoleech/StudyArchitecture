from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import AuthModel
from app.services.composition_service import CompositionService

router = APIRouter()

@router.post("/composition")
def composition(data: AuthModel, db: Session = Depends(get_db)):
    composition_service = CompositionService(db)
    auth_response = composition_service.check_and_authorize(data)
    return auth_response