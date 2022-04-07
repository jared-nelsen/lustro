from flask import jsonify, make_response, request, json, g
import dateutil.parser
import json
import uuid
import requests

from app import app
from app import api as api

def generateUUID():
    return uuid.uuid4().hex

@app.route('/create-interview-plan', methods=['GET', 'POST'])
def createInterviewPlan():
    # Create the id
    uuid = generateUUID()
    # Get the question data
    questions = json.loads(request.args.get('questions'))
    # Synthesize audio files for each question and store the urls here
    question_audio_urls = api.synthesizeQuestions(questions)
    # Generate the responses that will be used for each question
    responsesMap = api.synthesizeResponses(len(questions))
    # Create the interview plan
    api.createInterviewPlan(uuid, questions, question_audio_urls, responsesMap)
    # Form the response body
    response_body = {
        "id": uuid
    }
    return make_response(jsonify(response_body), 200)
    
@app.route('/retrieve-interview-plan', methods=['GET', 'POST'])
def retrieveInterviewPlan():
    # Get the id
    uuid = request.args.get('id')
    # Retrieve the interview plan
    interview_plan = api.retrieveInterviewPlan(uuid)
    # Form the response body
    response_body = {
        "interview_plan": interview_plan
    }
    return make_response(jsonify(response_body), 200)

@app.route('/create-interview', methods=['GET', 'POST'])
def createInterview():
    # Create an id for the interview
    uuid = generateUUID()
    # Get the interview plan id
    interview_plan_id = request.args.get('interview_plan_id')
    # Retrieve the interview plan
    interview_plan = json.loads(api.retrieveInterviewPlan(interview_plan_id))
    # Get the questions from the interview plan
    questions = interview_plan['questions']
    # Get the question audio urls from the interview plan
    question_audio_urls = interview_plan['question_audio_urls']
    # Get the responses from the interview plan
    responses = interview_plan['responses']
    # Get the response urls from the interview plan
    response_urls = interview_plan['response_urls']
    # Create the interview
    interview = {'id': uuid,
                 'interview_plan_id': interview_plan_id,
                 'question_index': 0,
                 'questions': questions,
                 'question_audio_urls': question_audio_urls,
                 'responses': responses,
                 'response_urls': response_urls,
                 'answers': []
                }
    # Perist the interview
    api.persistInterview(json.dumps(interview))
    # Return the id of the interview
    response_body = {
        "id": uuid
    }
    return make_response(jsonify(response_body), 200)

@app.route('/persist-interview', methods=['GET', 'POST'])
def persistInterview():
    # Get the interview json
    interviewJson = request.args.get('interview')
    # Persist it
    api.persistInterview(interviewJson)
    # For the response body
    response_body = {
        "Success" : 200
    }
    return make_response(jsonify(response_body), 200)

@app.route('/retrieve-interview', methods=['GET', 'POST'])
def retrieveInterview():
    # Get the id
    id = request.args.get('id')
    # Get the interview by id
    interview = api.retrieveInterview(id)
    # The reponse body is the interview
    return make_response(jsonify(interview), 200)
