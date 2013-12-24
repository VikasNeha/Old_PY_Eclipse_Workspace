'''
Created on May 21, 2013

@author: Vikas
'''
import unittest
import time

from root.nested import Utilities, FormFunctions, TestDataStructure, PersonalLoanFormSuper
from root.nested.FormFunctions import sleepTime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def setupTestData(self):
    self.testData = TestDataStructure.setUpTestDataForTC3_TC1("Alabama", 
                                     "Up to $100", 
                                     "test", "test", "test@test.com", "3333333333", "33333", True)
    
def TCsSpecificSetup(self):
    testData = self.testData                
    driver = self.driver
    Utilities.openURL(driver, self.appURL)
    #self.assertIn(self, "Personal Loans", driver.title)
    
    #Click Apply Here
    FormFunctions.clickApplyHere(driver)                                
    FormFunctions.assertTextInFormArea(driver, "Select your residence state", "Apply Here")
    
    #Select State
    FormFunctions.selectState(driver, testData.home_state)
    FormFunctions.assertTextInFormArea(driver, "Up to what loan amount", "State")
    
    #Select Loan Amount
    FormFunctions.selectLoanAmount(driver, testData.loan_amount)
    FormFunctions.assertTextInFormArea(driver, "Your First Name", "Loan Amount")

def assertFinalValidationPopup(self, fieldName):
    driver = self.driver
    try:
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to_alert()
        self.assertTrue("Please fill out all fields" in alert.text)
        alert.accept()
    except TimeoutException:
        self.failMsg = self.failMsg + "Popup not displayed on losing focus from " + fieldName
        raise TimeoutException(self.failMsg)
    except AssertionError:
        self.failMsg = self.failMsg + "Wrong Popup displayed on losing focus from " + fieldName + "Popup text: " + alert.text
        raise AssertionError(self.failMsg)

