# XtraMathBot

# Table of contents
1. [About](#about)
    * [Built With](#builtwith)
2. [Getting Started](#gettingstarted)
    * [Installation](#installation) 

# About <a name="about"></a>

This is my xtra math bot I made using Slenium, Pytesseract, and OpenCV. There are 2 parts to this project: Logging in and Answering Questions

## Logging In
https://user-images.githubusercontent.com/104532194/177196100-d5f5c637-9088-4689-b545-4b1f3189c3be.mp4
#### Video 1: Logging in Phase

First, the bot logs in with selenium, a module which can minipulate key presses and mouse clicks. The bot enters your email, student name, and pin code into the text boxes and presses enter, continuing onto the questions phase. 

## Answering the Questions

https://user-images.githubusercontent.com/104532194/177197161-88699143-3b9f-4086-b7ab-b015625a995f.mp4
#### Video 2: Answering the Questions

After the logging in phase is completed, it moves on to the answering questions phase. First, it takes 2 or 1 screenshot(s) (the top and bottom number or the whole area where the questions are in) and saves them in the path you specified. Next it uses 2 modules, pytesseract and openCV, to process and read the numbers and turn them into 
python strings. After that, the code turns the numbers into integers and it adds/subtracts/multiplies/divides them and stores it as the result. Finally, the program  types in the answer with keyboard automation using pyautogui. 

Keep the code running until it says you have completed your program.

## Built With <a name="builtwith"></a>
This program is built with the following languages:
* Python

# Getting Started <a name="gettingstarted"></a>
**To get this project running follow these steps**

## Installation <a name="installation"></a>
1. Clone the Repository
```sh
   git clone https://github.com/OmPatel5/XtraMathBotAdding.git
   ```
2. Install Selenium
```sh
   pip install selenium
   ```
3. Install Chrome WebDriver
**Install Chrome Webdriver asociated with the version of your chrome you are using**
```sh
   https://sites.google.com/a/chromium.org/chromedriver/downloads
   ```
4. Install Tesseract-OCR
**Install Tesseract-OCR with associated windows version**
```sh
   https://github.com/UB-Mannheim/tesseract/wiki
   ```
```sh
   pip install pytesseract
   ```
