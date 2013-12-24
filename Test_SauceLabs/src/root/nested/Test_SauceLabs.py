'''
Created on May 21, 2013

@author: Vikas
'''
import unittest
import base64
import json
import httplib
import sys
from selenium import webdriver

config = {"username": "vikas_ojha",
          "access-key": "ba3aa6cb-162f-4aaf-b68d-f35cfd524204"}

class Selenium2OnSauce(unittest.TestCase):

    def setUp(self):
        desired_capabilities = webdriver.DesiredCapabilities.IPHONE
        desired_capabilities['version'] = '5.0'
        desired_capabilities['platform'] = 'MAC'
        desired_capabilities['name'] = 'Testing Selenium 2 in Python at Sauce'

        self.driver = webdriver.Remote(
            desired_capabilities=desired_capabilities,
            command_executor="http://vikas_ojha:ba3aa6cb-162f-4aaf-b68d-f35cfd524204@ondemand.saucelabs.com:80/wd/hub"
        )
        self.driver.implicitly_wait(30)

    def test_sauce(self):
        self.driver.get('http://saucelabs.com/test/guinea-pig')
        self.assertTrue("I am a page title - Sauce Labs" in self.driver.title)
        comments = self.driver.find_element_by_id('comments')
        comments.send_keys('Hello! I am some example comments.'
                           ' I should be in the page after submitting the form')
        self.driver.find_element_by_id('submit').click()

        commented = self.driver.find_element_by_id('your_comments')
        self.assertTrue('Your comments: Hello! I am some example comments.'
                        ' I should be in the page after submitting the form'
                        in commented.text)
        body = self.driver.find_element_by_xpath('//body')
        self.assertFalse('I am some other page content' in body.text)
        self.driver.find_elements_by_link_text('i am a link')[0].click()
        body = self.driver.find_element_by_xpath('//body')
        self.assertTrue('I am some other page content' in body.text)
        
    def report_pass_fail(self):
        base64string = base64.encodestring('%s:%s' % (config['username'],
                                                      config['access-key']))[:-1]
        result = json.dumps({'public':'true','passed': sys.exc_info() == (None, None, None)})
        connection = httplib.HTTPConnection("saucelabs.com")
        connection.request('PUT', '/rest/v1/%s/jobs/%s' % (config['username'],
                                                           self.driver.session_id),
                           result,
                           headers={"Authorization": "Basic %s" % base64string})
        result = connection.getresponse()
        return result.status == 200

    def tearDown(self):
        print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
        self.report_pass_fail()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()