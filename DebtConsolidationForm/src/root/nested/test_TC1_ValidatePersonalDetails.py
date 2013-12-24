'''
Created on May 21, 2013

@author: Vikas
'''
import unittest

from root.nested import DebtConsolidationFormSuper, TestDataStructure, FormFunctions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def setupTestData(self):
    self.testData = TestDataStructure.setUpTestDataForTC1("less than $1,000", "test", "test", "test@test.com", "3333333333", "Alabama")

def TCsSpecificSetup(self):
    driver = self.driver
    driver.get(self.appURL)
    self.assertTrue("Credit Counseling", driver.title)

def AssertFinalWarnings(self, WarningToAssert):
    driver = self.driver
    errorBox = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.errors.show")))
    try:
        self.assertTrue(WarningToAssert in errorBox.text)
    except AssertionError:
        self.failMsg = "Expected Warning not displayed. Errors displayed: " + errorBox.text
        raise AssertionError(self.failMsg)

class TC1_ValidateLoanAmount(unittest.TestCase):
    
    def setUp(self):
        DebtConsolidationFormSuper.setUp(self, "TC1: Loan Amount should be greater than 0")
        setupTestData(self)
        TCsSpecificSetup(self)
        
    def tearDown(self):
        DebtConsolidationFormSuper.tearDown(self)
    
    def test_TC1_ValidateLoanAmount(self):
        testData = self.testData
        driver = self.driver        
        testData.debt_amount = "Total Unsecured Debt"
        
        FormFunctions.selectLoanAmount(driver, testData.debt_amount)
        FormFunctions.enterFirstName(driver, testData.first_name)
        FormFunctions.enterLastName(driver, testData.last_name)
        FormFunctions.enterEmail(driver, testData.email)
        FormFunctions.enterPhone(driver, testData.phone)
        FormFunctions.selectState(driver, testData.state)
        FormFunctions.submitForm(driver)
        
        AssertFinalWarnings(self, "Invalid Debt Amount")
        
class TC2_FirstNameLengthZero(unittest.TestCase):
    
    def setUp(self):
        DebtConsolidationFormSuper.setUp(self, "TC2: First Name blank")
        setupTestData(self)
        TCsSpecificSetup(self)
        
    def tearDown(self):
        DebtConsolidationFormSuper.tearDown(self)
    
    def test_TC2_FirstNameLengthZero(self):
        testData = self.testData
        driver = self.driver
        
        FormFunctions.selectLoanAmount(driver, testData.debt_amount)
        #FormFunctions.enterFirstName(driver, testData.first_name)
        FormFunctions.enterLastName(driver, testData.last_name)
        FormFunctions.enterEmail(driver, testData.email)
        FormFunctions.enterPhone(driver, testData.phone)
        FormFunctions.selectState(driver, testData.state)
        FormFunctions.submitForm(driver)
        
        AssertFinalWarnings(self, "Is that really your first name")
        
class TC3_FirstNameLengthOne(unittest.TestCase):
    
    def setUp(self):
        DebtConsolidationFormSuper.setUp(self, "TC3: First Name with Length One")
        setupTestData(self)
        TCsSpecificSetup(self)
        
    def tearDown(self):
        DebtConsolidationFormSuper.tearDown(self)
    
    def test_TC3_FirstNameLengthOne(self):
        testData = self.testData
        driver = self.driver
        testData.first_name = "a"
        
        FormFunctions.selectLoanAmount(driver, testData.debt_amount)
        FormFunctions.enterFirstName(driver, testData.first_name)
        FormFunctions.enterLastName(driver, testData.last_name)
        FormFunctions.enterEmail(driver, testData.email)
        FormFunctions.enterPhone(driver, testData.phone)
        FormFunctions.selectState(driver, testData.state)
        FormFunctions.submitForm(driver)
        
        AssertFinalWarnings(self, "Is that really your first name")

class TC4_LastNameLengthZero(unittest.TestCase):
    
    def setUp(self):
        DebtConsolidationFormSuper.setUp(self, "TC4: Last Name blank")
        setupTestData(self)
        TCsSpecificSetup(self)
        
    def tearDown(self):
        DebtConsolidationFormSuper.tearDown(self)
    
    def test_TC4_LastNameLengthZero(self):
        testData = self.testData
        driver = self.driver
        
        FormFunctions.selectLoanAmount(driver, testData.debt_amount)
        FormFunctions.enterFirstName(driver, testData.first_name)
        #FormFunctions.enterLastName(driver, testData.last_name)
        FormFunctions.enterEmail(driver, testData.email)
        FormFunctions.enterPhone(driver, testData.phone)
        FormFunctions.selectState(driver, testData.state)
        FormFunctions.submitForm(driver)
        
        AssertFinalWarnings(self, "Is that really your last name")

