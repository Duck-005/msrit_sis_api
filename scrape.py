from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
from model import Data

service = Service(executable_path='./chromedriver.exe')
options = Options()
options.add_argument("--headless=new")
options.add_argument("--disable-gpu") 
options.add_argument("--no-sandbox")  
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--enable-automation")  
options.add_argument("--window-size=1920,1080")  
options.add_argument("--disable-extensions") 
options.add_argument("--disable-notifications")  
options.add_argument("--disable-plugins")  
options.add_argument("--disable-infobars") 

class SIS:
    def __init__(self):
        self.driver = webdriver.Chrome(service=service, options=options)
    
    def scrape(self, usn, password):
        driver = self.driver
        driver.get('https://parents.msrit.edu/newparents/')
        self.login(usn, password)
        pfImage = driver.find_element(By.XPATH, '//*[@id="page_bg"]/div[1]/div/div/div[2]/div/div/div[1]/div/img').get_attribute("src")
        name = driver.find_element(By.XPATH, '//*[@id="page_bg"]/div[1]/div/div/div[2]/div/div/div[1]/div').text
        lastUpdated = driver.find_element(By.XPATH, '//*[@id="page_bg"]/div[1]/div/div/div[3]/div[2]/div/p').text[17:]
        
        detail = driver.find_element(By.XPATH, '//*[@id="page_bg"]/div[1]/div/div/div[2]/div/div/div[2]/div/div[2]/p').text
        sem = detail[8:14]
        section = detail[16:]

        courseData = []
        for sub in range(1,10):
            subAttendanceXpath = f'//*[@id="page_bg"]/div[1]/div/div/div[5]/div/div/div/table/tbody/tr[{sub}]/td[5]/a/button'
            subCodeXpath = f'//*[@id="page_bg"]/div[1]/div/div/div[5]/div/div/div/table/tbody/tr[{sub}]/td[1]'
            subNameXpath = f'//*[@id="page_bg"]/div[1]/div/div/div[5]/div/div/div/table/tbody/tr[{sub}]/td[2]'

            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, subAttendanceXpath)))
            
            subAttendance = driver.find_element(By.XPATH, subAttendanceXpath).text
            subCode = driver.find_element(By.XPATH, subCodeXpath).text
            subName = driver.find_element(By.XPATH, subNameXpath).text
            
            courseData.append({
                "code": subCode,
                "name": subName,
                "attendance": subAttendance
            })
            
        # rows = driver.find_elements(By.XPATH, "//tr[starts-with(@class, 'bb-tooltip-name-')]")
        # for row in rows:
        #     WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//tr[starts-with(@class, 'bb-tooltip-name-')]")))
        #     subMarks = row.find_element(By.CLASS_NAME, "value").text.strip()
        #     print(subMarks)
        #     #  courseData[subCode].add(subMarks)
        
        driver.quit()

        return Data(
                name=name,
                usn=usn,
                section=section,
                photo=pfImage,
                sem=sem,
                courseData=courseData,
                lastUpdated=lastUpdated
            )
        
    def login(self, usn, password):
        driver = self.driver
        driver.find_element(By.ID, "username").send_keys(usn)  # 07-08-2005
        Select(driver.find_element(By.ID, 'dd')).select_by_index(int(password[0:2].lstrip('0')))
        Select(driver.find_element(By.ID, 'mm')).select_by_index(int(password[3:5].lstrip('0')))
        Select(driver.find_element(By.ID, 'yyyy')).select_by_visible_text(password[6:])

        driver.find_element(By.XPATH, '//*[@id="login-form"]/div[3]/input[1]').click()  # login button
        ActionChains(driver).move_by_offset(10, 10).click().perform()
                