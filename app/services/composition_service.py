from sqlalchemy.orm import Session
from app.models import AuthModel, LoginModel
from app.services.score_service import ScoreService
from app.services.auth_service import AuthService
from app.crud import delete_user
import os
THRESHOLD_SCORE = float(os.getenv("THRESHOLD_SCORE", 0.5))

class CompositionService:
    def __init__(self, db: Session):
        self.db = db
        self.score_service = ScoreService(db)
        self.auth_service = AuthService()

    def check_and_authorize(self, auth: AuthModel) -> dict:
        """
        Проверяет пользователя и авторизует его, если он соответствует требованиям.
        Args:
            auth (AuthModel): Модель аутентификации пользователя.
        Returns:
            dict: Словарь с результатом авторизации. Если пользователь не прошел проверку, 
                  возвращается {"authorized": False}, иначе пересылает результат авторизации от auth_service.
        """
        user = self.score_service.get_user(LoginModel(login=auth.login))
        print(user)
        if user["score"] < THRESHOLD_SCORE:
            delete_user(self.db, user["login"])
            return {"authorized": False, "message": "User was deleted due to low score"}
        
        return self.auth_service.authorize(self.db, auth)