class TC5_LastNameLengthOne(unittest.TestCase):
    
    def setUp(self):
        DebtConsolidationFormSuper.setUp(self, "TC5: Last Name with Length One")
        setupTestData(self)
        TCsSpecificSetup(self)
        
    def tearDown(self):
        DebtConsolidationFormSuper.tearDown(self)
    
    def test_TC5_FirstNameLengthOne(self):
        testData = self.testData
        driver = self.driver
        testData.last_name = "a"
        
        FormFunctions.selectLoanAmount(driver, testData.debt_amount)
        FormFunctions.enterFirstName(driver, testData.first_name)
        FormFunctions.enterLastName(driver, testData.last_name)
        FormFunctions.enterEmail(driver, testData.email)
        FormFunctions.enterPhone(driver, testData.phone)
        FormFunctions.selectState(driver, testData.state)
        FormFunctions.submitForm(driver)
        
        AssertFinalWarnings(self, "Is that really your last name")

class TC6_EmailBlank(unittest.TestCase):
    
    def setUp(self):
        DebtConsolidationFormSuper.setUp(self, "TC6: Email blank")
        setupTestData(self)
        TCsSpecificSetup(self)
        
    def tearDown(self):
        DebtConsolidationFormSuper.tearDown(self)
    
    def test_TC6_EmailBlank(self):
        testData = self.testData
        driver = self.driver
        
        FormFunctions.selectLoanAmount(driver, testData.debt_amount)
        FormFunctions.enterFirstName(driver, testData.first_name)
        FormFunctions.enterLastName(driver, testData.last_name)
        #FormFunctions.enterEmail(driver, testData.email)
        FormFunctions.enterPhone(driver, testData.phone)
        FormFunctions.selectState(driver, testData.state)
        FormFunctions.submitForm(driver)
        
        AssertFinalWarnings(self, "Invalid email")

class TC7_EmailInvalid(unittest.TestCase):
    
    def setUp(self):
        DebtConsolidationFormSuper.setUp(self, "TC7: Email invalid")
        setupTestData(self)
        TCsSpecificSetup(self)
        
    def tearDown(self):
        DebtConsolidationFormSuper.tearDown(self)
    
    def test_TC7_EmailInvalid(self):
        testData = self.testData
        driver = self.driver
        testData.email = "test@test"
        
        FormFunctions.selectLoanAmount(driver, testData.debt_amount)
        FormFunctions.enterFirstName(driver, testData.first_name)
        FormFunctions.enterLastName(driver, testData.last_name)
        FormFunctions.enterEmail(driver, testData.email)
        FormFunctions.enterPhone(driver, testData.phone)
        FormFunctions.selectState(driver, testData.state)
        FormFunctions.submitForm(driver)
        
        AssertFinalWarnings(self, "Invalid email")

class TC8_PhoneLengthZero(unittest.TestCase):
    
    def setUp(self):
        DebtConsolidationFormSuper.setUp(self, "TC8: Phone blank")
        setupTestData(self)
        TCsSpecificSetup(self)
        
    def tearDown(self):
        DebtConsolidationFormSuper.tearDown(self)
    
    def test_TC8_PhoneLengthZero(self):
        testData = self.testData
        driver = self.driver
        
        FormFunctions.selectLoanAmount(driver, testData.debt_amount)
        FormFunctions.enterFirstName(driver, testData.first_name)
        FormFunctions.enterLastName(driver, testData.last_name)
        FormFunctions.enterEmail(driver, testData.email)
        #FormFunctions.enterPhone(driver, testData.phone)
        FormFunctions.selectState(driver, testData.state)
        FormFunctions.submitForm(driver)
        
        AssertFinalWarnings(self, "Valid 10 digit US phone # required")

class TC9_PhoneLengthNine(unittest.TestCase):
    
    def setUp(self):
        DebtConsolidationFormSuper.setUp(self, "TC9: Phone length 9")
        setupTestData(self)
        TCsSpecificSetup(self)
        
    def tearDown(self):
        DebtConsolidationFormSuper.tearDown(self)
    
    def test_TC9_PhoneLengthNine(self):
        testData = self.testData
        driver = self.driver
        testData.phone = "123456789"
        
        FormFunctions.selectLoanAmount(driver, testData.debt_amount)
        FormFunctions.enterFirstName(driver, testData.first_name)
        FormFunctions.enterLastName(driver, testData.last_name)
        FormFunctions.enterEmail(driver, testData.email)
        FormFunctions.enterPhone(driver, testData.phone)
        FormFunctions.selectState(driver, testData.state)
        FormFunctions.submitForm(driver)
        
        AssertFinalWarnings(self, "Valid 10 digit US phone # required")

class TC10_PhoneLengthEleven(unittest.TestCase):
    
    def setUp(self):
        DebtConsolidationFormSuper.setUp(self, "TC10: Phone length 11")
        setupTestData(self)
        TCsSpecificSetup(self)
        
    def tearDown(self):
        DebtConsolidationFormSuper.tearDown(self)
    
    def test_TC10_PhoneLengthEleven(self):
        testData = self.testData
        driver = self.driver
        testData.phone = "12345678901"
        
        FormFunctions.selectLoanAmount(driver, testData.debt_amount)
        FormFunctions.enterFirstName(driver, testData.first_name)
        FormFunctions.enterLastName(driver, testData.last_name)
        FormFunctions.enterEmail(driver, testData.email)
        FormFunctions.enterPhone(driver, testData.phone)
        FormFunctions.selectState(driver, testData.state)
        FormFunctions.submitForm(driver)
        
        AssertFinalWarnings(self, "Valid 10 digit US phone # required")

