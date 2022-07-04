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
text.send_keys("test")

pin = WebDriverWait(driver, 120, 1).until(
        expect.visibility_of_element_located(
        (By.XPATH, "(//input[@name='pin'])[3]")))
pin.click()
pin.send_keys("6802")

time.sleep(3)
pin.send_keys(Keys.RETURN)

time.sleep(2)
keyboard = Controller()
for i in range(2):
        time.sleep(2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

time.sleep(4)
for i in range(100):
    time.sleep(0.48) 
    
    #IMAGE 2

    screenshot = pyautogui.screenshot(region=(800,465,400,150))
    screenshot.save(r'C:\Users\omp16\Documents\Python Projects\XtraMath\bottomno.png')

    # this is screenshot number 2 (bottom No.)

    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

    img2 = cv2.imread(r"C:\\Users\omp16\\Documents\\Python Projects\\XtraMath\\bottomno.png")

    img2 = cv2.resize(img2,(0,0),fx=2,fy=2)
    img2 = cv2.GaussianBlur(img2,(11,11),0)
    img2 = cv2.medianBlur(img2,9)

    img2 = Image.fromarray(img2)
    ocr = pytesseract.image_to_string(img2, lang='eng', config='--psm 7-c tessedit_char_whitelist=0123456789')
    print(ocr)
    ocr_split = ocr.split(")")
    print(ocr_split)
    ocr1_string = ocr_split[0]
    ocr2_split = ocr_split[1]
    ocr2_strip = ocr2_split.strip('\n')
    ocr2_string = ocr2_strip.strip()


    print(ocr1_string)

    print(ocr2_string)
    print(ocr2_split)
    
    if ocr2_string == 'O':
        ocr2_string = '0'
    
    if ocr2_string == 'Tf':
        ocr2_string = '7'

    if ocr2_string == '/':
        ocr2_string = '7'

    if ocr2_string == 'Q':
        ocr2_string = '0'
    
    if ocr2_string == 'f':
        ocr2_string = '7'
    
    if ocr1_string == 'O':
        ocr1_string = '0'
    
    if ocr1_string == 'Tf':
        ocr1_string = '7'

    if ocr1_string == '/':
        ocr1_string = '7'

    if ocr1_string == 'Q':
        ocr1_string = '0'
    
    if ocr1_string == 'f':
        ocr1_string = '7'
    
    if open(r"C:\\Users\omp16\\Documents\\Python Projects\\XtraMath\\bottomno.png","rb").read() == open(r"C:\\Users\omp16\\Documents\\Python Projects\\XtraMath\\1.png","rb").read():
        ocr1_string = 1
        ocr2_string = 1

    ocr1 = int(ocr1_string)
    ocr2 = int(ocr2_string)

    

    if ocr1 == 0 or ocr2 == 0:
        result = 0
    else:
        result = ocr2 / ocr1
    
    new_result = str(result)
    
    keyboard.type(new_result)

