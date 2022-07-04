# XtraMathBot

# Table of contents
1. [About](#about)
    * [Built With](#builtwith)
2. [Getting Started](#gettingstarted)
    * [Installation](#installation) 

# About <a name="about"></a>

This is my xtra math bot I made using Slenium, Pytesseract, and OpenCV. There are 2 parts to this project: Logging in and Answering Questions

## Logging In

First, the bot logs in with selenium, a module which can minipulate key presses and mouse clicks. The bot enters your email, student name, and pin code into the text boxes and presses enter, continuing onto the questions phase. 


After it logs in your account and gets to the questions, it takes 2 screenshots (the first number and bottom number) and takes a screen shot of them and saves it in the 
folder you specified with the specified name. Then it uses some post processing and uses a moduale called pytesseract and openCV to read the images and turn them into 
strings. Then it turns the string into integers and it adds them two together and types in the answer with keyboard automation. Note that you will have to run program 3 or 4 times. After it is done and it shows ur progress and report on how many questions you got right and wrong, exit out of the webpage and run code until it says you got a certificate. This code is written is written in python.
