'''
Created on May 21, 2013

@author: Vikas
'''
import unittest, sys
from selenium import webdriver
# from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta


class PythonOrgSearch(unittest.TestCase):
    
    def setUp(self):
        #self.driver = webdriver.Firefox()
        pass
        
    def test_search_in_python_org(self):
        
        nextPayDate1 = datetime.strptime('05/28/2013', '%m/%d/%Y')
        nextPayDate2Actual = datetime.strptime('06/04/2013', '%m/%d/%Y')
        td = timedelta(days=30)
        nextPayDate2Expected = nextPayDate1.replace(month=nextPayDate1.month+1)
        
        print nextPayDate2Expected
        sys.exit(0)
        
        
        
        driver = self.driver
        driver.get("http://www.google.com")
        inputElement = driver.find_element_by_name("q")
        inputElement.send_keys("Cheese!")
        inputElement.submit()
        print driver.title
        
        try:
            WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))
            print driver.title
        finally:
            print driver.title
        
    def tearDown(self):
        #self.driver.close()
        pass
            
if __name__ == "__main__":
    unittest.main()