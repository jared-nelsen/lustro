from flask import Flask
from flask_cors import CORS, cross_origin

import os
import mock
from google.cloud import firestore
import google.auth.credentials
from firebase_admin import credentials as storage_creds, initialize_app

# Create the app
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

# Create the database
db = firestore.Client()

# Initialize Firebase cloud storage
cloud_storage_creds = None

if os.getenv('GAE_ENV', '').startswith('standard'):
    # production
    db = firestore.Client()
    # SET PROD CLOUD STORAGE CREDS FROM DOCKER DIR
else:
    # localhost
    os.environ["FIRESTORE_DATASET"] = "lustro"
    os.environ["FIRESTORE_EMULATOR_HOST"] = "localhost:8090"
    os.environ["FIRESTORE_EMULATOR_HOST_PATH"] = "localhost:4001/firestore"
    os.environ["FIRESTORE_HOST"] = "http://localhost:8090"
    os.environ["FIRESTORE_PROJECT_ID"] = "lustro"

    credentials = mock.Mock(spec=google.auth.credentials.Credentials)
    db = firestore.Client(project="lustro", credentials=credentials)

    # Initialize cloud storage
    # CAN DO OS.ENVIRON FOR CRED GET
    cloud_storage_creds = storage_creds.Certificate("/home/jared/Projects/lustro/firebase/lustro-1612481237849-0545b9dd697a.json")
    initialize_app(cloud_storage_creds, {'storageBucket': 'lustro-1612481237849.appspot.com'})

from app import routes