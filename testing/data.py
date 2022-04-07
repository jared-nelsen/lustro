import requests

lustro_api_url = "http://localhost:5001"
generateTestDataURI = lustro_api_url + "/persist-test-questions"

questions = ["How do you feel about yellow pants?",
             "Did you hear what Trump said the other day?",
             "What is your favorite thing to do on the weekend?",
             "Can you believe its not butter?",
             "Is Lustro the coolest thing this decade will ever produce?",
             "What do you think about my new hair cut?",
             "Are you qualified to talk to a robot?",
             "Pandemic? What pandemic?",
             "Have you ever tasted electrons? They are delicious!",
             "Have you met my brother number five?",
             "Have you heard of the internet?",
             "Thanks! We are done!"]

def getQuestionDataset():
    return questions
