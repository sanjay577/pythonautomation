#!/usr/bin/python
from ast import Bytes
from cgitb import text
from curses import keyname
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
driver.get("https://tms48.nepsetms.com.np/tms/client/dashboard")

#for login tms and credential
username_textbox =driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/div[2]/form/div[1]/input")
username_textbox.send_keys("2021023133")

password_textbox = driver.find_element_by_id('password-field')
password_textbox.send_keys("MFy5Y2#7S9M!v7")

#search credincal/////
time.sleep(20)
login_button = driver.find_element_by_xpath('/html/body/app-root/app-login/div/div/div[2]/form/div[4]/input').click()
time.sleep(5)
driver.find_element_by_name("filtername").send_keys("Buy/Sell undefined")
time.sleep(3)
driver.find_element_by_xpath("/html/body/app-root/tms/app-menubar/aside/nav/div/form/button/i").click()

#buing element ////
time.sleep(2)
driver.find_element_by_xpath("/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[2]/div[2]/input").send_keys("ADBL")

#dynamic data coping and paste
time.sleep(6)
driver.find_element_by_xpath("/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[2]/div[3]/input").send_keys("10")
time.sleep(3)
driver.find_element_by_xpath("/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[2]/div[4]/input").send_keys("412.7")


time.sleep(3)
driver.find_element_by_xpath("/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[1]/div[2]/app-three-state-toggle/div/div/label[3]").click()

time.sleep(5)
driver.find_element_by_xpath("/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[3]/div[2]/button[1]").click()







                                        