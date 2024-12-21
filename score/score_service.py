from sqlalchemy.orm import Session
from .models import UserModel
from .utils import generate_score

class ScoreService:
    def __init__(self, db: Session):
        self.db = db

    def get_score(self, login: str) -> float:
        user = self.db.query(UserModel).filter(UserModel.login == login).first()
        if user:
            return user.score
        raise ValueError("User not found")

    def regenerate_score(self, login: str, good: bool = False) -> float:
        user = self.db.query(UserModel).filter(UserModel.login == login).first()
        if user:
            user.score = generate_score(good)
            self.db.commit()
            return user.score
        raise ValueError("User not found")

    def evaluate_score(self, login: str, threshold: float) -> bool:
        user = self.db.query(UserModel).filter(UserModel.login == login).first()
        if user:
            return user.score > threshold
        raise ValueError("User not found")