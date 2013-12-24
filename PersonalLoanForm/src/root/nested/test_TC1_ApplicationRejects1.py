'''
Created on May 21, 2013

@author: Vikas
'''
import unittest

from root.nested import Utilities, FormFunctions, TestDataStructure, PersonalLoanFormSuper
    

class test_ApplicationRejects1(unittest.TestCase):
    def setUp(self):
        PersonalLoanFormSuper.setUp(self, "Personal Loan Form: TC1: Testing app rejection")
        
    def tearDown(self):
        PersonalLoanFormSuper.tearDownAndQuit(self)
    
    def test_ApplicationRejects1(self):
        testData = TestDataStructure.setUpTestDataForTC1("Alabama", 
                                     "Up to $100", 
                                     "test", "test", "test@test.com", "3333333333", "33333", True, 
                                     "Employment", 
                                     "123 test", "test", 
                                     "NO, I AM NOT", 
                                     "3333", 
                                     "I have a checking account", 
                                     "YES", 
                                     "Weekly", 
                                     "tester", "4444444444", "2+ years", 
                                     "test", "222371863", "999999999", 
                                     "Alabama", "3333",
                                     "March", "3", "1983", "333", "33", "3333")
        driver = self.driver
        Utilities.openURL(driver, self.appURL)
        self.assertIn("Personal Loans", driver.title)
        
        
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
        
        #Enter Bank Details
        FormFunctions.enterBankDetails(driver, testData.bank_name, testData.bank_aba, testData.bank_account)
        FormFunctions.assertTextInFormArea(driver, "Your driving license state", "Bank Details")
        
        #Enter Driving License Details
        FormFunctions.selectLicenseDetails(driver, testData.state_issued_id, testData.state_id_number)
        FormFunctions.assertTextInFormArea(driver, "Date of Birth", "License Details")
        
        #Enter Date Of Birth and SSN
        FormFunctions.enterDOB_SSN(driver, testData.dob_m, testData.dob_d, testData.dob_y, testData.ssn_area, testData.ssn_group, testData.ssn_serial)
        FormFunctions.assertTextInFormArea(driver, "Your application is now ready to be", "DOB & SSN Details")
        
        #Submit the Form
        FormFunctions.submitForm(driver)
        
        #Assert First Warning
        try:
            popUpBox = driver.find_element_by_class_name("popup")
            self.assertTrue("Most borrowers receive less than $1,000" in popUpBox.text)
            try:
                allButtons = popUpBox.find_elements_by_tag_name("input")
                for currentButton in allButtons:
                    if currentButton.get_attribute("type") == "button" and currentButton.get_attribute("value") == "Yes":
                        currentButton.click()
                        break
            except Exception as msg:
                print msg
        except AssertionError:
            self.failMsg = self.failMsg + "Wrong first warning displayed on submitting the form. Warning text: " + popUpBox.text
            raise AssertionError(self.failMsg)
        except Exception:
            self.failMsg = "First warning not displayed on submitting the form"
            raise AssertionError(self.failMsg)
        
        #Assert Second Warning
        try:
            popUpBox = driver.find_element_by_class_name("popup")
            self.assertTrue("Are you sure you will accept a loan for less than $1,000" in popUpBox.text)
            try:
                allButtons = popUpBox.find_elements_by_tag_name("input")
                for currentButton in allButtons:
                    if currentButton.get_attribute("type") == "button" and currentButton.get_attribute("value") == "Accept My Loan":
                        currentButton.click()
                        break
            except Exception as msg:
                print msg
        except AssertionError:
            self.failMsg = self.failMsg + "Wrong second warning displayed on submitting the form. Warning text: " + popUpBox.text
            raise AssertionError(self.failMsg)
        except Exception:
            self.failMsg = "Second warning not displayed on submitting the form"
            raise AssertionError(self.failMsg)
        
        #Assert Final Result
        FormFunctions.assertFinalResultRejected(driver)
 
       
def suite():
    suite = unittest.TestSuite()
    suite.addTest(test_ApplicationRejects1("test_ApplicationRejects1"))
    return suite