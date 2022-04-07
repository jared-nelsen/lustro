# Console App

import requests
import uuid
from datetime import datetime, timedelta
import json

from data import getQuestionDataset

# This app contains functionality for local development

def generateUUID():
    return uuid.uuid4().hex

# ----------------------------------------------------------------------------------------------------
# URLs
# ----------------------------------------------------------------------------------------------------
lustro_api_url = "http://localhost:5001"
createInterviewPlanURI = lustro_api_url + "/create-interview-plan"
retrieveInterviewPlanURI = lustro_api_url + "/retrieve-interview-plan"
createInterviewURI = lustro_api_url + "/create-interview"
retrieveInterviewURI = lustro_api_url + "/retrieve-interview"
updateInterviewURI = lustro_api_url + "/persist-interview"

lustro_interviewer_local = "http://localhost:5555/#/land"

# ----------------------------------------------------------------------------------------------------
# Interview Testing
# ----------------------------------------------------------------------------------------------------

def createDefaultInterviewPlan():
    questions = []
    questions.append("What's up?")
    questions.append("How's it going?")
    questions.append("What's new?")
    questions.append("Thanks! We are done!")
    params = {"questions": json.dumps(questions)}
    r = requests.get(createInterviewPlanURI, params=params)
    return json.loads(r.text)['id']

def createRandomInterviewPlan():
    questions = getQuestionDataset()
    params = {"questions": json.dumps(questions)}
    r = requests.get(createInterviewPlanURI, params=params)
    return json.loads(r.text)['id']

def retrieveInterviewPlan():
    planId = input("What is the interview plan ID to retrieve?\n")
    params = {"id": planId}
    # Make the request
    r = requests.get(retrieveInterviewPlanURI, params=params)
    print(r.text)

def createDefaultInterview():
    # Generate the default interview plan
    planId = createDefaultInterviewPlan()
    # Create the request params
    params = {"interview_plan_id": planId}
    r = requests.get(createInterviewURI, params=params)
    interviewID = json.loads(r.text)['id']
    print(lustro_interviewer_local + "?id=" + interviewID)
    return interviewID

def createRandomInterviewFromTestData():
    # Generate a random interview plan
    planId = createRandomInterviewPlan()
    # Create the request params
    params = {"interview_plan_id": planId}
    r = requests.get(createInterviewURI, params=params)
    interviewID = json.loads(r.text)['id']
    print(lustro_interviewer_local + "?id=" + interviewID)
    return interviewID
    
def retrieveInterviewByID(interviewId):
    params = {"id": interviewId}
    r = requests.get(retrieveInterviewURI, params=params)
    return r.text
    
# ----------------------------------------------------------------------------------------------------
# Interview Simulation    
# ----------------------------------------------------------------------------------------------------

class Interview():
    def __init__(self, interviewJson):
        interview = json.loads(interviewJson)
        self.interview_id = interview['id']
        self.interview_plan_id = interview['interview_plan_id']
        self.question_index = interview['question_index']
        self.questions = interview['questions']
        self.responses = interview['responses']
        self.response_urls = interview['response_urls']
        self.question_audio_urls = interview['question_audio_urls']
        self.answers = []

    def update(self, answer):
        self.answers.append(answer)
        self.question_index = int(self.question_index) + 1
        params = {'id': self.interview_id,
                  'interview_plan_id': self.interview_plan_id,
                  'question_index': self.question_index,
                  'questions': self.questions,
                  'responses': self.responses,
                  'response_urls': self.response_urls,
                  'question_audio_urls': self.question_audio_urls,
                  'answers': self.answers}
        r = requests.get(updateInterviewURI, params=params)
        
    def prnt(self):
        print("-----------------------------------------------")
        print("Interview:")
        print("----------")
        print("ID = " + self.interview_id)
        print("Interview Plan ID = " + self.interview_plan_id)
        print("Question Index = " + str(self.question_index))
        print("Responses")
        for x in self.responses:
            print(" " + x)
        print("Response Urls")
        for x in self.response_urls:
            print(" " + x)
        print("Question Audio Urls = ")
        for x in self.question_audio_urls:
            print(" " + x)
        print("Questions = ")
        for x in self.questions:
            print(" " + x)
        print("Answers = ")
        for x in self.answers:
            print(" " + x)
        print("-----------------------------------------------\n")

def simulateDefaultInterview():
    interviewId = createDefaultInterview()
    interviewJson = retrieveInterviewByID(interviewId)
    interview = Interview(interviewJson)

    for question in interview.questions:
        answer = input(question + "\n")
        interview.update(answer)
        interview.prnt()

    print("\nDone with interview!")

def simulateRandomInterview():
    interviewId = createRandomInterviewFromTestData()
    interviewJson = retrieveInterviewByID(interviewId)
    interview = Interview(interviewJson)

    for question in interview.questions:
        answer = input(question + "\n")
        interview.update(answer)
        interview.prnt()
        
def simulateInterview():
    prompt = "\nWhat type of interview would you like to simulate?\n"
    prompt += "1. Default Interview\n"
    prompt += "2. Random Interview\n"
    selection = input(prompt)

    if selection == "1":
        simulateDefaultInterview()
    elif selection == "2":
        simulateRandomInterview()
        
# ----------------------------------------------------------------------------------------------------


prompt = "What would you like to do?\n"
prompt += "1. Create Default Interview Plan\n"
prompt += "2. Retrieve an Interview Plan by ID\n"
prompt += "3. Create Default Interview\n"
prompt += "4. Create Random Interview\n"
prompt += "5. Simulate Interview\n"
selection = input(prompt)

if selection == "1":
    createDefaultInterviewPlan()
elif selection == "2":
    retrieveInterviewPlan()
elif selection == "3":
    createDefaultInterview()
elif selection == "4":
    createRandomInterviewFromTestData()
elif selection == "5":
    simulateInterview()
