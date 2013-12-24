'''
Created on May 21, 2013

@author: Vikas
'''
import unittest
from root.nested import test_TC1_ValidatePersonalDetails

def suite():
    suite1 = test_TC1_ValidatePersonalDetails.suite()
    
    fullSuite = unittest.TestSuite()
    fullSuite.addTest(suite1)
    return fullSuite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run (test_suite)