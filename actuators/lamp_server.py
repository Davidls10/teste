import grpc
from concurrent import futures
import actuators.grpc_service_pb2 as grpc_messages
import actuators.grpc_service_pb2_grpc as grpc_stub

class LampadaService(grpc_stub.LampServiceServicer):
    estado = "desligado"

    def LigarLampada(self, request, context):
        self.estado = "ligado"
        print("💡 Lâmpada ligada!")
        return grpc_messages.Empty()
    
    def DesligarLampada(self, request, context):
        self.estado = "desligado"
        print("💡 Lâmpada desligada!")
        return grpc_messages.Empty()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    grpc_stub.add_LampServiceServicer_to_server(LampadaService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("🚀 Servidor gRPC de Lâmpada rodando na porta 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
