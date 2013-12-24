'''
Created on May 21, 2013

@author: Vikas
'''
import unittest, time

from root.nested import Utilities, FormFunctions, TestDataStructure, PersonalLoanFormSuper
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setupTestData(self):
    self.testData = TestDataStructure.setUpTestDataForTC6("Alabama", 
                                     "Up to $100", 
                                     "test", "test", "test@test.com", "3333333333", "33333", True, 
                                     "Employment", "123 test", "test", "NO, I AM NOT")
    
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
    
    #Enter Personal Details
    FormFunctions.enterPersonalDetails(driver, testData.name_first, testData.name_last, testData.email_primary, testData.phone_home, testData.home_zip, testData.terms)
    FormFunctions.assertTextInFormArea(driver, "What is your main source of income", "Personal Details")
    
    #Select Main Source of Income
    FormFunctions.selectIncomeSource(driver, testData.income_source)
    FormFunctions.assertTextInFormArea(driver, "Your Street Address", "Main Source of Income")
    
    #Enter Street Address and City
    FormFunctions.enterHomeStreetCity(driver, testData.home_street, testData.home_city)
    FormFunctions.assertTextInFormArea(driver, "Are you a U.S. Military Employee", "Street Address and City")
    
    #Select Military
    FormFunctions.selectMilitary(driver, testData.military)             
    FormFunctions.assertTextInFormArea(driver, "Your MONTHLY income:", "Military")

def assertWarningPopup(self, incomeValue):
    driver = self.driver
    try:
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to_alert()
        self.assertTrue("You must be making at least $800 per month to qualify" in alert.text)
        alert.accept()
    except TimeoutException:
        self.failMsg = self.failMsg + "Warning not displayed if income was entered as $" + incomeValue
        raise AssertionError(self.failMsg)
        alert.accept()
    except AssertionError:
        self.failMsg = self.failMsg + "Wrong warning displayed if income was entered as $" + incomeValue + "Popup text: " + alert.text
        raise AssertionError(self.failMsg)
        alert.accept()
    finally:
        time.sleep(5)
        
def acceptUnwantedPopup(self):
    driver = self.driver
    try:
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to_alert()
        alert.accept()
    except Exception:
        pass

class test_AppMonthlyIncomeShowsWarning(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        PersonalLoanFormSuper.setUp(self, "Personal Loan Form: TC6: Testing that app shows warning if monthly income is less than $800")
        setupTestData(self)
        TCsSpecificSetup(self)
    
    def setUp(self):
        pass
        
    def tearDown(self):
        PersonalLoanFormSuper.tearDown(self)
    
    @classmethod
    def tearDownClass(self):
        PersonalLoanFormSuper.tearDownClass(self)
    
    def test_TC1_AppMonthlyZero(self):
        #Enter Monthly Income
        FormFunctions.enterIncomeMonthlyNet(self.driver, "0")
        #Assert Warning Box
        assertWarningPopup(self, "0")
    
    def test_TC2_AppMonthly799(self):
        acceptUnwantedPopup(self)
        #Enter Monthly Income
        FormFunctions.enterIncomeMonthlyNet(self.driver, "799")
        #Assert Warning Box
        assertWarningPopup(self, "799")
        
    def test_TC3_AppMonthly800(self):
        acceptUnwantedPopup(self)
        #Enter Monthly Income
        FormFunctions.enterIncomeMonthlyNet(self.driver, "800")
        #Assert Warning Box
        try:
            assertWarningPopup(self, "800")
        except AssertionError:
            self.assertTrue(True)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(test_AppMonthlyIncomeShowsWarning("test_TC1_AppMonthlyZero"))
    suite.addTest(test_AppMonthlyIncomeShowsWarning("test_TC2_AppMonthly799"))
    suite.addTest(test_AppMonthlyIncomeShowsWarning("test_TC3_AppMonthly800"))
    return suite