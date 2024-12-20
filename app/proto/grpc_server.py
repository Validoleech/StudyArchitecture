import logging
from concurrent import futures
import grpc
from app.proto import services_pb2, services_pb2_grpc
from app.services.score_service import ScoreService
from app.services.auth_service import AuthService
from app.database import get_db

class ScoreServiceServicer(services_pb2_grpc.ScoreServiceServicer):
    def __init__(self, db):
        self.score_service = ScoreService(db)

    def GetScore(self, request, context):
        user = self.score_service.get_user(request)
        return services_pb2.ScoreResponse(
            login=user["login"],
            message="Score retrieved successfully.",
            score=user["score"],
            valid=user["score"]
        )

    def GetPassword(self, request, context):
        user = self.score_service.get_password(request)
        return services_pb2.PasswordResponse(
            login=user["login"],
            password=user["password"]
        )

    def GetGud(self, request, context):
        user = self.score_service.reset_score(request, good=True)
        return services_pb2.ScoreResponse(
            login=user["login"],
            message="Score reset to a good value.",
            score=user["score"],
            valid=user["score"]
        )

class AuthServiceServicer(services_pb2_grpc.AuthServiceServicer):
    def __init__(self, db):
        self.auth_service = AuthService()
        self.db = db

    def Authorize(self, request, context):
        auth_response = self.auth_service.authorize(self.db, request)
        return services_pb2.AuthResponse(
            authorized=auth_response["authorized"],
            message=auth_response["message"]
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=6))
    db = next(get_db())
    services_pb2_grpc.add_ScoreServiceServicer_to_server(ScoreServiceServicer(db), server)
    services_pb2_grpc.add_AuthServiceServicer_to_server(AuthServiceServicer(db), server)
    server.add_insecure_port('[::]:50051')
    logging.info("gRPC server is starting on port 50051.")
    server.start()
    logging.info("gRPC server started.")
    server.wait_for_termination()