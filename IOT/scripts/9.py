from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import sys
l = sys.argv
l = l[1:]
song = ' '.join(l)
song = song.replace('play','')

binary = '/root/images_to_spoof/firefox/firefox'
browser = webdriver.Firefox(firefox_binary=binary)
browser.get('https://www.youtube.com/results?search_query='+song)
song_title = browser.find_element_by_id('video-title')
song_title.click()
