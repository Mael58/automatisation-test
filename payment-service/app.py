import grpc
from concurrent import futures
from models.payment_pb2_grpc import PaymentServicer, add_PaymentServicer_to_server
from models.payment_pb2 import PayReply
import random
import logging

class PaymentSvc(PaymentServicer):

    def Pay(self, request, context):
        payment_is_ok = random.randint(0, 1)
        return PayReply(payment_is_ok == 1)

def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_PaymentServicer_to_server(PaymentSvc(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()