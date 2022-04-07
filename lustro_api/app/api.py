import json
import requests
import uuid
import base64

from firebase_admin import storage
from app import response as responder
from app import db

speechSynthesisUrl = 'https://texttospeech.googleapis.com' + '/v1beta1/text:synthesize'
headers = {'X-Goog-Api-Key': "AIzaSyAse3iwQUjsEAdBvN8OxZoTjKu2mvryCa0"}
def audioSynthesisConfig(text):
    config = {'input': {'text': text}, 
              'voice': {'name': 'en-GB-Standard-B', 
                        'languageCode': 'en-GB'},
              'audioConfig': {'audioEncoding': 'MP3'}}
    return json.dumps(config)

def generateUUID():
    return uuid.uuid4().hex

def createInterviewPlan(uuid, questions, question_audio_urls, responsesMap):
    # Unpack the response data
    responses = responsesMap['responses']
    responseUrls = responsesMap['response_urls']
    # Make the document
    interview_plan = {'id': uuid, 
                      'questions': questions,
                      'question_audio_urls': question_audio_urls,
                      'responses': responses,
                      'response_urls': responseUrls}
    # Get the document reference
    ref = db.collection('interview_plan').document(uuid)
    # Set the document
    ref.set(interview_plan)

def retrieveInterviewPlan(id):
    # Create the reference
    ref = db.collection('interview_plan').document(id)
    # Get the document
    doc = ref.get()
    # Return the json
    return json.dumps(doc.to_dict())

def persistInterview(interviewJson):
    # Load the interview
    interview = json.loads(interviewJson)
    # Get the id of the interview
    id = interview['id']
    # Get the document reference
    doc = db.collection('interview').document(id)
    # Set the data
    doc.set(interview)

def retrieveInterview(id):
    # Create the reference
    ref = db.collection('interview').document(id)
    # Get the document
    doc = ref.get()
    # Return the json
    return doc.to_dict()

def synthesizeQuestion(question):
    # Create the synthesization config for the question
    synthConfig = audioSynthesisConfig(question)
    # Make the call to sythesize the question
    synthesizedFile = requests.post(speechSynthesisUrl, 
                                    data=synthConfig, 
                                    headers=headers)
    # Jsonify response
    synthesizedFile = json.loads(synthesizedFile.text)
    # Get audio content from json
    synthesizedFile = synthesizedFile['audioContent']
    # Decode the synthesized audio
    synthesizedFile = base64.b64decode(synthesizedFile)
    # Create a uuid for the audio
    uuid = generateUUID()
    # Create the bucket
    bucket = storage.bucket()
    # Create the audio blob
    blob = bucket.blob(uuid)
    # Upload the audio
    blob.upload_from_string(synthesizedFile)
    # Make the blob public
    blob.make_public()
    # Return the url to the file
    return blob.public_url

def synthesizeQuestions(questions):
    # Define the list of question urls to return
    questionUrls = []
    # For each question
    for question in questions:
        # Synthesize, upload, and get the url
        questionUrl = synthesizeQuestion(question)
        # Add the url to the collection
        questionUrls.append(questionUrl)
    # Return the list of question urls
    return questionUrls

def synthesizeResponse():
    # Generate a response to the response of the user
    generatedResponse = responder.generateResponse()
    # Create the synthesization config for the generated reponse
    synthConfig = audioSynthesisConfig(generatedResponse)
    # Make the call to synthesize the reponse
    synthesizedFile = requests.post(speechSynthesisUrl, 
                                    data=synthConfig, 
                                    headers=headers)
    # Jsonify response
    synthesizedFile = json.loads(synthesizedFile.text)
    # Get audio content from json
    synthesizedFile = synthesizedFile['audioContent']
    # Decode the synthesized audio
    synthesizedFile = base64.b64decode(synthesizedFile)
    # Create a uuid for the audio
    uuid = generateUUID()
    # Create the bucket
    bucket = storage.bucket()
    # Create the audio blob
    blob = bucket.blob(uuid)
    # Upload the audio
    blob.upload_from_string(synthesizedFile)
    # Make the blob public
    blob.make_public()
    # Set the url to the file
    url = blob.public_url
    # Make the response map object
    reponseMap = {
        'response_url': url,
        'response': generatedResponse
    }
    # Return the response map
    return reponseMap

def synthesizeResponses(count):
    # Define the list of responses and urlsto reeturn
    responses = []
    response_urls = []
    # While in the range
    for i in range(count):
        # Synthesize, upload, and get the response string and url
        synthesisResponse = synthesizeResponse()
        # Add the response and url to the respective lists
        responses.append(synthesisResponse['response'])
        response_urls.append(synthesisResponse['response_url'])
    # Define a map to return
    returnMap = {
        'responses': responses,
        'response_urls': response_urls
    }
    return returnMap