'''
Created on May 21, 2013

@author: Vikas
'''
import unittest

from root.nested import Utilities, FormFunctions, TestDataStructure, PersonalLoanFormSuper
from datetime import datetime, timedelta

def setupTestData(self):
    self.testData = TestDataStructure.setUpTestDataForTC9("Alabama", 
                                     "Up to $100", 
                                     "test", "test", "test@test.com", "3333333333", "33333", True, 
                                     "Employment", "123 test", "test", "NO, I AM NOT", "3333", 
                                     "I have a checking account", "YES")
    
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



class test_NextPayDateCalculations(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        PersonalLoanFormSuper.setUp(self, "Personal Loan Form: TC9: Testing calcutations of next pay date")
        setupTestData(self)
        TCsSpecificSetup(self)
    def setUp(self):
        pass
    @classmethod
    def tearDownClass(self):
        PersonalLoanFormSuper.tearDownClass(self)
    def tearDown(self):
        PersonalLoanFormSuper.tearDown(self)
    
    def test_TC1_NextPayDateCalculationsWeekly(self):
        driver = self.driver        
        
        #Select Income Frequency
        FormFunctions.selectIncomeFrequency(driver, "Weekly")
        FormFunctions.assertTextInFormArea(driver, "Select your next 2 Paycheck Dates", "Income Frequency")
        
        #Select Next Pay Date 1
        calendarElement = driver.find_element_by_class_name("ui-datepicker-calendar")
        nextClickableDateElement = calendarElement.find_element_by_tag_name("a")
        nextClickableDateElement.click()
        
        #Get Next Pay Date Values
        nextPayDate1 = datetime.strptime(driver.find_element_by_id("nextpaydate1").get_attribute("value"), '%m/%d/%Y')
        nextPayDate2Actual = datetime.strptime(driver.find_element_by_id("nextpaydate2").get_attribute("value"), '%m/%d/%Y')
        
        td = timedelta(days=7)
        nextPayDate2Expected = nextPayDate1 + td
        if (nextPayDate2Expected == nextPayDate2Actual):
            self.assertTrue(True)
        else:
            self.failMsg = "Next Pay date 2 not correctly calculated. Expected: " + nextPayDate2Expected.strftime('%m/%d/%Y') + ", Actual: " + nextPayDate2Actual.strftime('%m/%d/%Y')
            self.assertTrue(False, self.failMsg)
            
    def test_TC2_NextPayDateCalculationsEveryOtherWeek(self):
        driver = self.driver
        
        FormFunctions.clickBackButton(driver)
        
        FormFunctions.assertTextInFormArea(driver, "How often are you being paid", "Direct Deposit")
        
        #Select Income Frequency
        FormFunctions.selectIncomeFrequency(driver, "Every other week")
        FormFunctions.assertTextInFormArea(driver, "Select your next 2 Paycheck Dates", "Income Frequency")
        
        #Select Next Pay Date 1
        calendarElement = driver.find_element_by_class_name("ui-datepicker-calendar")
        nextClickableDateElement = calendarElement.find_element_by_tag_name("a")
        nextClickableDateElement.click()
        
        #Get Next Pay Date Values
        nextPayDate1 = datetime.strptime(driver.find_element_by_id("nextpaydate1").get_attribute("value"), '%m/%d/%Y')
        nextPayDate2Actual = datetime.strptime(driver.find_element_by_id("nextpaydate2").get_attribute("value"), '%m/%d/%Y')
        
        td = timedelta(days=14)
        nextPayDate2Expected = nextPayDate1 + td
        if (nextPayDate2Expected == nextPayDate2Actual):
            self.assertTrue(True)
        else:
            self.failMsg = "Next Pay date 2 not correctly calculated. Expected: " + nextPayDate2Expected.strftime('%m/%d/%Y') + ", Actual: " + nextPayDate2Actual.strftime('%m/%d/%Y')
            self.assertTrue(False, self.failMsg)
            
    def test_TC3_NextPayDateCalculationsTwiceAMonth(self):
        driver = self.driver
        
        FormFunctions.clickBackButton(driver)
        
        FormFunctions.assertTextInFormArea(driver, "How often are you being paid", "Direct Deposit")
        
        #Select Income Frequency
        FormFunctions.selectIncomeFrequency(driver, "Twice a month")
        FormFunctions.assertTextInFormArea(driver, "Select your next 2 Paycheck Dates", "Income Frequency")
        
        #Select Next Pay Date 1
        calendarElement = driver.find_element_by_class_name("ui-datepicker-calendar")
        nextClickableDateElement = calendarElement.find_element_by_tag_name("a")
        nextClickableDateElement.click()
        
        #Get Next Pay Date Values
        nextPayDate1 = datetime.strptime(driver.find_element_by_id("nextpaydate1").get_attribute("value"), '%m/%d/%Y')
        nextPayDate2Actual = datetime.strptime(driver.find_element_by_id("nextpaydate2").get_attribute("value"), '%m/%d/%Y')
        
        td = timedelta(days=14)
        nextPayDate2Expected = nextPayDate1 + td
        if (nextPayDate2Expected == nextPayDate2Actual):
            self.assertTrue(True)
        else:
            self.failMsg = "Next Pay date 2 not correctly calculated. Expected: " + nextPayDate2Expected.strftime('%m/%d/%Y') + ", Actual: " + nextPayDate2Actual.strftime('%m/%d/%Y')
            self.assertTrue(False, self.failMsg)
            
    def test_TC4_NextPayDateCalculationsMonthly(self):
        driver = self.driver
        
        FormFunctions.clickBackButton(driver)
        
        FormFunctions.assertTextInFormArea(driver, "How often are you being paid", "Direct Deposit")
        
        #Select Income Frequency
        FormFunctions.selectIncomeFrequency(driver, "Monthly")
        FormFunctions.assertTextInFormArea(driver, "Select your next 2 Paycheck Dates", "Income Frequency")
        
        #Select Next Pay Date 1
        calendarElement = driver.find_element_by_class_name("ui-datepicker-calendar")
        nextClickableDateElement = calendarElement.find_element_by_tag_name("a")
        nextClickableDateElement.click()
        
        #Get Next Pay Date Values
        nextPayDate1 = datetime.strptime(driver.find_element_by_id("nextpaydate1").get_attribute("value"), '%m/%d/%Y')
        nextPayDate2Actual = datetime.strptime(driver.find_element_by_id("nextpaydate2").get_attribute("value"), '%m/%d/%Y')
        
        #td = timedelta(days=30)
        nextPayDate2Expected = nextPayDate1.replace(month=nextPayDate1.month+1)
        if (nextPayDate2Expected == nextPayDate2Actual):
            self.assertTrue(True)
        else:
            self.failMsg = "Next Pay date 2 not correctly calculated. Expected: " + nextPayDate2Expected.strftime('%m/%d/%Y') + ", Actual: " + nextPayDate2Actual.strftime('%m/%d/%Y')
            self.assertTrue(False, self.failMsg)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(test_NextPayDateCalculations("test_TC1_NextPayDateCalculationsWeekly"))
    suite.addTest(test_NextPayDateCalculations("test_TC2_NextPayDateCalculationsEveryOtherWeek"))
    suite.addTest(test_NextPayDateCalculations("test_TC3_NextPayDateCalculationsTwiceAMonth"))
    suite.addTest(test_NextPayDateCalculations("test_TC4_NextPayDateCalculationsMonthly"))
    return suite