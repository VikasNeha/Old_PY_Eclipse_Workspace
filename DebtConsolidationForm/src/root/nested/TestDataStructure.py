'''
Created on May 22, 2013

@author: Vikas
'''
def setUpTestDataForTC1(debt_amount, first_name, last_name, email, phone, state):
    testData = TestDataStructure()
    testData.debt_amount = debt_amount
    testData.first_name = first_name
    testData.last_name = last_name
    testData.email = email
    testData.phone = phone
    testData.state = state        
    return testData

class TestDataStructure(object):
    pass