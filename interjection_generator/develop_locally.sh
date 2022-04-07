#!/bin/bash

# Develop Interjection Generator Locally

echo 'Starting Interjection Generator server...'
fuser -k 5002/tcp
gnome-terminal -e 'sh -c "echo ''Interjection Generator server...''; export FLASK_APP=interjection_generator.py; flask run -h localhost -p 5002;"'