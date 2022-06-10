import math
from operator import sub
from random import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common import by
from fake_useragent import UserAgent

def split_raw_code(code):
    codes = code.split("-")
    if len(codes) == 5:
        print("Length of codes arr:",len(codes))

        if(len(codes[0])==7 and len(codes[1])==5) and len(codes[2])==4 and len(codes[3])==4 and len(codes[4])==2:
            print("Passed")
            return codes
            
ua = UserAgent(verify_ssl=False)
user_agent = ua.random

print("USER AGENT: " + user_agent)
code = input("Input Chik-Fil-A Survey Code: ")
code_arr = split_raw_code(code)

profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", user_agent)
driver = webdriver.Firefox(profile)

driver.get("https://www.mycfavisit.com/")
boxes = []
boxes.append(driver.find_element("name", "CN1")) 
boxes.append(driver.find_element("name", "CN2"))
boxes.append(driver.find_element("name", "CN3"))
boxes.append(driver.find_element("name", "CN4"))
boxes.append(driver.find_element("name", "CN5"))

print(code_arr)
for index,section in enumerate(code_arr):
    boxes[index].send_keys(section)
    # for key in section:
    #     sleep((.33*random())+.23)
    #     boxes[index].send_keys(key)

btn = driver.find_element("name","NextButton")
btn.click()