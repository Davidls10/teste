import grpc
import gateway.grpc_service_pb2 as grpc_messages
import gateway.grpc_service_pb2_grpc as grpc_stub

# Função para controlar a lâmpada via gRPC
def control_lampada(action):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = grpc_stub.LampServiceStub(channel)
        
        if action == "ligar":
            stub.LigarLampada(grpc_messages.Empty())
            print("Lâmpada ligada")
        elif action == "desligar":
            stub.DesligarLampada(grpc_messages.Empty())
            print("Lâmpada desligada")

# Exemplo de uso
if __name__ == '__main__':
    action = input("Digite 'ligar' ou 'desligar' para a lâmpada: ")
    control_lampada(action)
