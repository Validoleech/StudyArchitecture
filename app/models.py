from sqlalchemy import Column, String, Float
from pydantic import BaseModel
from .database import Base

class User(Base):
    __tablename__ = "users"
    login = Column(String, primary_key=True, index=True)
    password = Column(String, nullable=False)
    score = Column(Float, default=0.0)

class LoginModel(BaseModel):
    login: str

class AuthModel(LoginModel):
    password: str

class ScoreModel(LoginModel):
    score: float