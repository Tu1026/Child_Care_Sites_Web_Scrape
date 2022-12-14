# Generated by Selenium IDE
# import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
centers = []
locations =[]
emails =[]
programs =  []
phones = []
# Test name: Untitled
# Step # | name | target | value
# 1 | open | https://maps.gov.bc.ca/ess/hm/ccf/ | 
driver.get("https://childcaresearch.gov.mb.ca/?fbclid=IwAR0DlU0LdxYNRrV-Qz4penGpkcDQQcNdxPLbtikqrL09j5qdj5udZzrrBl8")
# 2 | click | css=fieldset:nth-child(1) .col-12:nth-child(3) .custom-control-label | 
driver.find_element(By.CSS_SELECTOR, "fieldset:nth-child(1) .col-12:nth-child(3) .custom-control-label").click()
# 3 | click | css=fieldset:nth-child(3) .col-12:nth-child(1) .custom-control-label | 
driver.find_element(By.CSS_SELECTOR, "fieldset:nth-child(3) .col-12:nth-child(1) .custom-control-label").click()
# 4 | click | css=fieldset:nth-child(3) .col-12:nth-child(2) .custom-control-label | 
driver.find_element(By.CSS_SELECTOR, "fieldset:nth-child(3) .col-12:nth-child(2) .custom-control-label").click()
WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".page-length")))
WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".record-count")))
curr = (driver.find_element(By.CSS_SELECTOR, ".page-length").text)
max_page =  (driver.find_element(By.CSS_SELECTOR, ".record-count").text)

while not curr or not max_page:
  curr = driver.find_element(By.CSS_SELECTOR, ".page-length").text
  max_page =  driver.find_element(By.CSS_SELECTOR, ".record-count").text
    
print('curr ',curr)
print('max ', max_page)
while int(driver.find_element(By.CSS_SELECTOR, ".page-length").text) < int(driver.find_element(By.CSS_SELECTOR, ".record-count").text) - 24:
  while not curr:
    curr = driver.find_element(By.CSS_SELECTOR, ".page-length").text
    max_page =  driver.find_element(By.CSS_SELECTOR, ".record-count").text
  # time.sleep(20)
  curr = int(curr) + 24
  print('curr ',driver.find_element(By.CSS_SELECTOR, ".page-length").text)
  print('max ', driver.find_element(By.CSS_SELECTOR, ".record-count").text)
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

i = 1
driver.implicitly_wait(0)
while len(driver.find_elements(By.CSS_SELECTOR, f".col-lg-6:nth-child({i}) .child-care-facility-name")) > 0:
  print(driver.find_element(By.CSS_SELECTOR, f".col-lg-6:nth-child({i}) .child-care-facility-name").text)
  centers.append(driver.find_element(By.CSS_SELECTOR, f".col-lg-6:nth-child({i}) .child-care-facility-name").text)

  if len(driver.find_elements(By.CSS_SELECTOR, f".col-lg-6:nth-child({i}) .child-care-facility-email")) > 0:
    print('size of emails ',len(driver.find_elements(By.CSS_SELECTOR, f".col-lg-6:nth-child({i}) .child-care-facility-email")))
    emails.append(driver.find_element(By.CSS_SELECTOR, f".col-lg-6:nth-child({i}) .child-care-facility-email").text)
  else:
    emails.append("")
  if len(driver.find_elements(By.CSS_SELECTOR, f".col-lg-6:nth-child({i}) .child-care-facility-phone-number")) > 0:
    phones.append(driver.find_element(By.CSS_SELECTOR, f".col-lg-6:nth-child({i}) .child-care-facility-phone-number").text)
  else:
    phones.append('')
  # emails.append(driver.find_element(By.CSS_SELECTOR, f".col-lg-6:nth-child({i}) .child-care-facility-email").text)
  
  programs.append(driver.find_element(By.CSS_SELECTOR, f".col-lg-6:nth-child({i}) .child-care-facility-description").text)
  locations.append(driver.find_element(By.CSS_SELECTOR, f".col-lg-6:nth-child({i}) .child-care-facility-address").text)
  # phones.append( (driver.find_element(By.CSS_SELECTOR, f".col-lg-6:nth-child({i}) .child-care-facility-phone-number").text))
    
  i +=1 
  



pd.DataFrame({"Centers":centers, "Locations":locations, "emails":emails, 
              "programs":programs}).to_csv('manitoba.csv')


# # Test name: manitoba
# # Step # | name | target | value
# # 1 | open | /?fbclid=IwAR0DlU0LdxYNRrV-Qz4penGpkcDQQcNdxPLbtikqrL09j5qdj5udZzrrBl8 | 
# self.driver.get("https://childcaresearch.gov.mb.ca/?fbclid=IwAR0DlU0LdxYNRrV-Qz4penGpkcDQQcNdxPLbtikqrL09j5qdj5udZzrrBl8")
# # 2 | click | css=fieldset:nth-child(1) .col-12:nth-child(3) .custom-control-label | 
# self.driver.find_element(By.CSS_SELECTOR, "fieldset:nth-child(1) .col-12:nth-child(3) .custom-control-label").click()
# # 3 | click | css=fieldset:nth-child(3) .col-12:nth-child(1) .custom-control-label | 
# self.driver.find_element(By.CSS_SELECTOR, "fieldset:nth-child(3) .col-12:nth-child(1) .custom-control-label").click()
# # 4 | click | css=fieldset:nth-child(3) .col-12:nth-child(2) .custom-control-label | 
# self.driver.find_element(By.CSS_SELECTOR, "fieldset:nth-child(3) .col-12:nth-child(2) .custom-control-label").click()
# # 6 | storeText | css=.page-length | curr
# self.vars["curr"] = self.driver.find_element(By.CSS_SELECTOR, ".page-length").text
# # 7 | storeText | css=.record-count | total
# self.vars["total"] = self.driver.find_element(By.CSS_SELECTOR, ".record-count").text
# # 8 | storeText | css=.col-lg-6:nth-child(26) .child-care-facility-name | factName
# self.vars["factName"] = self.driver.find_element(By.CSS_SELECTOR, ".col-lg-6:nth-child(26) .child-care-facility-name").text
# # 9 | verifyElementPresent | css=.col-lg-6:nth-child(26) .child-care-facility-name | 
# elements = self.driver.find_elements(By.CSS_SELECTOR, ".col-lg-6:nth-child(26) .child-care-facility-name")
# assert len(elements) > 0
# # 10 | storeText | css=.col-lg-6:nth-child(25) .child-care-facility-description | factDesc
# self.vars["factDesc"] = self.driver.find_element(By.CSS_SELECTOR, ".col-lg-6:nth-child(25) .child-care-facility-description").text
# # 11 | storeText | css=.col-lg-6:nth-child(25) .col-6 > div | email
# self.vars["email"] = self.driver.find_element(By.CSS_SELECTOR, ".col-lg-6:nth-child(25) .col-6 > div").text
# # 12 | storeText | css=.col-lg-6:nth-child(25) .child-care-facility-address | address
# self.vars["address"] = self.driver.find_element(By.CSS_SELECTOR, ".col-lg-6:nth-child(25) .child-care-facility-address").text

