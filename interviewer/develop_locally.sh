#!/bin/bash
# Develop the Interviewer Front End Locally

echo 'Interviewer Front End starting...'
fuser -k 5555/tcp
gnome-terminal -e 'sh -c "echo ''Interviewer Front End console...''; flutter build web; flutter run -d chrome --web-port 5555"'
