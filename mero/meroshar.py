#!/usr/bin/python
from ast import Bytes
from cgitb import text
from curses import KEY_DOWN, keyname
from curses.textpad import Textbox
from email.mime import image
from gettext import find
from re import search
import click
from selenium import webdriver
from getpass import getpass
import time


driver_location = "/usr/bin/chromedriver"


driver = webdriver.Chrome()
driver.get("https://meroshare.cdsc.com.np/#/login")

driver.find_element_by_xpath("/html/body/app-login/div/div/div/div/div/div/div[1]/div/form/div/div[1]/div/div/select2/span/span[1]/span/span[1]").click()
driver.find_element_by_xpath("/html/body/span/span/span[2]/ul/li[41]").click()
#for login tms and credential
username_textbox =driver.find_element_by_xpath("/html/body/app-login/div/div/div/div/div/div/div[1]/div/form/div/div[2]/div/div/input")
username_textbox.send_keys("00950352")

password_textbox = driver.find_element_by_xpath("/html/body/app-login/div/div/div/div/div/div/div[1]/div/form/div/div[3]/div/div/input")
password_textbox.send_keys("rawalsanjay123")


driver.find_element_by_xpath("/html/body/app-login/div/div/div/div/div/div/div[1]/div/form/div/div[4]/div/button").click()
time.sleep(4)
driver.find_element_by_xpath("/html/body/app-dashboard/div/div[1]/nav/ul/li[8]/a").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/app-dashboard/div/main/div/app-asba/div/div[2]/app-applicable-issue/div/div/div/div/div/div/div[2]/div/div[4]/button").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/app-dashboard/div/main/div/app-issue/div/wizard/div/wizard-step[1]/form/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div/select").click()
#time.sleep(3)
#driver.find_element_by_xpath("/html/body/app-dashboard/div/main/div/app-issue/div/wizard/div/wizard-step[1]/form/div[2]/div/div[4]/div/div[2]/div/div/div[2]/div/select/option").click()

time.sleep(3)
driver.find_element_by_xpath("/html/body/app-dashboard/div/main/div/app-issue/div/wizard/div/wizard-step[1]/form/div[2]/div/div[4]/div/div[5]/div/div/div[2]/div/input").send_keys(10)
time.sleep(3)
driver.find_element_by_xpath("/html/body/app-dashboard/div/main/div/app-issue/div/wizard/div/wizard-step[1]/form/div[2]/div/div[4]/div/div[7]/div/div/div[2]/div/input").send_keys("01210017525225")
time.sleep(2)
driver.find_element_by_xpath("/html/body/app-dashboard/div/main/div/app-issue/div/wizard/div/wizard-step[1]/form/div[2]/div/div[5]/div[1]/div/input").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/app-dashboard/div/main/div/app-issue/div/wizard/div/wizard-step[1]/form/div[2]/div/div[5]/div[2]/div/button[1]").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/app-dashboard/div/main/div/app-issue/div/wizard/div/wizard-step[2]/div[2]/div/form/div[1]/div/div[3]/div/input").send_keys("0023")

time.sleep(5)
driver.find_element_by_xpath("/html/body/app-dashboard/div/main/div/app-issue/div/wizard/div/wizard-step[2]/div[2]/div/form/div[2]/div/div/div/button[2]").click()