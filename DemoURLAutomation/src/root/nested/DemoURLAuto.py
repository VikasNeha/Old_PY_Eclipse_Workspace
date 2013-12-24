'''
Created on 15-Jul-2013
@author: Neha-Vikas
'''

from root.nested.Utilities import getUserdataFromDatabase
from root.nested import WebpageEvents, appEvents, gmailEvents, Utilities
from selenium import webdriver

userData = getUserdataFromDatabase()

driver = webdriver.Firefox()
driver.implicitly_wait(30)
appURL = "https://cvmas15.cvmsolutions.com/disney/new_vendor_registration.asp"

WebpageEvents.openURL(driver, appURL)
appEvents.fillUserForm(driver, userData)
appEvents.moveNextFromSearchPage(driver)

activationURL = gmailEvents.getActivationURLFromEmail(driver, userData, "Activation Email", "cvmsolutions")
print activationURL

driver.get(activationURL)

Utilities.updateUserdataActivationStatus(userData, "Activated")
