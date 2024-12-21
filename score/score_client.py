import grpc
import score_service_pb2
import score_service_pb2_grpc

class ScoreClient:
    def __init__(self):
        self.channel = grpc.insecure_channel('localhost:50052')
        self.stub = score_service_pb2_grpc.ScoreServiceStub(self.channel)

    def get_score(self, login: str) -> float:
        response = self.stub.GetScore(score_service_pb2.GetScoreRequest(login=login))
        return response.score

    def regenerate_score(self, login: str, good: bool = False) -> float:
        response = self.stub.RegenerateScore(score_service_pb2.RegenerateScoreRequest(login=login, good=good))
        return response.score

    def evaluate_score(self, login: str) -> bool:
        response = self.stub.EvaluateScore(score_service_pb2.EvaluateScoreRequest(login=login))
        return response.valid