class TC11_PhoneInvalid(unittest.TestCase):
    
    def setUp(self):
        DebtConsolidationFormSuper.setUp(self, "TC11: Phone alpha-numeric")
        setupTestData(self)
        TCsSpecificSetup(self)
        
    def tearDown(self):
        DebtConsolidationFormSuper.tearDown(self)
    
    def test_TC11_PhoneInvalid(self):
        testData = self.testData
        driver = self.driver
        testData.phone = "abcdabcd12"
        
        FormFunctions.selectLoanAmount(driver, testData.debt_amount)
        FormFunctions.enterFirstName(driver, testData.first_name)
        FormFunctions.enterLastName(driver, testData.last_name)
        FormFunctions.enterEmail(driver, testData.email)
        FormFunctions.enterPhone(driver, testData.phone)
        FormFunctions.selectState(driver, testData.state)
        FormFunctions.submitForm(driver)
        
        AssertFinalWarnings(self, "Valid 10 digit US phone # required")

class TC12_ValidateState(unittest.TestCase):
    
    def setUp(self):
        DebtConsolidationFormSuper.setUp(self, "TC12: State should be selected")
        setupTestData(self)
        TCsSpecificSetup(self)
        
    def tearDown(self):
        DebtConsolidationFormSuper.tearDown(self)
    
    def test_TC12_ValidateState(self):
        testData = self.testData
        driver = self.driver        
        
        FormFunctions.selectLoanAmount(driver, testData.debt_amount)
        FormFunctions.enterFirstName(driver, testData.first_name)
        FormFunctions.enterLastName(driver, testData.last_name)
        FormFunctions.enterEmail(driver, testData.email)
        FormFunctions.enterPhone(driver, testData.phone)
        #FormFunctions.selectState(driver, testData.state)
        FormFunctions.submitForm(driver)
        
        AssertFinalWarnings(self, "Which US state do you live in")

class TC13_ValidateAllFiedls(unittest.TestCase):
    
    def setUp(self):
        DebtConsolidationFormSuper.setUp(self, "TC13: Validate All Fields")
        setupTestData(self)
        TCsSpecificSetup(self)
        
    def tearDown(self):
        DebtConsolidationFormSuper.tearDown(self)
    
    def test_TC13_ValidateAllFields(self):
        testData = self.testData
        driver = self.driver
        testData.debt_amount = "Total Unsecured Debt"    
        
        FormFunctions.selectLoanAmount(driver, testData.debt_amount)
        #FormFunctions.enterFirstName(driver, testData.first_name)
        #FormFunctions.enterLastName(driver, testData.last_name)
        #FormFunctions.enterEmail(driver, testData.email)
        #FormFunctions.enterPhone(driver, testData.phone)
        #FormFunctions.selectState(driver, testData.state)
        FormFunctions.submitForm(driver)
        
        AssertFinalWarnings(self, "Invalid Debt Amount")
        AssertFinalWarnings(self, "Is that really your first name")
        AssertFinalWarnings(self, "Is that really your last name")
        AssertFinalWarnings(self, "Invalid email")
        AssertFinalWarnings(self, "Valid 10 digit US phone # required")        
        AssertFinalWarnings(self, "Which US state do you live in")


def suite():
    suite = unittest.TestSuite()
    #suite.addTest(TC1_ValidateLoanAmount("test_TC1_ValidateLoanAmount"))
    #suite.addTest(TC2_FirstNameLengthZero("test_TC2_FirstNameLengthZero"))
    #suite.addTest(TC3_FirstNameLengthOne("test_TC3_FirstNameLengthOne"))
    #suite.addTest(TC4_LastNameLengthZero("test_TC4_LastNameLengthZero"))
    #suite.addTest(TC5_LastNameLengthOne("test_TC5_FirstNameLengthOne"))
    #suite.addTest(TC6_EmailBlank("test_TC6_EmailBlank"))
    #suite.addTest(TC7_EmailInvalid("test_TC7_EmailInvalid"))
    #suite.addTest(TC8_PhoneLengthZero("test_TC8_PhoneLengthZero"))
    #suite.addTest(TC9_PhoneLengthNine("test_TC9_PhoneLengthNine"))
    #suite.addTest(TC10_PhoneLengthEleven("test_TC10_PhoneLengthEleven"))
    #suite.addTest(TC11_PhoneInvalid("test_TC11_PhoneInvalid"))
    #suite.addTest(TC12_ValidateState("test_TC12_ValidateState"))
    suite.addTest(TC13_ValidateAllFiedls("test_TC13_ValidateAllFields"))
    return suite