# client.py
import json

from app import celery


@celery.task(name="client_func")
def client_func():
    import grpc
    from app.client import greet_pb2
    from app.client import greet_pb2_grpc
    channel = grpc.insecure_channel("grpc_server:50051")
    stub = greet_pb2_grpc.GreetServiceStub(channel)
    response = stub.Greet(greet_pb2.GreetRequest(object_id="ZRgPP9dBMm"))  # Here we have to enter the object_id
    # of car to request the data.
    print(type(response))
    print("Data: ", json.loads(response.data))
    print("Status: ", response.status)
