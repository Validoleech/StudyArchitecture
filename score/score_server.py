from concurrent import futures
import grpc
from models import UserModel
from utils import generate_score
from models import SessionLocal
import score_service_pb2
import score_service_pb2_grpc
import os
import logging

THRESHOLD_SCORE = float(os.getenv("THRESHOLD_SCORE", 0.5))

class ScoreServiceServicer(score_service_pb2_grpc.ScoreServiceServicer):
    def __init__(self):
        self.db = SessionLocal()

    def GetScore(self, request, context):
        user = self.db.query(UserModel).filter(UserModel.login == request.login).first()
        if user:
            logging.info(f"Score of {user.login} obtained: {user.score}")
            return score_service_pb2.ScoreResponse(score=user.score)
        context.set_code(grpc.StatusCode.NOT_FOUND)
        context.set_details("User not found")
        return score_service_pb2.ScoreResponse()

    def RegenerateScore(self, request, context):
        user = self.db.query(UserModel).filter(UserModel.login == request.login).first()
        if user:
            user.score = generate_score(request.good)
            self.db.commit()
            logging.info(f"Score of {user.login} regenerated: {user.score}")
            return score_service_pb2.ScoreResponse(score=user.score)
        context.set_code(grpc.StatusCode.NOT_FOUND)
        context.set_details("User not found")
        return score_service_pb2.ScoreResponse()

    def EvaluateScore(self, request, context):
        user = self.db.query(UserModel).filter(UserModel.login == request.login).first()
        if user:
            valid = user.score > THRESHOLD_SCORE
            logging.info(f"Score of {user.login} evaluated: {valid}")
            return score_service_pb2.EvaluateScoreResponse(valid=valid)
        context.set_code(grpc.StatusCode.NOT_FOUND)
        context.set_details("User not found")
        return score_service_pb2.EvaluateScoreResponse()
    
    def GenerateScore(self, request, context):
        score = generate_score(request.good)
        logging.info(f"Generated score: {score}")
        return score_service_pb2.ScoreResponse(score=score)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    score_service_pb2_grpc.add_ScoreServiceServicer_to_server(ScoreServiceServicer(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()