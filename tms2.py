#!/usr/bin/python
from argparse import Action
from ast import Bytes
from asyncio import wait_for
from cgitb import text
from curses import keyname
from curses.textpad import Textbox
from email.mime import image
from gettext import find
from hashlib import new
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

from selenium.webdriver import ActionChains as A








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
driver.find_element_by_name("filtername").send_keys("Daily order Book")
time.sleep(3)
driver.find_element_by_xpath("/html/body/app-root/tms/app-menubar/aside/nav/div/form/button/i").click()
time.sleep(5)
driver.find_element_by_xpath("/html/body/app-root/tms/main/div/div/app-order-book-v3/div/div[2]/div/order-book-prime/div/div[2]/div/div/kendo-grid/kendo-grid-toolbar/div/div[1]/div/div[1]/input").send_keys("sanjay")
#a.move_to_element(Element1).click().send_key("sanjay")
#a.key_down(K.CONTROL).send_key("a")
#a.send_keys("c")
#a.move_to_element(Element2).click()
#a.key_down(K.CONTROL).send_key("v")
#a.key_up(K.CONTROL).build.perform()







                                        