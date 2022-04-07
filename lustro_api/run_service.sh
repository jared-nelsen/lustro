#!/bin/bash

# Start the Lustro API server in Prod

echo 'Starting Lustro API server...'
export FLASK_APP=lustro_api.py
flask run -h localhost -p 5001
