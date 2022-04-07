import 'package:audioplayers/audioplayers.dart';
import 'package:flutter/material.dart';

import 'package:interviewer/common/interview.dart';

class LandingPage extends StatefulWidget {
  static String routeName = '/land';
  String _interviewID;

  LandingPage(this._interviewID);

  @override
  _LandingPageState createState() => _LandingPageState(this._interviewID);
}

class _LandingPageState extends State<LandingPage> {
  AudioPlayer audioPlugin = AudioPlayer();

  TextEditingController _answerController = TextEditingController();

  String interviewID = "default";
  Interview interview = new Interview();
  String _currentQuestion = "default";

  _LandingPageState(this.interviewID);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Interviewer Text Landing Page"),
        leading: Container(),
      ),
      body: Container(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Text(
                  this._currentQuestion,
                  style: TextStyle(
                    fontSize: 60,
                  ),
                ),
              ],
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              crossAxisAlignment: CrossAxisAlignment.center,
              children: [
                Container(
                  width: 1000,
                  height: 100,
                  child: Center(
                    child: TextField(
                      controller: _answerController,
                      textAlign: TextAlign.center,
                      decoration: InputDecoration(
                        hintText: "Answer the question",
                        hintStyle: TextStyle(fontSize: 25),
                      ),
                      style: TextStyle(fontSize: 25),
                    ),
                  ),
                ),
              ],
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              crossAxisAlignment: CrossAxisAlignment.center,
              children: [
                Container(
                  width: 1000,
                  height: 100,
                  child: Center(
                    child: SizedBox(
                      height: 50,
                      width: 100,
                      child: RaisedButton(
                        onPressed: _submit,
                        child: Text(
                          'Submit',
                          style: TextStyle(
                            color: Colors.white,
                          ),
                        ),
                        color: Colors.blue,
                      ),
                    ),
                  ),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }

  _submit() async {
    if (interview.questionIndex == interview.questions.length - 1) {
      await speak();
      return;
    }

    await respond();
    await speak();
    await interview.update(_answerController.text);
  }

  Future speak() async {
    String questionAudioURL = interview.getCurrentQuestionAudioURL();
    await audioPlugin.play(questionAudioURL);
    String question = interview.getCurrentQuestion();
    setState(() {
      this._currentQuestion = question;
    });
  }

  Future respond() async {
    String response = interview.getCurrentResponse();
    setState(() {
      this._currentQuestion = response;
    });
    String responseAudioURL = interview.getCurrentResponseURL();
    await audioPlugin.play(responseAudioURL);
    await Future.delayed(Duration(seconds: 2));
  }

  init() async {
    await Future.delayed(Duration(seconds: 1));
    await speak();
  }

  @override
  void initState() {
    super.initState();
    interview.init(this.interviewID).then((value) {
      init();
    });
  }

  @override
  void dispose() {
    _answerController.dispose();
    super.dispose();
  }
}
