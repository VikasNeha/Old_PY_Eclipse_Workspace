'''
Created on May 21, 2013

@author: Vikas
'''
import unittest

from root.nested import Utilities, FormFunctions, TestDataStructure, PersonalLoanFormSuper
from selenium.common.exceptions import TimeoutException

def setupTestData(self):
    self.testData = TestDataStructure.setUpTestDataForTC8("Alabama", 
                                     "Up to $100", 
                                     "test", "test", "test@test.com", "3333333333", "33333", True, 
                                     "Employment", "123 test", "test", "NO, I AM NOT", "3333", 
                                     "I have a checking account")
    
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
    
    #Enter Monthly Income
    FormFunctions.enterIncomeMonthlyNet(driver, testData.income_monthly_net)
    FormFunctions.assertTextInFormArea(driver, "Do you have a bank account", "Monthly Income")
    
    #Select Bank Account Type
    FormFunctions.selectBankAccountType(driver, testData.bank_account_type)
    FormFunctions.assertTextInFormArea(driver, "Do you have Direct Deposit", "Bank Account Type")

class test_AppRejectsDirectDeposit(unittest.TestCase):
    def setUp(self):
        PersonalLoanFormSuper.setUp(self, "Personal Loan Form: TC8: Testing rejection of app due to No Direct Deposit")
        setupTestData(self)
        TCsSpecificSetup(self)
        
    def tearDown(self):
        PersonalLoanFormSuper.tearDownAndQuit(self)
    
    def test_TC1_AppRejectsDirectDepositNo(self):
        driver = self.driver        
        #Select Direct Deposit
        FormFunctions.selectDirectDeposit(driver, "No")
        
        #Assert Final Result
        try:
            FormFunctions.assertFinalResultRejected(driver)
        except TimeoutException:
            self.failMsg = "Application was not rejected on selecting No Direct Deposit"
            raise AssertionError(self.failMsg)
        
    def test_TC2_AppRejectsDirectDepositDontKnow(self):
        driver = self.driver        
        #Select Direct Deposit
        FormFunctions.selectDirectDeposit(driver, "I don't know")
        
        #Assert Final Result
        try:
            FormFunctions.assertFinalResultRejected(driver)
        except TimeoutException:
            self.failMsg = "Application was not rejected on selecting Dont Know Direct Deposit"
            raise AssertionError(self.failMsg)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(test_AppRejectsDirectDeposit("test_TC1_AppRejectsDirectDepositNo"))
    suite.addTest(test_AppRejectsDirectDeposit("test_TC2_AppRejectsDirectDepositDontKnow"))
    return suite