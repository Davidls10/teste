from flask import Flask
from threading import Thread
import broker_consumer  # Importando o consumidor Kafka
import rest_api  # Importando o arquivo REST API

# Função para iniciar o consumidor Kafka em um thread separado
def start_kafka_consumer():
    consumer_thread = Thread(target=broker_consumer.consume_sensor_data)
    consumer_thread.daemon = True
    consumer_thread.start()

# Iniciar o servidor Flask e o consumidor Kafka
if __name__ == '__main__':
    start_kafka_consumer()  # Inicia o consumidor Kafka
    rest_api.app.run(host='0.0.0.0', port=5000)  # Inicia o servidor Flask
