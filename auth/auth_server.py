from concurrent import futures
import grpc
from crud import create_user, read_user, delete_user, update_password
from utils import generate_password
from models import SessionLocal
import auth_service_pb2
import auth_service_pb2_grpc

class AuthServiceServicer(auth_service_pb2_grpc.AuthServiceServicer):
    def __init__(self):
        self.db = SessionLocal()

    def Authorize(self, request, context):
        user = read_user(self.db, request.login)
        if user and user.password == request.password:
            return auth_service_pb2.AuthorizeResponse(authorized=True)
        return auth_service_pb2.AuthorizeResponse(authorized=False)

    def CreateUser(self, request, context):
        try:
            password = request.password if request.password else generate_password()
            user = create_user(self.db, request.login, password, request.score)
            return auth_service_pb2.UserResponse(login=user.login, password=user.password, score=request.score)
        except Exception as e:
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return auth_service_pb2.UserResponse()

    def ReadUser(self, request, context):
        user = read_user(self.db, request.login)
        if user is None:
            context.set_details("User not found")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return auth_service_pb2.UserResponse()
        return auth_service_pb2.UserResponse(login=user.login, password=user.password, score=user.score)

    def DeleteUser(self, request, context):
        user = read_user(self.db, request.login)
        if user is None:
            context.set_details("User not found")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return auth_service_pb2.Empty()
        delete_user(self.db, request.login)
        return auth_service_pb2.Empty()

    def ChangePassword(self, request, context):
        user = read_user(self.db, request.login)
        if user is None:
            context.set_details("User not found")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return auth_service_pb2.UserResponse()
        if user.password != request.old_password:
            context.set_details("Old password is incorrect")
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            return auth_service_pb2.UserResponse()
        new_password = request.new_password if request.new_password else generate_password()
        user = update_password(self.db, request.login, new_password)
        return auth_service_pb2.UserResponse(login=user.login, password=user.password, score=user.score)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    auth_service_pb2_grpc.add_AuthServiceServicer_to_server(AuthServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()