# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium import webdriver as wb
import time as t
a=wb.Chrome("D:/chrome/chromedriver.exe")  #setting chromedriver path

a.get("https://accounts.google.com")
t.sleep(2)
usn=a.find_element_by_id("identifierId")
usn.send_keys("thakurgaurav497@gmail.com")
t.sleep(2)
but=a.find_element_by_id("identifierNext")
but.click()
t.sleep(2)
pas=a.find_element_by_name("password")
pas.send_keys("gaurav04")
but1=a.find_element_by_id("passwordNext")
but1.click()