import grpc
from app.proto import services_pb2, services_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = services_pb2_grpc.ScoreServiceStub(channel)

    request = services_pb2.LoginRequest(login='test_user')

    try:
        response = stub.GetScore(request)
        print("ScoreService client received: " + response.message)
    except grpc.RpcError as e:
        print(f"gRPC error: {e.code()} - {e.details()}")

if __name__ == '__main__':
    run()