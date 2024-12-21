import grpc
import auth_service_pb2
import auth_service_pb2_grpc

class AuthClient:
    def __init__(self):
        self.channel = grpc.insecure_channel('localhost:50051')
        self.stub = auth_service_pb2_grpc.AuthServiceStub(self.channel)

    def authorize(self, login: str, password: str) -> bool:
        response = self.stub.Authorize(auth_service_pb2.AuthorizeRequest(login=login, password=password))
        return response.authorized

    def create_user(self, login: str, password: str, score: float):
        response = self.stub.CreateUser(auth_service_pb2.CreateUserRequest(login=login, password=password, score=score))
        return response

    def read_user(self, login: str):
        response = self.stub.ReadUser(auth_service_pb2.ReadUserRequest(login=login))
        return response

    def change_password(self, login: str, old_password: str, new_password: str):
        response = self.stub.ChangePassword(auth_service_pb2.ChangePasswordRequest(login=login, old_password=old_password, new_password=new_password))
        return response

    def delete_user(self, login: str):
        response = self.stub.DeleteUser(auth_service_pb2.DeleteUserRequest(login=login))
        return response