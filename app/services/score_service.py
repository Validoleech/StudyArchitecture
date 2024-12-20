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
        """
        Получает пользователя из БД или создаёт нового, если такой логин отсутствует.

        Args:
            auth (LoginModel): Модель логина, содержащая учетные данные пользователя.

        Returns:
            dict: Словарь, содержащий логин пользователя, пароль и оценку.
        """
        user = get_or_create_user(self.db, auth.login)
        return {"login": user.login, "password": user.password, "score": user.score}
    
    def reset_score(self, auth: LoginModel, good: bool = False) -> dict:
        """
        Сбрасывает счет пользователя.
        Args:
            auth (LoginModel): Модель аутентификации пользователя.
            good (bool, optional): Флаг генерации от 0.5 до 1.0. По умолчанию: False
        Returns:
            dict: Словарь с логином пользователя, новым счетом и сообщением о сбросе счета.
        """
        user = get_or_create_user(self.db, auth.login)
        user.score = generate_score(good)
        self.db.commit()
        return {"login": user.login, "score": user.score, "message": "Score reset."}
    
    def is_admin(self, auth: LoginModel) -> bool:
        """Проверяет, является ли пользователь администратором.

        Args:
            auth (LoginModel): Логин пользователя.

        Returns:
            bool: True, если является.
        """
        return auth.login == "auth_admin"