#!/bin/bash

# Starts the local development environment

# Start local Firebase
cd firebase
sh ./start_firebase_emulator.sh
cd ..

# Start the Lustro API
cd lustro_api
sh ./develop_locally.sh
cd ..

# Start the Interjection Generator
cd interjection_generator
sh ./develop_locally.sh
cd ..

# Start the Interviewer Front End
cd interviewer
sh ./develop_locally.sh
cd ..
