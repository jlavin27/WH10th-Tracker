# WH10th-Tracker
Game tracker for 10th Edition of Warhammer 40k

This is a basic game tracker for 40k. 
Currently can keep track of:
  -Turn number
  -Primary Objective
  -Mission Rule
  -Deployment
  -Attacker and Defender
  -Secondary Objective (Right now only supports 2 fixed or tatical) (TODO add dynamic support depending on Mission rule, Know there is one that requires 3)
  -Victory Points (Seperated by primary and secondary)
  -Command Points
  -Gambit

As it currently stands the tracker is basic and very basic looking and only aids to tack key details of the game. It currently can track the 6 example combat patrols, Only War and Leviathan games.
Leviathan games have two options Leviathan (Custom) which allows user to pick Primary Objective, Mission rule and Deployment and Leviathan which will randomly generate these three.

I plan on adding a few features to automate and clarify scoring to users as possible such as auto point calculation and descriptions of each rule/objective.

Tried to keep requirements to run as simple as possible to ensure it can run on a varity of devices. I currently use on a Raspberry Pi4 on Python 3.11 but have also run on Windows Laptop and and Steam deck using Python 3.10
  -Python 3.10 or greater with Tkinter (TK Should come with most prepackaged installations but can be sometimes be missing if installing python from source)
