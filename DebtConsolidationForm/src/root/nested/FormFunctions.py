'''
Created on May 23, 2013

@author: Vikas
'''

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def selectLoanAmount(driver, debt_amount_to_select):
    debt_amount = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "rbm-drop-rbm_consumerdebt_debt_amount")))
    debt_amount.click()
    debt_amount_options = driver.find_element_by_id("rbm-drop-list-rbm_consumerdebt_debt_amount")
    debt_amount_options = debt_amount_options.find_elements_by_tag_name("li")
    for currentOption in debt_amount_options:
        if (debt_amount_to_select in currentOption.text):
            currentOption.click()
            break
        
def enterFirstName(driver, nameToEnter):
    first_name = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "first-name")))
    first_name.clear()
    first_name.send_keys(nameToEnter)

def enterLastName(driver, nameToEnter):
    last_name = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "last-name")))
    last_name.clear()
    last_name.send_keys(nameToEnter)
    
def enterEmail(driver, emailToEnter):
    email = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "email")))
    email.clear()
    email.send_keys(emailToEnter)

def enterPhone(driver, phoneToEnter):
    phone = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "phone")))
    phone.clear()
    phone.send_keys(phoneToEnter)
    
def selectState(driver, state_to_select):
    state = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "state-selection")))
    state.click()
    state_options = driver.find_element_by_id("state-dropdown")
    state_options = state_options.find_elements_by_tag_name("li")
    for currentOption in state_options:
        if (state_to_select in currentOption.text):
            currentOption.click()
            break

def submitForm(driver):
    submitButton = driver.find_element_by_id("debt-form-submit")
    submitButton.click()