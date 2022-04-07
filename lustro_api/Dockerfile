# Lustro Dockerfile

# Install Dependencies
FROM debian:latest AS build-env
RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN apt-get clean

# Install Python Dependencies
RUN pip3 install Flask flask_cors Datetime requests mock google-cloud-firestore google-cloud-storage firebase firebase_admin testresources python-dateutil

# Copy the app files
COPY . /usr/local/bin/app
WORKDIR /usr/local/bin/app

# Copy the Google credentials file
COPY ./firebase/check-in-app-test-32264ecd3d50.json /usr/local/bin/app
# Set it as an environment variable
ENV GOOGLE_APPLICATION_CREDENTIALS /usr/local/bin/app/check-in-app-test-32264ecd3d50.json

# Set the service startup script as executable
RUN ["chmod", "+x", "/usr/local/bin/app/run_service.sh"]

# Start the notification service
ENTRYPOINT ["/usr/local/bin/app/run_service.sh"]