#!/bin/bash

docker-compose build 
gnome-terminal -- bash -c "docker-compose up flask; exec bash" 
gnome-terminal -- bash -c "python3 spammer.py; exec bash"
sleep 3
gnome-terminal -- bash -c "python3 rps_origin.py http://127.0.0.1:9881; exec bash"
sleep 100
docker kill strawberry
docker kill orange
sleep 100
docker start strawberry
docker start orange




