from flask import Flask
from flask_cors import CORS, cross_origin

import os
import mock
from google.cloud import firestore
import google.auth.credentials

# Create the app
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

# Create the database
db = firestore.Client()

if os.getenv('GAE_ENV', '').startswith('standard'):
    # production
    db = firestore.Client()
else:
    # localhost
    os.environ["FIRESTORE_DATASET"] = "lustro"
    os.environ["FIRESTORE_EMULATOR_HOST"] = "localhost:8090"
    os.environ["FIRESTORE_EMULATOR_HOST_PATH"] = "localhost:4001/firestore"
    os.environ["FIRESTORE_HOST"] = "http://localhost:8090"
    os.environ["FIRESTORE_PROJECT_ID"] = "lustro"

    credentials = mock.Mock(spec=google.auth.credentials.Credentials)
    db = firestore.Client(project="lustro", credentials=credentials)

from app import routes