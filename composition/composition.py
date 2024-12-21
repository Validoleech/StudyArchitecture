import sys
sys.path.append('/app/score')
sys.path.append('/app/auth')

import grpc
from fastapi import FastAPI, HTTPException
import auth_service_pb2 as auth_pb2
import auth_service_pb2_grpc as auth_pb2_grpc
import score_service_pb2 as score_pb2
import score_service_pb2_grpc as score_pb2_grpc

app = FastAPI()

class CompositionService:
    def __init__(self):
        self.auth_channel = grpc.insecure_channel('localhost:50051')
        self.auth_stub = auth_pb2_grpc.AuthServiceStub(self.auth_channel)
        self.score_channel = grpc.insecure_channel('localhost:50052')
        self.score_stub = score_pb2_grpc.ScoreServiceStub(self.score_channel)

    def create_user(self, login: str, password: str = None, good: bool = False):
        try:
            score_response = self.score_stub.GenerateScore(score_pb2.GenerateScoreRequest(good=good))
            response = self.auth_stub.CreateUser(auth_pb2.CreateUserRequest(login=login, password=password, score=score_response))
            return response
        except grpc.RpcError as e:
            raise HTTPException(status_code=e.code().value[0], detail=e.details())

    def delete_user(self, login: str):
        try:
            self.auth_stub.DeleteUser(auth_pb2.DeleteUserRequest(login=login))
        except grpc.RpcError as e:
            raise HTTPException(status_code=e.code().value[0], detail=e.details())

    def reset_score(self, login: str, good: bool = False):
        try:
            response = self.score_stub.RegenerateScore(score_pb2.RegenerateScoreRequest(login=login, good=good))
            return response
        except grpc.RpcError as e:
            raise HTTPException(status_code=e.code().value[0], detail=e.details())

    def get_password(self, login: str):
        try:
            response = self.auth_stub.ReadUser(auth_pb2.ReadUserRequest(login=login))
            return response.password
        except grpc.RpcError as e:
            raise HTTPException(status_code=e.code().value[0], detail=e.details())

    def reset_password(self, login: str, old_password: str, new_password: str):
        try:
            response = self.auth_stub.ChangePassword(auth_pb2.ChangePasswordRequest(login=login, old_password=old_password, new_password=new_password))
            return response
        except grpc.RpcError as e:
            raise HTTPException(status_code=e.code().value[0], detail=e.details())

composition_service = CompositionService()

@app.post("/users/")
def create_user(login: str, good: bool = False):
    return composition_service.create_user(login, good)

@app.delete("/users/{login}/delete")
def delete_user(login: str):
    return composition_service.delete_user(login)

@app.post("/users/{login}/reset_score")
def reset_score(login: str, good: bool = False):
    return composition_service.reset_score(login, good)

@app.get("/users/{login}/password")
def get_password(login: str):
    return composition_service.get_password(login)

@app.post("/users/{login}/reset_password")
def reset_password(login: str, old_password: str, new_password: str):
    return composition_service.reset_password(login, old_password, new_password)