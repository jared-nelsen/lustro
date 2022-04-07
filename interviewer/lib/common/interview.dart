import 'dart:convert';

import 'urls.dart';
import 'package:http/http.dart' as http;

class Interview {
  String interviewID;
  String interviewPlanID;
  int questionIndex;
  List<String> questions = [];
  List<String> questionAudioUrls = [];
  List<String> responses = [];
  List<String> responseUrls = [];
  List<String> answers = [];

  Interview();

  init(String interviewID) async {
    this.interviewID = interviewID;
    await _pull();
    _print();
  }

  update(String answer) async {
    this.answers.add(answer);
    questionIndex++;
    await _persist();
    await _pull();
    _print();
  }

  String getCurrentQuestion() {
    return this.questions.elementAt(questionIndex);
  }

  String getCurrentQuestionAudioURL() {
    return this.questionAudioUrls.elementAt(questionIndex);
  }

  String getCurrentResponse() {
    return this.responses.elementAt(questionIndex);
  }

  String getCurrentResponseURL() {
    return this.responseUrls.elementAt(questionIndex);
  }

  _persist() async {
    var uri = Uri.parse(URLs.PERSIST_INTERVIEW_URL);

    uri = uri.replace(
      queryParameters: <String, dynamic>{
        URLs.INTERVIEW_QUERY: jsonEncode(this.toJson())
      },
    );

    await http.get(uri);
    //Can check for success here
  }

  _pull() async {
    var uri = Uri.parse(URLs.RETRIEVE_INTERVIEW_URL);

    uri = uri.replace(
      queryParameters: <String, dynamic>{
        URLs.INTERVIEW_ID_QUERY: this.interviewID
      },
    );

    final response = await http.get(uri);

    fromJson(response.body);
  }

  Map<String, dynamic> toJson() => {
        'id': interviewID,
        'interview_plan_id': interviewPlanID,
        'question_index': questionIndex,
        'questions': questions,
        'question_audio_urls': questionAudioUrls,
        'responses': responses,
        'response_urls': responseUrls,
        'answers': answers
      };

  fromJson(String incoming) {
    Map<String, dynamic> json = jsonDecode(incoming);
    this.interviewID = json['id'];
    this.interviewPlanID = json['interview_plan_id'];
    var questionIndexVar = json['question_index'];
    if (questionIndexVar is String) {
      this.questionIndex = int.parse(questionIndexVar);
    } else {
      this.questionIndex = questionIndexVar;
    }
    this.questions = List.from(json['questions']);
    this.questionAudioUrls = List.from(json['question_audio_urls']);
    this.responses = List.from(json['responses']);
    this.responseUrls = List.from(json['response_urls']);
    List<dynamic> answersJson = json['answers'];
    if (answersJson != null) {
      this.answers = List.from(answersJson);
    }
  }

  _print() {
    print("------------------------------------------------------------");
    print("ID = " + this.interviewID);
    print("Interview Plan ID = " + this.interviewPlanID);
    print("Question Index = " + this.questionIndex.toString());
    print("Questions:");
    for (var q in this.questions) {
      print(" " + q);
    }
    print("Question Audio Urls");
    for (var q in this.questionAudioUrls) {
      print(" " + q);
    }
    print("Responses");
    for (var q in this.responses) {
      print(" " + q);
    }
    print("Response Urls");
    for (var q in this.responseUrls) {
      print(" " + q);
    }
    print("Answers:");
    if (this.answers == null) {
      return;
    }
    for (var a in this.answers) {
      print(" " + a);
    }
    print("------------------------------------------------------------");
  }
}
