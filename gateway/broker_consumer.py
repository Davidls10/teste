from kafka import KafkaConsumer
import json

# Função que consome dados do Kafka
def consume_sensor_data():
    consumer = KafkaConsumer(
        'sensor_data',  # Nome do tópico Kafka
        bootstrap_servers='localhost:9092',
        group_id='sensor_group',
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )
    
    for message in consumer:
        print(f"📩 Dados do sensor recebidos: {message.value}")
        # Aqui você pode processar ou salvar os dados conforme necessário.

# Chama a função para consumir dados do Kafka
if __name__ == '__main__':
    consume_sensor_data()
