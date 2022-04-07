import 'package:interviewer/landing_page.dart';
import 'package:flutter/material.dart';

import 'package:firebase_core/firebase_core.dart';

import 'home_page.dart';

void main() {
  runApp(Interviewer());
}

class Interviewer extends StatefulWidget {
  @override
  InterviewerState createState() => InterviewerState();
}

class InterviewerState extends State<Interviewer> {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      initialRoute: HomePage.routeName,
      routes: {
        HomePage.routeName: (context) => HomePage(),
      },
      onGenerateRoute: (settings) {
        String specificRoute = settings.name.substring(0, 5);

        if (specificRoute == LandingPage.routeName) {
          String sessionID = Uri.parse(settings.name).queryParameters['id'];

          // if (sessionID == null ||
          //     sessionID.isEmpty ||
          //     sessionID.length != 32) {
          //   //Maybe navigate to an error screen
          //   return MaterialPageRoute(
          //     builder: (context) {
          //       return HomePage();
          //     },
          //   );
          // }

          return MaterialPageRoute(
            builder: (context) {
              return LandingPage(sessionID);
            },
          );
        }
      },
    );
  }

  _initializeFlutterFire() async {
    await Firebase.initializeApp();
  }

  @override
  void initState() {
    _initializeFlutterFire();
    super.initState();
  }
}
