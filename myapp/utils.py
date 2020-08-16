from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pickle
import time


def autolike():
    driver = webdriver.Firefox(executable_path=r'C:\Users\admin\PycharmProjects\day1__py\geckodriver.exe')
    cookies = pickle.load(open(r'C:\Users\admin\PycharmProjects\djgo1\myapp\cookie.pkl', 'rb'))
    driver.get("http://www.facebook.com")
    print(cookies)
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get("http://www.facebook.com")


