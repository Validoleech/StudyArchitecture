from sqlalchemy.orm import Session
from app.crud import get_user_login
from app.models import AuthModel

class AuthService:
    @staticmethod
    def authorize(db: Session, auth: AuthModel) -> dict:
        user = get_user_login(db, auth.login)
        
        if user and user.password == auth.password:
            return {"authorized": True}

        return {"authorized": False}