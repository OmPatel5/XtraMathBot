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
elem.send_keys("omisthebestandistoogood@gmail.com")

text = WebDriverWait(driver, 120, 1).until(
        expect.visibility_of_element_located(
        (By.XPATH, "(//input[@name='displayName'])[2]")))
text.click()
text.send_keys("Test")

pin = WebDriverWait(driver, 120, 1).until(
        expect.visibility_of_element_located(
        (By.XPATH, "(//input[@name='pin'])[3]")))
pin.click()
pin.send_keys("5581")

time.sleep(3)
pin.send_keys(Keys.RETURN)

time.sleep(2)
keyboard = Controller()
for i in range(2):
        time.sleep(2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

time.sleep(4)
for i in range(50):
    time.sleep(1)
    screenshot = pyautogui.screenshot(region=(700,320,400,160))
    screenshot.save(r'C:\Users\omp16\Documents\new_folder\my_screenshot.png')

    time.sleep(1)

    # this is screenshot number 1 (top No.)

    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    img = cv2.imread("my_screenshot.png")

    inverted_img = cv2.bitwise_not(img)
    cv2.imwrite('C:\\Users\\omp16\\Documents\\new_folder\\inverted.png', inverted_img)

    # cv2.imshow("inverted", inverted_img)
    # cv2.waitKey(0)

    def grayscale(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gray_image = grayscale(img)
    cv2.imwrite('C:\\Users\\omp16\\Documents\\new_folder\\gray.png', gray_image)

    # cv2.imshow("gray", gray_image)
    # cv2.waitKey(0)

    thresh, img_bw = cv2.threshold(gray_image, 180, 255, cv2.THRESH_BINARY)
    cv2.imwrite('C:\\Users\\omp16\\Documents\\new_folder\\bw_image.png', img_bw)

    # cv2.imshow("black and white image", img_bw)
    # cv2.waitKey(0)

    def noise_removal(image):
        import numpy as np
        kernel = np.ones((1, 1), np.uint8)
        image = cv2.dilate(image, kernel, iterations=1)
        kernel = np.ones((1, 1), np.uint8)
        image = cv2.erode(image, kernel, iterations=1)
        image  = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
        image = cv2.medianBlur(image, 3)
        return image

    no_noise = noise_removal(img_bw)
    cv2.imwrite('C:\\Users\\omp16\\Documents\\new_folder\\no_noise.png', no_noise)

    # cv2.imshow("no noise", no_noise)
    # cv2.waitKey(0)

    def thin_font(image):
        import numpy as np
        image = cv2.bitwise_not(image)
        kernel = np.ones((2, 2), np.uint8)
        image = cv2.erode(image, kernel, iterations=1)
        image = cv2.bitwise_not(image)
        return image

    eroded_img = thin_font(no_noise)
    cv2.imwrite('C:\\Users\\omp16\\Documents\\new_folder\\eroded_img.png', eroded_img)

    eroded_img = cv2.resize(eroded_img,(0,0),fx=2,fy=2)
    eroded_img = cv2.GaussianBlur(eroded_img,(11,11),0)
    eroded_img = cv2.medianBlur(eroded_img,9)

    # cv2.imshow("eroded img", eroded_img)
    # cv2.waitKey(0)

    img = Image.fromarray(eroded_img)
    ocr1 = pytesseract.image_to_string(img, lang='eng', config='--psm 6-c tessedit_char_whitelist=0123456789')    
    ocr1_split = ocr1.split()
    ocr1_string = ocr1_split[0]
    if ocr1_string == 'O':
        ocr1_string = '0'
    
    
    ocr1 = int(ocr1_string)
        
    #IMAGE 2

    time.sleep(1)
    screenshot = pyautogui.screenshot(region=(800,465,400,180))
    screenshot.save(r'C:\Users\omp16\Documents\new_folder\my_screenshot2.png')


    # this is screenshot number 2 (bottom No.)

    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    img2 = cv2.imread("my_screenshot2.png")

    inverted2_img = cv2.bitwise_not(img2)
    cv2.imwrite('C:\\Users\\omp16\\Documents\\new_folder\\inverted2.png', inverted2_img)

    # cv2.imshow("inverted", inverted_img)
    # cv2.waitKey(0)


    gray_image2 = grayscale(img2)
    cv2.imwrite('C:\\Users\\omp16\\Documents\\new_folder\\gray2.png', gray_image2)

    # cv2.imshow("gray", gray_image)
    # cv2.waitKey(0)

    thresh, img2_bw = cv2.threshold(gray_image2, 180, 255, cv2.THRESH_BINARY)
    cv2.imwrite('C:\\Users\\omp16\\Documents\\new_folder\\bw_image2.png', img2_bw)

    # cv2.imshow("black and white image", img_bw)
    # cv2.waitKey(0)

    no_noise2 = noise_removal(img2_bw)
    cv2.imwrite('C:\\Users\\omp16\\Documents\\new_folder\\no_noise2.png', no_noise2)

    # cv2.imshow("no noise", no_noise)
    # cv2.waitKey(0)

    eroded_img2 = thin_font(no_noise2)
    cv2.imwrite('C:\\Users\\omp16\\Documents\\new_folder\\eroded_img.png', eroded_img)

    eroded_img2 = cv2.resize(eroded_img2,(0,0),fx=2,fy=2)
    eroded_img2 = cv2.GaussianBlur(eroded_img2,(11,11),0)
    eroded_img2 = cv2.medianBlur(eroded_img2,9)

    # cv2.imshow("eroded img", eroded_img)
    # cv2.waitKey(0)

    img2 = Image.fromarray(eroded_img2)
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
    
    time.sleep(1)
    result = ocr1 + ocr2
    
    new_result = str(result)
    
    keyboard.type(new_result)

