'''
Created on May 21, 2013

@author: Vikas
'''
import unittest

from root.nested import Utilities, FormFunctions, TestDataStructure, PersonalLoanFormSuper
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setupTestData(self):
    self.testData = TestDataStructure.setUpTestDataForTC11("Alabama", 
                                     "Up to $100", 
                                     "test", "test", "test@test.com", "3333333333", "33333", True, 
                                     "Employment", "123 test", "test", "NO, I AM NOT", "3333", 
                                     "I have a checking account", "YES",
                                     "Weekly", 
                                     "tester", "4444444444", "2+ years",
                                     "test", "222371853", "999999999")
    
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
    
    #Select Direct Deposit
    FormFunctions.selectDirectDeposit(driver, testData.direct_deposit)
    FormFunctions.assertTextInFormArea(driver, "How often are you being paid", "Direct Deposit")

    #Select Income Frequency
    FormFunctions.selectIncomeFrequency(driver, testData.income_frequency)
    FormFunctions.assertTextInFormArea(driver, "Select your next 2 Paycheck Dates", "Income Frequency")
    
    #Select Next 2 Paycheck Dates
    FormFunctions.selectNextPayDates(driver)
    FormFunctions.assertTextInFormArea(driver, "Employer Name", "Next Paycheck Dates")
    
    #Enter Employer Details
    FormFunctions.enterEmployerDetails(driver, testData.employer_name, testData.phone_work, testData.employment_length)
    FormFunctions.assertTextInFormArea(driver, "Into what account would you", "Employer Details")

def assertWarningPopup(self):
    driver = self.driver
    try:
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to_alert()
        self.assertTrue("The Bank Routing Number you have entered appears to be incorrect" in alert.text)
        alert.accept()
    except TimeoutException:
        self.failMsg = self.failMsg + "Warning not displayed if bank routing no is incorrect"
        raise AssertionError(self.failMsg)
        alert.accept()
    except AssertionError:
        self.failMsg = self.failMsg + "Wrong warning displayed if bank routing no is incorrect. Popup text: " + alert.text
        raise AssertionError(self.failMsg)
        alert.accept()

class test_BankValidations(unittest.TestCase):
        
    def setUp(self):
        PersonalLoanFormSuper.setUp(self, "Personal Loan Form: TC11: Incorrect Bank Routing No arenot allowed")
        setupTestData(self)
        TCsSpecificSetup(self)
   
    def tearDown(self):
        PersonalLoanFormSuper.tearDownAndQuit(self)
    
    def test_TC1_BankRoutingMod10Validation(self):
        driver = self.driver        
        testData = self.testData
        
        #Enter Bank Details
        Utilities.enterText(driver, "bank_name", testData.bank_name)
        Utilities.enterText(driver, "bank_aba", testData.bank_aba)
        driver.find_element_by_id("bank_account").click()
        assertWarningPopup(self)
    
def suite():
    suite = unittest.TestSuite()
    suite.addTest(test_BankValidations("test_TC1_BankRoutingMod10Validation"))

    return suite