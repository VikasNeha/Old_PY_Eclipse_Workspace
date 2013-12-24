'''
Created on 15-Jul-2013
@author: Neha-Vikas
'''

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def openURL(driver, URL):
    driver.get(URL)
    
def enterText(driver, by, elementID, text):
    textBox = WebDriverWait(driver, 5).until(EC.presence_of_element_located((by, elementID)))
    textBox.clear()
    textBox.send_keys(text)
    
def clickButton(driver, by, elementID):
    button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((by, elementID)))
    button.click()
    
def selctOptionFromDropDown(driver, by, parentElementID, VisibleText):
    dropDown = WebDriverWait(driver, 5).until(EC.presence_of_element_located((by, parentElementID)))
    dropDown = Select(dropDown)
    dropDown.select_by_visible_text(VisibleText)

def clickLink(driver, by, elementID):
    link = WebDriverWait(driver, 5).until(EC.presence_of_element_located((by, elementID)))
    link.click()
    
def checkUncheckCheckbox(driver, by, elementID, desiredState):
    checkBoxElement = WebDriverWait(driver, 5).until(EC.presence_of_element_located((by, elementID)))
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
def switchToFrame(driver, frameName):
    WebDriverWait(driver, 5).until(EC.frame_to_be_available_and_switch_to_it(frameName))