class test_ValidatePersonalDetails(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        PersonalLoanFormSuper.setUp(self, "Personal Loan Form: TC3: Testing validation of Personal Details")
        setupTestData(self)
        TCsSpecificSetup(self)
    
    def setUp(self):
        pass
        
    def tearDown(self):
        PersonalLoanFormSuper.tearDown(self)
    
    @classmethod
    def tearDownClass(self):
        PersonalLoanFormSuper.tearDownClass(self)
    
    def test_TC1_ValidateFirstNameRequired(self):
        testData = self.testData
        driver = self.driver
        
        driver.find_element_by_id("name_last").click()        
        try:
            WebDriverWait(driver, 5).until(EC.alert_is_present())
            alert = driver.switch_to_alert()
            self.assertTrue("Please provide your correct first name" in alert.text)
            alert.accept()
        except TimeoutException:
            self.failMsg = self.failMsg + "Popup not displayed on losing focus from First Name"
            raise TimeoutException(self.failMsg)
        except AssertionError:
            self.failMsg = self.failMsg + "Wrong Popup displayed on losing focus from First Name. Popup text: " + alert.text
            raise AssertionError(self.failMsg)
        
        #Utilities.enterText(driver, "name_first", testData.name_first)
        Utilities.enterText(driver, "name_last", testData.name_last)
        Utilities.enterText(driver, "email_primary", testData.email_primary)
        Utilities.enterText(driver, "phone_home_1", testData.phone_home[0:3])
        Utilities.enterText(driver, "phone_home_2", testData.phone_home[3:6])
        Utilities.enterText(driver, "phone_home_3", testData.phone_home[6:])
        Utilities.enterText(driver, "home_zip", testData.home_zip)
        Utilities.checkUncheckCheckbox(driver, "terms", testData.terms)
        Utilities.clickButton(driver, "button_next_2")
        time.sleep(sleepTime)
        
        assertFinalValidationPopup(self, "First Name")
        
    def test_TC2_ValidateLastNameRequired(self):
        testData = self.testData
        driver = self.driver
        
        Utilities.enterText(driver, "name_first", testData.name_first)
        #Utilities.enterText(driver, "name_last", testData.name_last)
        Utilities.clearText(driver, "name_last")
        driver.find_element_by_id("email_primary").click()
        try:
            WebDriverWait(driver, 5).until(EC.alert_is_present())
            alert = driver.switch_to_alert()
            self.assertTrue("Please provide your correct last name" in alert.text)
            alert.accept()
        except TimeoutException:
            self.failMsg = self.failMsg + "Popup not displayed on losing focus from Last Name"
            raise TimeoutException(self.failMsg)
        except AssertionError:
            self.failMsg = self.failMsg + "Wrong Popup displayed on losing focus from Last Name. Popup text: " + alert.text
            raise AssertionError(self.failMsg)
        Utilities.enterText(driver, "email_primary", testData.email_primary)
        Utilities.enterText(driver, "phone_home_1", testData.phone_home[0:3])
        Utilities.enterText(driver, "phone_home_2", testData.phone_home[3:6])
        Utilities.enterText(driver, "phone_home_3", testData.phone_home[6:])
        Utilities.enterText(driver, "home_zip", testData.home_zip)
        Utilities.checkUncheckCheckbox(driver, "terms", testData.terms)
        Utilities.clickButton(driver, "button_next_2")
        time.sleep(sleepTime)
        
        assertFinalValidationPopup(self, "Last Name")

    def test_TC3_ValidateEmailRequired(self):
        testData = self.testData
        driver = self.driver
        
        Utilities.enterText(driver, "name_first", testData.name_first)
        Utilities.enterText(driver, "name_last", testData.name_last)
        #Utilities.enterText(driver, "email_primary", testData.email_primary)
        Utilities.clearText(driver, "email_primary")
        driver.find_element_by_id("name_last").click()
        try:
            WebDriverWait(driver, 5).until(EC.alert_is_present())
            alert = driver.switch_to_alert()
            self.assertTrue("Please provide a valid email address" in alert.text)
            alert.accept()
        except TimeoutException:
            self.failMsg = self.failMsg + "Popup not displayed on losing focus from Email"
            raise TimeoutException(self.failMsg)
        except AssertionError:
            self.failMsg = self.failMsg + "Wrong Popup displayed on losing focus from Email. Popup text: " + alert.text
            raise AssertionError(self.failMsg)
        Utilities.enterText(driver, "phone_home_1", testData.phone_home[0:3])
        Utilities.enterText(driver, "phone_home_2", testData.phone_home[3:6])
        Utilities.enterText(driver, "phone_home_3", testData.phone_home[6:])
        Utilities.enterText(driver, "home_zip", testData.home_zip)
        Utilities.checkUncheckCheckbox(driver, "terms", testData.terms)
        Utilities.clickButton(driver, "button_next_2")
        time.sleep(sleepTime)
        
        assertFinalValidationPopup(self, "Email")

    def test_TC4_ValidatePhone1Required(self):
        testData = self.testData
        driver = self.driver
        
        Utilities.enterText(driver, "name_first", testData.name_first)
        Utilities.enterText(driver, "name_last", testData.name_last)
        Utilities.enterText(driver, "email_primary", testData.email_primary)
        #Utilities.enterText(driver, "phone_home_1", testData.phone_home[0:3])
        Utilities.clearText(driver, "phone_home_1")
        Utilities.enterText(driver, "phone_home_2", testData.phone_home[3:6])
        Utilities.enterText(driver, "phone_home_3", testData.phone_home[6:])
        Utilities.enterText(driver, "home_zip", testData.home_zip)
        Utilities.checkUncheckCheckbox(driver, "terms", testData.terms)
        Utilities.clickButton(driver, "button_next_2")
        time.sleep(sleepTime)
        
        assertFinalValidationPopup(self, "Phone 1")
        
    def test_TC5_ValidatePhone2Required(self):
        testData = self.testData
        driver = self.driver
        
        Utilities.enterText(driver, "name_first", testData.name_first)
        Utilities.enterText(driver, "name_last", testData.name_last)
        Utilities.enterText(driver, "email_primary", testData.email_primary)
        Utilities.enterText(driver, "phone_home_1", testData.phone_home[0:3])
        #Utilities.enterText(driver, "phone_home_2", testData.phone_home[3:6])
        Utilities.clearText(driver, "phone_home_2")
        Utilities.enterText(driver, "phone_home_3", testData.phone_home[6:])
        Utilities.enterText(driver, "home_zip", testData.home_zip)
        Utilities.checkUncheckCheckbox(driver, "terms", testData.terms)
        Utilities.clickButton(driver, "button_next_2")
        time.sleep(sleepTime)
        
        assertFinalValidationPopup(self, "Phone 2")
        
    def test_TC6_ValidatePhone3Required(self):
        testData = self.testData
        driver = self.driver
        
        Utilities.enterText(driver, "name_first", testData.name_first)
        Utilities.enterText(driver, "name_last", testData.name_last)
        Utilities.enterText(driver, "email_primary", testData.email_primary)
        Utilities.enterText(driver, "phone_home_1", testData.phone_home[0:3])
        Utilities.enterText(driver, "phone_home_2", testData.phone_home[3:6])
        #Utilities.enterText(driver, "phone_home_3", testData.phone_home[6:])
        Utilities.clearText(driver, "phone_home_3")
        Utilities.enterText(driver, "home_zip", testData.home_zip)
        Utilities.checkUncheckCheckbox(driver, "terms", testData.terms)
        Utilities.clickButton(driver, "button_next_2")
        time.sleep(sleepTime)
        
        assertFinalValidationPopup(self, "Phone 3")
        
    def test_TC7_ValidateZipCodeRequired(self):
        testData = self.testData
        driver = self.driver
        
        Utilities.enterText(driver, "name_first", testData.name_first)
        Utilities.enterText(driver, "name_last", testData.name_last)
        Utilities.enterText(driver, "email_primary", testData.email_primary)
        Utilities.enterText(driver, "phone_home_1", testData.phone_home[0:3])
        Utilities.enterText(driver, "phone_home_2", testData.phone_home[3:6])
        Utilities.enterText(driver, "phone_home_3", testData.phone_home[6:])
        #Utilities.enterText(driver, "home_zip", testData.home_zip)
        Utilities.clearText(driver, "home_zip")
        Utilities.checkUncheckCheckbox(driver, "terms", testData.terms)
        Utilities.clickButton(driver, "button_next_2")
        time.sleep(sleepTime)
        
        assertFinalValidationPopup(self, "Zip Code")

    def test_TC8_ValidateEmailValidation(self):
        #testData = self.testData
        driver = self.driver        
        #Utilities.enterText(driver, "name_first", testData.name_first)
        #Utilities.enterText(driver, "name_last", testData.name_last)
        Utilities.enterText(driver, "email_primary", "test")
        name_last = driver.find_element_by_id("name_last")
        name_last.click()
        time.sleep(sleepTime)
        
        try:
            WebDriverWait(driver, 5).until(EC.alert_is_present())
            alert = driver.switch_to_alert()
            self.assertTrue("Please provide a valid email address" in alert.text)
            alert.accept()
        except TimeoutException:
            self.failMsg = self.failMsg + "Popup not displayed on entering invalid Email"
            raise TimeoutException(self.failMsg)
        except AssertionError:
            self.failMsg = self.failMsg + "Wrong Popup displayed on entering invalid Email" + alert.text
            raise AssertionError(self.failMsg)
        
    def test_TC9_ValidatePhoneAutoMoveCursor(self):
        testData = self.testData
        driver = self.driver
        
        Utilities.enterText(driver, "name_first", testData.name_first)
        Utilities.enterText(driver, "name_last", testData.name_last)
        Utilities.enterText(driver, "email_primary", testData.email_primary)
        Utilities.clearText(driver, "phone_home_1")
        Utilities.clearText(driver, "phone_home_2")
        Utilities.clearText(driver, "phone_home_3")
        Utilities.enterText(driver, "phone_home_1", testData.phone_home[0:3])
        try:
            currentActiveElement = driver.switchTo().activeElement();
            self.assertTrue("phone_home_2" in currentActiveElement.get_attribute("id"))
        except AssertionError:
            self.failMsg = self.failMsg + "Cursor did not move to Phone 2 after entering Phone 1"
            raise AssertionError(self.failMsg)
        Utilities.enterText(driver, "phone_home_2", testData.phone_home[3:6])
        try:
            currentActiveElement = driver.switch_to_active_element();
            self.assertTrue("phone_home_3" in currentActiveElement.get_attribute("id"))
        except AssertionError:
            self.failMsg = self.failMsg + "Cursor did not move to Phone 3 after entering Phone 2"
            raise AssertionError(self.failMsg)
        #Utilities.enterText(driver, "phone_home_3", testData.phone_home[6:])
        
    def test_TC10_ValidateTermsAreCheckedByDefault(self):
        driver = self.driver
        
        terms = driver.find_element_by_id("terms")
        try:
            self.assertTrue(terms.is_selected())
        except AssertionError:
            self.failMsg = self.failMsg + "Terms and Conditions are not checked by default"
            raise AssertionError(self.failMsg)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(test_ValidatePersonalDetails("test_TC10_ValidateTermsAreCheckedByDefault"))
    suite.addTest(test_ValidatePersonalDetails("test_TC1_ValidateFirstNameRequired"))
    suite.addTest(test_ValidatePersonalDetails("test_TC2_ValidateLastNameRequired"))
    suite.addTest(test_ValidatePersonalDetails("test_TC3_ValidateEmailRequired"))
    suite.addTest(test_ValidatePersonalDetails("test_TC4_ValidatePhone1Required"))
    suite.addTest(test_ValidatePersonalDetails("test_TC5_ValidatePhone2Required"))
    suite.addTest(test_ValidatePersonalDetails("test_TC6_ValidatePhone3Required"))
    suite.addTest(test_ValidatePersonalDetails("test_TC7_ValidateZipCodeRequired"))
    suite.addTest(test_ValidatePersonalDetails("test_TC8_ValidateEmailValidation"))
    suite.addTest(test_ValidatePersonalDetails("test_TC9_ValidatePhoneAutoMoveCursor"))
    return suite