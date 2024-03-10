from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
import pyautogui
import os

filenames = {}
dirnames= ["Digital_Communication"]# USERDEFINED
for x in dirnames:
    filenames[x] = set(os.listdir(r'C:\Users\Sathvik Malgikar\OCR_BOT_IN'+f"\{x}"))
    os.makedirs(r'C:\Users\Sathvik Malgikar\OCR_BOT_OUT'+f"\{x}")
cs = webdriver.ChromeService("./chromedriver.exe")

driver = webdriver.Chrome(service=cs)
web_driver_wait = WebDriverWait(driver=driver,timeout=8)
from time import sleep

import shutil
import os
import time
def wait_for_file(path, timeout=None, poll_interval=2):
    start_time = time.time()
    while True:
        if os.path.exists(path):
            return True
        if timeout is not None and time.time() - start_time >= timeout:
            return False
        time.sleep(poll_interval)


def move_file(source_file, destination_folder):
    if not os.path.exists(source_file):
        return  

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    filename = os.path.basename(source_file)
    
    destination_path = os.path.join(destination_folder, filename)
    
    shutil.move(source_file, destination_path)

goback=False
absoluteFirst=True
while dirnames:
 
        
    if len(filenames[x])==0:
        
        del filenames[x]
        dirnames.remove(x)
        
        goback=True
        
        continue
        
    temp = filenames[x].pop()
    driver.get("https://www.ilovepdf.com/ocr-pdf")
    sleep(4)
    ele = driver.find_element(By.LINK_TEXT,"Select PDF file")
    web_driver_wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Select PDF file")))
    ele.click()
    sleep(3)
    
  
    if absoluteFirst:   
        pyautogui.typewrite("OCR_BOT_IN")
        pyautogui.press("enter")
        sleep(2)
        pyautogui.typewrite(x)
        pyautogui.press("enter")
        sleep(2)
    absoluteFirst=False
    if goback:
        pyautogui.hotkey('alt', 'up')
        sleep(2)
        pyautogui.hotkey('alt', 'up')
        sleep(2)
        pyautogui.typewrite(x)
        pyautogui.press("enter")
        sleep(2)
    goback=False
    pyautogui.typewrite(temp)
    pyautogui.press("enter")
    
    ele= web_driver_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button#processTask")))
    ele.click()
    
    sleep(16) # processing time
    

    ele = web_driver_wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Download PDF")))
    ele.click()
    
    sleep(26)# download time
    wait_for_file(r"C:\Users\Sathvik Malgikar\Downloads"+f"\{temp}")
    move_file(r"C:\Users\Sathvik Malgikar\Downloads"+f"\{temp}",r"C:\Users\Sathvik Malgikar\OCR_BOT_OUT"f"\{x}")

    

    current = driver.current_window_handle
    driver.execute_script("window.open('https://www.ilovepdf.com/ocr-pdf')")
    new_tab = [tab for tab in driver.window_handles if tab != current][0]
    
    driver.switch_to.window(current)
    driver.close()
    
    driver.switch_to.window(new_tab)
    sleep(2)
    
    

sleep(100)    

driver.close()