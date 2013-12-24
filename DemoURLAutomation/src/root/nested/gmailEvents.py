'''
Created on 15-Jul-2013
@author: Neha-Vikas
'''
from root.nested import WebpageEvents
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import StaleElementReferenceException

def checkIfLoggedIn(driver):
    if driver.title == "Gmail: Email from Google" :
        return False
    else:
        return True

def loginToGmail(driver, userData):
    if checkIfLoggedIn(driver) == True:
        logoutFromGmail(driver)
    WebpageEvents.enterText(driver, By.ID, "Email", userData.Gmail_Username.strip())
    WebpageEvents.enterText(driver, By.ID, "Passwd", userData.Gmail_Password.strip())
    WebpageEvents.checkUncheckCheckbox(driver, By.ID, "PersistentCookie", False)
    WebpageEvents.clickButton(driver, By.ID, "signIn")
        
def logoutFromGmail(driver):
    #WebpageEvents.switchToFrame(driver, "canvas_frame")
    WebpageEvents.clickLink(driver, By.PARTIAL_LINK_TEXT, "@gmail.com")
    WebpageEvents.clickLink(driver, By.PARTIAL_LINK_TEXT, "Sign out")

def openEmailWithSubject(driver, subject):
    WebpageEvents.switchToFrame(driver, "canvas_frame")
    allTDs = driver.find_elements_by_tag_name("td")
    for currentTD in allTDs:
        if subject in currentTD.text:
            currentTD.click()
            break

def openEmailWithFrom(driver, fromEmail):
    WebpageEvents.switchToFrame(driver, "canvas_frame")
    allTDs = driver.find_elements(By.TAG_NAME, "td")
    for currentTD in allTDs:
        if fromEmail in currentTD.text:
            currentTD.click()
            break
        
def getActivationURLFromEmail(driver, userData, emailSubject, linkText):
    driver.get("https://www.gmail.com")
    loginToGmail(driver, userData)
    openEmailWithSubject(driver, emailSubject)
    time.sleep(5)
    linkElements = driver.find_elements(By.TAG_NAME, "a")
    for currEle in linkElements:
        try:
            if (linkText in currEle.get_attribute("href")):
                linkURL = currEle.get_attribute("href")
                break
        except StaleElementReferenceException:
            continue
    
    logoutFromGmail(driver)
    return linkURL