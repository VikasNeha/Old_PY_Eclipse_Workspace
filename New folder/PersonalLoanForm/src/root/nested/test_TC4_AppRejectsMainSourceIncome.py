'''
Created on May 21, 2013

@author: Vikas
'''
import unittest

from root.nested import Utilities, FormFunctions, TestDataStructure, PersonalLoanFormSuper
from selenium.common.exceptions import TimeoutException

def setupTestData(self):
    self.testData = TestDataStructure.setUpTestDataForTC4("Alabama", 
                                     "Up to $100", 
                                     "test", "test", "test@test.com", "3333333333", "33333", True, "Benefits (social security, etc.)")
    
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


class test_AppRejectsMainSourceIncome(unittest.TestCase):
    def setUp(self):
        PersonalLoanFormSuper.setUp(self, "Personal Loan Form: TC4: Testing rejection of app due to Social Security Benefits")
        setupTestData(self)
        TCsSpecificSetup(self)
        
    def tearDown(self):
        PersonalLoanFormSuper.tearDownAndQuit(self)
    
    def test_TC1_AppRejectsMainSourceIncome(self):
        testData = self.testData
        driver = self.driver
        
        #Select Main Source of Income
        FormFunctions.selectIncomeSource(driver, testData.income_source)
        
        #Assert Final Result
        try:
            FormFunctions.assertFinalResultRejected(driver)
        except TimeoutException:
            self.failMsg = "Application was not rejected on selecting Social Security Benefits as Main Source of Income"
            raise AssertionError(self.failMsg)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(test_AppRejectsMainSourceIncome("test_TC1_AppRejectsMainSourceIncome"))
    return suite