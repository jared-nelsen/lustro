#!/bin/bash

# Develop Lustro API Locally

echo 'Starting Lustro API server...'
fuser -k 5001/tcp
gnome-terminal -e 'sh -c "echo ''Lustro API server...''; export FLASK_APP=lustro_api.py; flask run -h localhost -p 5001;"'