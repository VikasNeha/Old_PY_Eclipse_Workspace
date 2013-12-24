'''
Created on May 22, 2013

@author: Vikas
'''
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def openURL(driver, URL):
    driver.get(URL)
    
def selctOptionFromDropDown(driver, parentElementID, VisibleText):
    dropDown = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, parentElementID)))
    dropDown = Select(dropDown)
    dropDown.select_by_visible_text(VisibleText)
    
def enterText(driver, elementID, textToEnter):
    textBox = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, elementID)))
    textBox.clear()
    textBox.send_keys(textToEnter)

def clearText(driver, elementID):
    textBox = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, elementID)))
    textBox.clear()

def checkUncheckCheckbox(driver, elementID, desiredState):
    checkBoxElement = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, elementID)))
    if desiredState == True:
        if checkBoxElement.is_selected():
            pass
        else:
            checkBoxElement.click()
    elif desiredState == False:
        if checkBoxElement.is_selected():
            checkBoxElement.click()
        else:
            pass
    
def clickButton(driver, elementID):
    buttonElement = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, elementID)))
    buttonElement.click()