'''
Created on May 21, 2013

@author: Vikas
'''
import unittest, time

from root.nested import Utilities, FormFunctions, TestDataStructure, PersonalLoanFormSuper
from selenium.common.exceptions import TimeoutException
from root.nested.FormFunctions import sleepTime

def setupTestData(self):
    self.testData = TestDataStructure.setUpTestDataForTC7("Alabama", 
                                     "Up to $100", 
                                     "test", "test", "test@test.com", "3333333333", "33333", True, 
                                     "Employment", "123 test", "test", "NO, I AM NOT", "3333")
    
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

class test_AppRejectsBankAccount(unittest.TestCase):
    def setUp(self):
        PersonalLoanFormSuper.setUp(self, "Personal Loan Form: TC7: Testing rejection of app due to Savings or No Bank Account")
        setupTestData(self)
        TCsSpecificSetup(self)
        
    def tearDown(self):
        PersonalLoanFormSuper.tearDownAndQuit(self)
    
    def test_TC1_AppRejectsBankAccountSavingsAcc(self):
        driver = self.driver
        
        #Select Bank Account Type
        FormFunctions.selectBankAccountType(driver, "I only have a savings account")
        
        #Assert Final Result
        try:
            FormFunctions.assertFinalResultRejectedBankAcount(driver)
        except TimeoutException:
            self.failMsg = "Application was not rejected on selecting Savings Account as Bank Account"
            raise AssertionError(self.failMsg)
        
    def test_TC2_AppRejectsBankAccountNoAcc(self):
        driver = self.driver
        
        #Select Bank Account Type
        FormFunctions.selectBankAccountType(driver, "I do not have a bank account.")
        
        time.sleep(sleepTime)
        popUpBox = driver.find_element_by_class_name("popup")
        allOptions = popUpBox.find_elements_by_tag_name("input")
        for currentOption in allOptions:
            if currentOption.get_attribute("value") == "no":
                currentOption.click()
                break
        for currentOption in allOptions:
            if currentOption.get_attribute("value") == "Continue":
                currentOption.click()
                break
        
        #Assert Final Result
        try:
            FormFunctions.assertFinalResultRejectedBankAcount(driver)
        except TimeoutException:
            self.failMsg = "Application was not rejected on selecting No Bank Account"
            raise AssertionError(self.failMsg)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(test_AppRejectsBankAccount("test_TC1_AppRejectsBankAccountSavingsAcc"))
    suite.addTest(test_AppRejectsBankAccount("test_TC2_AppRejectsBankAccountNoAcc"))
    return suite