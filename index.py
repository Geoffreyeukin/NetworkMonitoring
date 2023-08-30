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
        #get the title of the publication
    def _get_title(self,driver,classe=""):
        try:
         return driver.find_element(By.CSS_SELECTOR,classe).text
        except: return 0
            #titre=driver.find_element(By.CSS_SELECTOR,"._52jd")
    
    def _get_description(self,driver,csscelector="") -> list:
#description=driver.find_elements(By.CSS_SELECTOR,"._5rgt>div>p")
     try:
        description=driver.find_elements(By.CSS_SELECTOR,csscelector)
        return [i.text for i in description]
     except:return 0 
    def _get_date(self,driver,classe="") -> dict:
        # driver.find_element(By.CSS_SELECTOR,"._52jc>a").text
        try:
            date=driver.find_element(By.CSS_SELECTOR,classe).text
            return date
        except:return 0 
    def _getsharingnumber(self,driver,cssselector):
        try: 
            sharing=driver.find_element(By.CSS_SELECTOR,"._43lx>a>span")
            return driver.find_element(By.CSS_SELECTOR,cssselector).text.split(" ")[0]
        except: return 0   
    def getLikenumber(self,driver,cssselector=""):
        try: 
            #like=driver.find_element(By.CSS_SELECTOR,"._1g06")
            return driver.find_element(By.CSS_SELECTOR,cssselector).text
        except:return 0  
    def _getcomment(self,driver,xpathselector=""):
        try: 
        # commentbody=driver.find_elements(By.XPATH,"//div[@data-sigil='comment-body']")
            commentbody=driver.find_elements(By.XPATH,xpathselector)
        
            comment=[i.text for i in commentbody]
            if len(comment)>10:
                return comment[:10] 
        except:return 0            
    def searchaccident(self,usernames,passwords):
    
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
        time.sleep(15)
        i=0
            
        responses=driver.find_elements(By.XPATH,"//a[@class='_5msj _26yo']")
        print(len(responses))
        publications={}
        i=0
        while i <len(responses):
                print(i)
                j=0
                while j<10:
                    response=driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(5)
                    j+=1 
                time.sleep(10)    
                responses=driver.find_elements(By.XPATH,"//a[@class='_5msj _26yo']")
                print(len(responses))
                time.sleep(10)
                responses[i].click()
                time.sleep(10)
                title=driver.find_element(By.CSS_SELECTOR,"._52jd").text
                print(title)
                publication={"like_numbers":self.getLikenumber(driver,"._1g06"), "comment":self._getcomment(driver,"//div[@data-sigil='comment-body']"), "share_number":self._getsharingnumber(driver,"._43lx>a>span"),"date":self._get_date(driver,"._52jc>a"), "description":self._get_description(driver,"._5rgt>div>p"),"title":self._get_title(driver,"._52jd")}
                publications.update(publication)
                print(publication)
                driver.execute_script("window.history.go(-1)")
                i+=1
                time.sleep(10)
        print(publications)        
                       
facebook=getFacebookInfo()
username="" #Enter your facebook username here
password="" #Enter your facebook password here
facebook.searchaccident(username,password)                      