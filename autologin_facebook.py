# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium import webdriver as wb
import time as t
a=wb.Chrome("D:/chrome/chromedriver.exe")  #setting chromedriver path

a.get("https://www.facebook.com/login")
t.sleep(2)

usn=a.find_element_by_id("email")
usn.send_keys("Enter your facebook address")
t.sleep(2)

pas=a.find_element_by_name("pass")
pas.send_keys("Enter your password")
t.sleep(10)
but1=a.find_element_by_id("loginbutton")
but1.click()
