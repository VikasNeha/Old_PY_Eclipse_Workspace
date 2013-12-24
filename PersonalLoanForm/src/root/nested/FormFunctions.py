'''
Created on May 23, 2013

@author: Vikas
'''

from root.nested import Utilities
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
#from selenium.webdriver.common.by import By

sleepTime = 1

def selectState(driver, home_state):
    Utilities.selctOptionFromDropDown(driver, "home_state", home_state)
    time.sleep(sleepTime)
    
def selectLoanAmount(driver, loan_amount):
    Utilities.selctOptionFromDropDown(driver, "loan_amount", loan_amount)
    time.sleep(sleepTime)    
    
def enterPersonalDetails(driver, name_first, name_last, email_primary, phone_home, home_zip, terms):
    Utilities.enterText(driver, "name_first", name_first)
    Utilities.enterText(driver, "name_last", name_last)
    Utilities.enterText(driver, "email_primary", email_primary)
    Utilities.enterText(driver, "phone_home_1", phone_home[0:3])
    Utilities.enterText(driver, "phone_home_2", phone_home[3:6])
    Utilities.enterText(driver, "phone_home_3", phone_home[6:])
    Utilities.enterText(driver, "home_zip", home_zip)
    Utilities.checkUncheckCheckbox(driver, "terms", terms)
    Utilities.clickButton(driver, "button_next_2")
    time.sleep(sleepTime)    

def selectIncomeSource(driver, income_source):
    Utilities.selctOptionFromDropDown(driver, "income_source", income_source)
    time.sleep(sleepTime)
    
def enterHomeStreetCity(driver, home_street, home_city):
    Utilities.enterText(driver, "home_street", home_street)
    Utilities.enterText(driver, "home_city", home_city)
    Utilities.clickButton(driver, "button_next_4")
    time.sleep(sleepTime)
        
def selectMilitary(driver, military):
    Utilities.selctOptionFromDropDown(driver, "military", military)
    time.sleep(sleepTime)
    
def enterIncomeMonthlyNet(driver, income_monthly_net):
    Utilities.enterText(driver, "income_monthly_net", income_monthly_net)
    Utilities.clickButton(driver, "button_next_6")
    time.sleep(sleepTime)    
    
def selectBankAccountType(driver, bank_account_type):
    Utilities.selctOptionFromDropDown(driver, "bank_account_type", bank_account_type)
    time.sleep(sleepTime)
    
def selectDirectDeposit(driver, direct_deposit):
    Utilities.selctOptionFromDropDown(driver, "direct_deposit", direct_deposit)
    time.sleep(sleepTime)    
    
def selectIncomeFrequency(driver, income_frequency):
    Utilities.selctOptionFromDropDown(driver, "income_frequency", income_frequency)
    time.sleep(sleepTime)    
    
def selectNextPayDates(driver):
    calendarElement = driver.find_element_by_class_name("ui-datepicker-calendar")
    nextClickableDateElement = calendarElement.find_element_by_tag_name("a")
    nextClickableDateElement.click()    
    
    Utilities.clickButton(driver, "button_next_10")
    time.sleep(sleepTime)        

def enterEmployerDetails(driver, employer_name, phone_work, employment_length):
    Utilities.enterText(driver, "employer_name", employer_name)
    Utilities.enterText(driver, "phone_work_1", phone_work[0:3])
    Utilities.enterText(driver, "phone_work_2", phone_work[3:6])
    Utilities.enterText(driver, "phone_work_3", phone_work[6:])
    Utilities.selctOptionFromDropDown(driver, "employment_length", employment_length)
    Utilities.clickButton(driver, "button_next_11")
    time.sleep(sleepTime)    
    
def enterBankDetails(driver, bank_name, bank_aba, bank_account):
    Utilities.enterText(driver, "bank_name", bank_name)
    Utilities.enterText(driver, "bank_aba", bank_aba)
    Utilities.enterText(driver, "bank_account", bank_account)
    Utilities.clickButton(driver, "button_next_12")
    time.sleep(sleepTime)    
    
def selectLicenseDetails(driver, state_issued_id, state_id_number):
    Utilities.selctOptionFromDropDown(driver, "state_issued_id", state_issued_id)
    Utilities.enterText(driver, "state_id_number", state_id_number)
    Utilities.clickButton(driver, "button_next_13")
    time.sleep(sleepTime)    
    
def enterDOB_SSN(driver, dob_m, dob_d, dob_y, ssn_area, ssn_group, ssn_serial):
    Utilities.selctOptionFromDropDown(driver, "dob_m", dob_m)
    Utilities.selctOptionFromDropDown(driver, "dob_d", dob_d)
    Utilities.selctOptionFromDropDown(driver, "dob_y", dob_y)
    Utilities.enterText(driver, "ssn_area", ssn_area)
    Utilities.enterText(driver, "ssn_group", ssn_group)
    Utilities.enterText(driver, "ssn_serial", ssn_serial)
    Utilities.clickButton(driver, "button_next_14")
    time.sleep(sleepTime)    

def submitForm(driver):
    Utilities.clickButton(driver, "button_next_15")
    time.sleep(sleepTime+sleepTime)

def clickApplyHere(driver):
    linkApplyHere = driver.find_element_by_link_text("Apply Here")
    linkApplyHere.click()
    time.sleep(sleepTime)        
        
def assertTextInFormArea(driver, textToAssert, currentFormElement):
    elem = returnFormArea(driver)
    assert textToAssert in elem.text
    
def returnFormArea(driver):
    elem = driver.find_element_by_id("form-area")
    return elem

def assertFinalResultRejected(driver):
    try:
        WebDriverWait(driver, 20).until(EC.title_contains("Loans, Personal Loans, Bad Credit Loans | CreditLoan.com"))
    except TimeoutException:
        raise TimeoutException

def assertFinalResultRejectedBankAcount(driver):
    try:
        WebDriverWait(driver, 20).until(EC.title_contains("Apply For Debt Consolidation Services"))
    except TimeoutException:
        raise TimeoutException

def assertFinalResultRedirectedToPioneer(driver):
    try:
        WebDriverWait(driver, 20).until(EC.title_contains("Pioneer Military Lending"))
    except TimeoutException:
        raise TimeoutException

def clickBackButton(driver):
    backButtons = driver.find_elements_by_name("button_back")
    for currentButton in backButtons:
        if currentButton.is_displayed():
            currentButton.click()
            break
    time.sleep(sleepTime)