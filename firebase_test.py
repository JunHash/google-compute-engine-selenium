#!/usr/bin/env python

from pyvirtualdisplay import Display
from selenium import webdriver
import time

def web_load(url):
    print 'browsing with firefox, ', url
    try:
      browser = webdriver.Firefox()
      browser.get(url)
      print browser.title
      browser.quit()
    except Exception as e:
      print e

    print 'browsing with chrome, ', url
    try:
      browser = webdriver.Chrome()
      browser.get(url)
      print browser.title
      browser.quit()
    except Exception as e:
      print e
    
display = Display(visible=0, size=(800, 600))
display.start()
url = 'https://www.junhash.com/firebase/'

while(1):
   web_load(url)
   time.sleep( 60 )

