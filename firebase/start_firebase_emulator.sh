#!/bin/bash

# Start the local firebase emulator

# Kill Auth port
fuser -k 9099/tcp
# Kill Functions port
fuser -k 5060/tcp
# Kill Firestore port
fuser -k 8090/tcp
# Kill Database port
fuser -k 9000/tcp
# Kill Hosting port
fuser -k 5065/tcp
# Kill pubsub port
fuser -k 8085/tcp
# Kill UI port
fuser -k 4001/tcp

# Start the local Firebase services
echo 'Starting Firebase Local Emulator server...'
gnome-terminal -e 'sh -c "echo ''Firebase Local Emulator server...''; firebase emulators:start;"'