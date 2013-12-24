'''
Created on May 21, 2013

@author: Vikas
'''
import unittest

from root.nested import Utilities, FormFunctions, TestDataStructure, PersonalLoanFormSuper
from selenium.common.exceptions import TimeoutException

def setupTestData(self):
    self.testData = TestDataStructure.setUpTestDataForTC5("Alabama", 
                                     "Up to $100", 
                                     "test", "test", "test@test.com", "3333333333", "33333", True, 
                                     "Employment", "123 test", "test")
    
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


class test_AppRedirectsPioneerMilitary(unittest.TestCase):
    def setUp(self):
        PersonalLoanFormSuper.setUp(self, "Personal Loan Form: TC5: Testing redirection of app due to Military Dependent or Member")
        setupTestData(self)
        TCsSpecificSetup(self)
        
    def tearDown(self):
        PersonalLoanFormSuper.tearDownAndQuit(self)
    
    def test_TC1_AppRedirectsPioneerMilitaryMember(self):
        driver = self.driver
        
        #Select Military
        FormFunctions.selectMilitary(driver, "I AM member of Armed Forces") 
        
        #Assert Final Result
        try:
            FormFunctions.assertFinalResultRedirectedToPioneer(driver)
        except TimeoutException:
            self.failMsg = "Application was not redirected to Pioneer Application on selecting Military Member"
            raise AssertionError(self.failMsg)
    
    def test_TC2_AppRedirectsPioneerMilitaryDependent(self):
        driver = self.driver
        
        #Select Military
        FormFunctions.selectMilitary(driver, "I AM a Dependent") 
        
        #Assert Final Result
        try:
            FormFunctions.assertFinalResultRedirectedToPioneer(driver)
        except TimeoutException:
            self.failMsg = "Application was not redirected to Pioneer Application on selecting Military Dependent"
            raise AssertionError(self.failMsg)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(test_AppRedirectsPioneerMilitary("test_TC1_AppRedirectsPioneerMilitaryMember"))
    suite.addTest(test_AppRedirectsPioneerMilitary("test_TC2_AppRedirectsPioneerMilitaryDependent"))
    return suite