'''
Created on May 21, 2013

@author: Vikas
'''
import base64
import json
import httplib
import sys
from selenium import webdriver
import pyodbc

config = {"username": "vikas_ojha",
          "access-key": "ba3aa6cb-162f-4aaf-b68d-f35cfd524204"}

def setUp(self, testName):
    
    desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
    desired_capabilities['platform'] = "Windows 7"
    desired_capabilities['version'] = "21"
    desired_capabilities['name'] = testName

    self.driver = webdriver.Remote(
        desired_capabilities=desired_capabilities,
        command_executor="http://vikas_ojha:ba3aa6cb-162f-4aaf-b68d-f35cfd524204@ondemand.saucelabs.com:80/wd/hub"
    )
    
    #self.driver = webdriver.Firefox()
    self.driver.implicitly_wait(30)
            
    self.appURL = "https://www.debtconsolidation.com/?test=true"
    self.failMsg = ""
        
def tearDown(self):
    print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
    report_pass_fail(self)
    self.driver.quit()
    
def report_pass_fail(self):
    base64string = base64.encodestring('%s:%s' % (config['username'],
                                                  config['access-key']))[:-1]
    result = json.dumps({'public':'true','passed': sys.exc_info() == (None, None, None),"custom-data": {"FailReason":self.failMsg}})
    connection = httplib.HTTPConnection("saucelabs.com")
    connection.request('PUT', '/rest/v1/%s/jobs/%s' % (config['username'],
                                                       self.driver.session_id),
                       result,
                       headers={"Authorization": "Basic %s" % base64string})
    result = connection.getresponse()
    return result.status == 200