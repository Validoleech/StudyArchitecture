from sqlalchemy.orm import Session
from app.models import AuthModel
from app.crud import get_or_create_user
from app.services.score_service import ScoreService
from app.services.auth_service import AuthService
import os
THRESHOLD_SCORE = float(os.getenv("THRESHOLD_SCORE", 0.5))

class CompositionService:
    def __init__(self, db: Session):
        self.db = db
        self.score_service = ScoreService(db)
        self.auth_service = AuthService()

    def check_and_authorize(self, auth: AuthModel) -> dict:
        user = self.score_service.get_user(auth)
        
        if user["score"] < THRESHOLD_SCORE:
            self.db.delete(user)
            self.db.commit()
            return {"authorized": False}
        
        return self.auth_service.authorize(user["login"], user["password"])