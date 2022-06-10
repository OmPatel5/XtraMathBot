from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.common.action_chains import ActionChains
from pynput.keyboard import Key, Controller
import pyautogui
from PIL import Image
import time
import pytesseract
import cv2
from matplotlib import pyplot as plt
import numpy as np



#note that u have to run program 3 or 4 times after it is done and it shows ur progress and report on how many questions you got write and wrong exit out of it after and run code until it says u beat it
PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://xtramath.org/#/signin/student_other")
driver.maximize_window()

time.sleep(5)
elem = WebDriverWait(driver, 120, 1).until(
        expect.visibility_of_element_located(

        (By.XPATH, "//input[@placeholder='Parent or Teacher']")))

elem.click()
elem.send_keys("omp091216@gmail.com")

text = WebDriverWait(driver, 120, 1).until(
        expect.visibility_of_element_located(
        (By.XPATH, "(//input[@name='displayName'])[2]")))
text.click()
text.send_keys("GG")

pin = WebDriverWait(driver, 120, 1).until(
        expect.visibility_of_element_located(
        (By.XPATH, "(//input[@name='pin'])[3]")))
pin.click()
pin.send_keys("4195")

time.sleep(3)
pin.send_keys(Keys.RETURN)

time.sleep(2)
keyboard = Controller()
for i in range(2):
        time.sleep(2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

time.sleep(4)
for i in range(200):
    time.sleep(0.48)
    screenshot = pyautogui.screenshot(region=(700,320,400,160))
    screenshot.save(r'C:\Users\omp16\Documents\new_folder\topno.png')

    # this is screenshot number 1 (top No.)

    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

    img = cv2.imread(r"C:\\Users\omp16\\Documents\\new_folder\\topno.png")
    img = cv2.resize(img,(0,0),fx=2,fy=2)
    img = cv2.GaussianBlur(img,(11,11),0)
    img = cv2.medianBlur(img,9)
    

    ocr1 = pytesseract.image_to_string(img, lang='eng', config='--psm 6-c tessedit_char_whitelist=0123456789')    
    print(ocr1)
    ocr1_split = ocr1.split()
    print(ocr1_split)
    ocr1_string = ocr1_split[0]
    if ocr1_string == 'O':
        ocr1_string = '0'
    print(ocr1_string)
    ocr1 = int(ocr1_string) 
    
        
   
    #IMAGE 2

    screenshot = pyautogui.screenshot(region=(800,465,400,180))
    screenshot.save(r'C:\Users\omp16\Documents\new_folder\bottomno.png')

    # this is screenshot number 2 (bottom No.)

    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

    img2 = cv2.imread(r"C:\\Users\omp16\\Documents\\new_folder\\bottomno.png")

    img2 = cv2.resize(img2,(0,0),fx=2,fy=2)
    img2 = cv2.GaussianBlur(img2,(11,11),0)
    img2 = cv2.medianBlur(img2,9)

    img2 = Image.fromarray(img2)
    ocr2 = pytesseract.image_to_string(img2, lang='eng', config='--psm 8-c tessedit_char_whitelist=0123456789')
    if ocr2 != '+5\n':
        ocr2 = pytesseract.image_to_string(img2, lang='eng', config='--psm 7-c tessedit_char_whitelist=0123456789')
        ocr2.strip(' +')
    else:
        ocr2 = '5'
    ocr2 = ocr2.strip(' +')
    ocr2_split = ocr2.split()
    ocr2_string = ocr2_split[0]
    
    if ocr2_string == 'O':
        ocr2_string = '0'
    
    if ocr2_string == 'f':
        ocr2_string = '7'
    

    ocr2 = int(ocr2_string)
    
    result = ocr1 + ocr2
    
    new_result = str(result)
    
    keyboard.type(new_result)

