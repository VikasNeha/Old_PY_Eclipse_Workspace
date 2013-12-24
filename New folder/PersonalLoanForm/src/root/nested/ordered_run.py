'''
Created on May 21, 2013

@author: Vikas
'''
import unittest
from root.nested import test_TC1_ApplicationRejects1, test_TC2_ApplicationRejectsState1, test_TC3_ValidatePersonalDetails,\
    test_TC4_AppRejectsMainSourceIncome, test_TC5_AppRedirectsPioneerMilitary,\
    test_TC6_AppMonthlyIncomeShowsWarning, test_TC7_AppRejectsBankAccount,\
    test_TC8_AppRejectsDirectDeposit, test_TC9_NextPayDateCalculations,\
    test_TC10_EmployerValidations, test_TC11_BankValidations

def suite():
    suite1 = test_TC1_ApplicationRejects1.suite()
    suite2 = test_TC2_ApplicationRejectsState1.suite()
    suite3 = test_TC3_ValidatePersonalDetails.suite()
    suite4 = test_TC4_AppRejectsMainSourceIncome.suite()
    suite5 = test_TC5_AppRedirectsPioneerMilitary.suite()
    suite6 = test_TC6_AppMonthlyIncomeShowsWarning.suite()
    suite7 = test_TC7_AppRejectsBankAccount.suite()
    suite8 = test_TC8_AppRejectsDirectDeposit.suite()
    suite9 = test_TC9_NextPayDateCalculations.suite()
    suite10 = test_TC10_EmployerValidations.suite()
    suite11 = test_TC11_BankValidations.suite()
    
    fullSuite = unittest.TestSuite()
    fullSuite.addTest(suite1)
    #fullSuite.addTest(suite2)
    #fullSuite.addTest(suite3)
    #fullSuite.addTest(suite4)
    #fullSuite.addTest(suite5)
    #fullSuite.addTest(suite6)
    #fullSuite.addTest(suite7)
    #fullSuite.addTest(suite8)
    #fullSuite.addTest(suite9)
    #fullSuite.addTest(suite10)
    #fullSuite.addTest(suite11)
    return fullSuite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run (test_suite)