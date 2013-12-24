'''
Created on 15-Jul-2013
@author: Neha-Vikas
'''
from root.nested import WebpageEvents
from selenium.webdriver.common.by import By

def fillUserForm(driver, userData):
    WebpageEvents.enterText(driver, By.ID, "Name", userData.Company_Name.strip())
    WebpageEvents.selctOptionFromDropDown(driver, By.NAME, "HQState", userData.State.strip())
    WebpageEvents.enterText(driver, By.ID, "TaxID1", userData.Federal_Tax_ID.strip())
    WebpageEvents.enterText(driver, By.ID, "HeadQuartersAddr1", userData.Address1.strip())
    WebpageEvents.enterText(driver, By.ID, "HeadQuartersAddr2", userData.Address2.strip())
    WebpageEvents.enterText(driver, By.ID, "HeadQuartersAddr3", userData.Address3.strip())
    WebpageEvents.enterText(driver, By.ID, "HeadQuartersCity", userData.City.strip())
    WebpageEvents.enterText(driver, By.ID, "HeadQuartersZip", userData.Postal_Code.strip())
    WebpageEvents.enterText(driver, By.ID, "HQAreaCode", userData.Phone_Area.strip())
    WebpageEvents.enterText(driver, By.ID, "HQTelephoneNumber", userData.Phone_Number.strip())
    WebpageEvents.enterText(driver, By.ID, "HQFaxAreaCode", userData.Fax_Area.strip())
    WebpageEvents.enterText(driver, By.ID, "HQFaxNumber", userData.Fax_Number.strip())
    WebpageEvents.enterText(driver, By.ID, "PrimaryContactFName", userData.Contact_Name.strip())
    WebpageEvents.enterText(driver, By.ID, "PrimaryContactTitle", userData.Title.strip())
    WebpageEvents.enterText(driver, By.ID, "PrimaryContactEmail", userData.Contact_Email.strip())
    WebpageEvents.enterText(driver, By.ID, "PrimaryContactAreaCode", userData.Contact_Phone_Area.strip())
    WebpageEvents.enterText(driver, By.ID, "PrimaryContactTelephoneNumber", userData.Contact_Phone_Number.strip())
    WebpageEvents.enterText(driver, By.ID, "PrimaryContactFaxAreaCode", userData.Contact_Fax_Area.strip())
    WebpageEvents.enterText(driver, By.ID, "PrimaryContactFaxNumber", userData.Contact_Fax_Number.strip())
    WebpageEvents.checkUncheckCheckbox(driver, By.ID, "chkTermsOfUse", True)
    WebpageEvents.clickButton(driver, By.ID, "btnOK")

def moveNextFromSearchPage(driver):
    WebpageEvents.clickLink(driver, By.LINK_TEXT, "click here")