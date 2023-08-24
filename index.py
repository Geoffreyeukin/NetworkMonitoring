import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class getFacebookInfo:
    def __init__(self) -> None:
        self.service = Service(executable_path='D:/chromedriver-win64/chromedriver.exe')
        self.chrome_options = webdriver.ChromeOptions()
        self.prefs = {"profile.default_content_setting_values.notifications" : 2}
        self.chrome_options.add_experimental_option("prefs",self.prefs)
        
    def searchaccident(self,usernames,passwords):
        self.driver = webdriver.Chrome(service=self.service,options=self.chrome_options)
        driver = webdriver.Chrome(service=self.service,options=self.chrome_options)
        driver.get("https://m.facebook.com/search/posts/?q=accident+circulation+cameroun+2023&source=filter&isTrending=0&tsid")
        connect = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[class='_7nyk _7nyj']"))).click()
        username = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
        password = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))
        username.clear()
        username.send_keys(usernames)
        password.clear()
        password.send_keys(passwords)
        button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='login']"))).click()
        time.sleep(30)
  
                       
facebook=getFacebookInfo()
username=""
password=""
facebook.searchaccident(username,password)                      