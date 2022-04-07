import 'package:flutter/material.dart';

class Utilities {
  static showConfirmationDialog(
      BuildContext context, String title, String confirmationText) {
    AlertDialog alert = AlertDialog(
      title: Text(title),
      content: Text(confirmationText),
      actions: [
        RaisedButton(
          child: Text("OK"),
          onPressed: () {
            Navigator.of(context).pop();
          },
        ),
      ],
    );

    showDialog(
      context: context,
      builder: (BuildContext context) {
        return alert;
      },
    );
  }

  static showFailureDialog(BuildContext context, String failureMessage) {
    AlertDialog alert = AlertDialog(
      title: Text("Failure"),
      content: Text(failureMessage),
      actions: [
        RaisedButton(
          child: Text("OK"),
          onPressed: () {
            Navigator.of(context).pop();
          },
        ),
      ],
    );

    showDialog(
      context: context,
      builder: (BuildContext context) {
        return alert;
      },
    );
  }
}
