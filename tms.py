#!/usr/bin/python
from ast import Bytes
from asyncio import wait_for
from cgitb import text
from curses import keyname
from curses.textpad import Textbox
from email.mime import image
from gettext import find
from multiprocessing.connection import wait
from re import A, search
from turtle import distance, speed
from xml.dom.minidom import Element
import click
from flask import send_file
from selenium import webdriver
from getpass import getpass
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys as K
from selenium.webdriver.support import expected_condition as E
from selenium.webdriver import ActionChains as A
from selenium .webdriver import webdriverWait as W







driver_location = "/usr/bin/chromedriver"
binary_location = "/usr/bin/google-chrome-stable"

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
driver.find_element_by_xpath("/html/body/app-root/tms/main/div/div/app-member-client-order-entry/div/div/div[3]/form/div[2]/div[2]/input").send_keys("Dailyordebook")
time.sleep(2)
driver.get("https://tms48.nepsetms.com.np/tms/me/order-book-v3")
a = A(driver)
Textbox1=driver.find_element_by_id("nav-open-info").send_keys("sanjay")
Textbox2=driver.find_element_by_id("nav-open-info")
a.key_down(K.CONTROL).send_key("a").perform()
a.key_down(K.CONTROL).send_key("c").perform()
a.click_and_hold(Textbox1).perform()
a.key_down(K.CONTROL).send_keys("v")








                                        