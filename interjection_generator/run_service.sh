#!/bin/bash

# Start the Interjection Generator server in Prod

echo 'Starting Interjection Generator server...'
export FLASK_APP=interjection_generator.py
flask run -h localhost -p 5002
