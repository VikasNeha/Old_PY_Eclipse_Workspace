'''
Created on May 21, 2013

@author: Vikas
'''
import unittest
from selenium.common.exceptions import TimeoutException

from root.nested import Utilities, FormFunctions, TestDataStructure,\
    PersonalLoanFormSuper

class test_ApplicationRejectsState1(unittest.TestCase):
    def setUp(self):
        PersonalLoanFormSuper.setUp(self, "Personal Loan Form: TC2: Testing app rejection because of States AZ, AR, GA, MD, PA, VA, WV")
        
    def tearDown(self):
        PersonalLoanFormSuper.tearDownAndQuit(self)    
    
    def test_ApplicationRejectsState1(self):
        states = ['Arizona', 'Arkansas', 'Georgia', 'Maryland', 'Pennsylvania', 'Virginia', 'West Virginia']
        errMsg = "Test Case failed for states: "
        failCount = 0
        for currentState in states:
            driver = self.driver
            Utilities.openURL(driver, self.appURL)
            testData = TestDataStructure.setUpTestDataForTC2(currentState)        
            
            #Click Apply Here
            FormFunctions.clickApplyHere(driver)
            FormFunctions.assertTextInFormArea(driver, "Select your residence state", "Apply Here")
            
            #Select State
            FormFunctions.selectState(driver, testData.home_state)
            
            #Assert Final Result
            try:
                FormFunctions.assertFinalResultRejected(driver)
            except TimeoutException:
                failCount = failCount + 1
                errMsg = errMsg + currentState + ", "
            
        if failCount > 0:
            self.failMsg = errMsg
            raise AssertionError(errMsg)
    
    
'''            
if __name__ == "__main__":
    unittest.main(verbosity=2)'''

def suite():
    suite = unittest.TestSuite()
    suite.addTest(test_ApplicationRejectsState1("test_ApplicationRejectsState1"))
    return suite