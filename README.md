# Lustro
  - Jared Nelsen Jan 17th, 2021
-------------------------------------------------------------------------------------------------------------------------------------

# Concepts

  - Interview - The Interview is the primary unit of Lustro. An Interview is administered by an Organization to an Interviewee.
                Interviews have a Topic associated with them. This Topic is a configurable unit that is defined at a Product
                level and is given to Lustro as metadata about an Interview. Interviews are ephemeral but their result, which
                is an Interview Presentation is stored and should then be accessible.

                Interviews are scheduled and managed. They have an Interview Plan associated with them.
                
  - Topic - An Interview Topic is metadata associated with each interview. This metadata gives Lustro context around what
            sort of Interview is taking place. They are defined at a Product level and are given to Lustro for various
            purposes such as administration, asynchronous API communication, and configuration. For instance, an Interview may
            be scheduled by a Product and the Product would then need to know the results of the interview and update itself
            accordingly so Lustro must know who and what to report back to the Product. 
                 - Examples:
                        1. Who is administering this Interview
                        2. When is this Interview is supposed to happen
                        3. How should the interviewee be contacted
                        4. What product should be updated with the results.
           - The concept of a Topic is still under development. It's purpose is to be the interface between Products and Lustro.
           - However, because I have not defined any Products it is a little unclear how it should act.
           
  - The Interview Plan - Interview plans are stored and managed. They are comprised of a vector of question IDs. Questions are
                         members of interview plans.
                         
  - Question - Questions are stored units. They are members of an Interview Plan. They are defined as the Interview Plan is written.
               I might do well to keep questions stored as part of the Interview Plan.
               
  - Baseline Question - Baseline Questions are questions that are defined by the Organization for each Interview. These are apposed
                        to the Interjections asked by Lustro. Organizations are encouraged to ask Baseline Questions in a Who,
                        What, When, Where, How, Why format.
                        
  - Interjection - Interjections are follow up questions that are generated based on the answer a user gives for a question in the
                   Interview Plan. Interjections and their Answers are stored and presented back to the Organization in the
                   Interview Presentation for each Interview Plan.
                   
  - Interview Presentation - Interview Presentations are the results of an Interview Plan that are given back to the Organization.
                             There are many Interview Presentations for each Interview Plan.
                             
  - The Organization - The Organization is the entity and primary customer. It has the ability to create, modify, delete, and
                       administer Interviews.
                       
# Architecture Notes

  The Central units of Lustro are:

               The Units of Lustro are then:
                   - Notification Generator
                     - Sends communications about scheduled Interviews
                   - Lustro API
                     - The central API that manages interviews, interview plans, and
                       the administration of interviews
                   - Interjection Generator
                     - Responsible for reading answers and making potential interjections
                   - Interviewer
                     - The Flutter App that carries out the interview

## Speech recognition architecture

   - Speech recognition will use the Google Speech to Text API
     - Plugin https://pub.dev/packages/google_speech
     - Streaming option
   - The response can then be set on the interview and sent back to the Lustro API
   - The response can then be sent to the Interjection generator to see if an interjection is required

## Flow

   1. The Interview starts and the interview is initialized
   2. A question is asked
   3. The response is set on the interview on its own field and as the corresponding answer to that question
   4. The Interview object is updated and sent to the server
   5. The back end persists the interview
   6. The back end attempts to get an interjection from the interjection generator
   7. If there is one then the interjection is set as the next question and the conversation index is not advanced
   8. If there is not one then the conversation index is advanced and the response is sent back to the client
   9. This process repeats until the end of the interview

      ** figure out how greetings and goodbyes are handled
     
-------------------------------------------------------------------------------------------------------------------------------------

# Ports

  - Interview Plan Manager: 5001
  
-------------------------------------------------------------------------------------------------------------------------------------

# Links

## Flutter

    - Dockerizing Flutter apps: https://blog.codemagic.io/how-to-dockerize-flutter-apps/
    - Video detailing Flutter web release strategies (Dart Web servers): https://www.youtube.com/watch?v=yoAdPgw7YLM

## Kubernetes

    - Developing services locally: https://cloud.google.com/community/tutorials/developing-services-with-k8s
    
## Docker

    - Install Docker on Linux Mint: https://computingforgeeks.com/install-docker-and-docker-compose-on-linux-mint-19/
    - User Permission Denied Fix: https://stackoverflow.com/questions/48957195/how-to-fix-docker-got-permission-denied-issue

## Dart

    - Simple Dart http servers: https://dart.dev/tutorials/server/httpserver

## Flask

    - https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
    
## Firestore

    - Install FireStore https://firebase.google.com/docs/cli#install-cli-mac-linux
    - Install Local Emulator Suite - https://firebase.google.com/docs/emulator-suite/install_and_configure
    - Use Python for local database - https://stackoverflow.com/questions/54868011/how-to-use-google-cloud-firestore-local-emulator-for-python-and-for-testing-purp
    - Start local emulator
        - firebase emulators:start
        - Hosted on port 4000
    - Firestore and Flask - https://gaedevs.com/blog/how-to-use-the-firestore-emulator-with-a-python-3-flask-app

## Kubernetes

   - Logging: https://logz.io/blog/a-practical-guide-to-kubernetes-logging/
   - Install Minikube: https://phoenixnap.com/kb/install-minikube-on-ubuntu

## Clojure

   - Ring: https://www.baeldung.com/clojure-ring
   - Compojure: https://github.com/weavejester/compojure/wiki/Getting-Started
                https://github.com/weavejester/compojure-example
                https://kendru.github.io/restful-clojure/2014/02/19/getting-a-web-server-up-and-running-with-compojure-restful-clojure-part-2/
-------------------------------------------------------------------------------------------------------------------------------------

## Development Environment Setup

   - TODO

-------------------------------------------------------------------------------------------------------------------------------------
## A note on question types

Ideally an interview is an organic experience with different types of questions. This is something I can emulate.

Types of questions:

1. Dichotomous Yes or No questions
2. Elaborative questions
3. Multiple Choice Questions
4. Text Slider Questions
5. Open Ended Questions
6. Thumbs Up Thumbs Down Question
7. User entered question
