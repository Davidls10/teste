#!/bin/bash

# Iniciar o broker Kafka/RabbitMQ
docker-compose up -d 

# Esperar o broker subir
sleep 10

# Iniciar o Gateway
python3 gateway/main.py &

# Iniciar Sensores
python3 sensors/luminosity_sensor.py &
python3 sensors/temperature_sensor.py &

# Iniciar Atuadores (Lâmpada e Ventilador)
python3 actuators/lamp_server.py &
python3 actuators/fan_server.py &

# Iniciar Cliente
python3 client/client_app.py &
