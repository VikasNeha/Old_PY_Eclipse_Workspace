'''
Created on May 22, 2013

@author: Vikas
'''
def setUpTestDataForTC1(home_state, 
                 loan_amount, 
                 name_first, name_last, email_primary, phone_home, home_zip, terms, 
                 income_source, 
                 home_street, home_city, 
                 military, 
                 income_monthly_net, 
                 bank_account_type, 
                 direct_deposit, 
                 income_frequency, 
                 employer_name, phone_work, employment_length, 
                 bank_name, bank_aba, bank_account, state_issued_id, state_id_number, 
                 dob_m, dob_d, dob_y, ssn_area, ssn_group, ssn_serial):
    testData = TestDataStructure()
    testData.home_state = home_state
    testData.loan_amount = loan_amount
    testData.name_first = name_first
    testData.name_last = name_last
    testData.email_primary = email_primary
    testData.phone_home = phone_home
    testData.home_zip = home_zip
    testData.terms = terms
    testData.income_source = income_source
    testData.home_street = home_street
    testData.home_city = home_city
    testData.military = military
    testData.income_monthly_net = income_monthly_net
    testData.bank_account_type = bank_account_type
    testData.direct_deposit = direct_deposit
    testData.income_frequency = income_frequency
    testData.employer_name = employer_name
    testData.phone_work = phone_work
    testData.employment_length = employment_length
    testData.bank_name = bank_name
    testData.bank_aba = bank_aba
    testData.bank_account = bank_account
    testData.state_issued_id = state_issued_id
    testData.state_id_number = state_id_number
    testData.dob_m = dob_m
    testData.dob_d = dob_d
    testData.dob_y = dob_y
    testData.ssn_area = ssn_area
    testData.ssn_group = ssn_group
    testData.ssn_serial = ssn_serial
    
    return testData

def setUpTestDataForTC2(home_state):
    testData = TestDataStructure()
    testData.home_state = home_state
    return testData

def setUpTestDataForTC3_TC1(home_state, loan_amount, name_first, name_last, email_primary, phone_home, home_zip, terms):
    testData = TestDataStructure()
    testData.home_state = home_state
    testData.loan_amount = loan_amount
    testData.name_first = name_first
    testData.name_last = name_last
    testData.email_primary = email_primary
    testData.phone_home = phone_home
    testData.home_zip = home_zip
    testData.terms = terms
    return testData

def setUpTestDataForTC4(home_state, loan_amount, name_first, name_last, email_primary, phone_home, home_zip, terms, income_source):
    testData = TestDataStructure()
    testData.home_state = home_state
    testData.loan_amount = loan_amount
    testData.name_first = name_first
    testData.name_last = name_last
    testData.email_primary = email_primary
    testData.phone_home = phone_home
    testData.home_zip = home_zip
    testData.terms = terms
    testData.income_source = income_source
    return testData

def setUpTestDataForTC5(home_state, loan_amount, 
                        name_first, name_last, email_primary, 
                        phone_home, home_zip, terms, 
                        income_source, 
                        home_street, home_city):
    testData = TestDataStructure()
    testData.home_state = home_state
    testData.loan_amount = loan_amount
    testData.name_first = name_first
    testData.name_last = name_last
    testData.email_primary = email_primary
    testData.phone_home = phone_home
    testData.home_zip = home_zip
    testData.terms = terms
    testData.income_source = income_source
    testData.home_street = home_street
    testData.home_city = home_city
    return testData

def setUpTestDataForTC6(home_state, loan_amount, 
                        name_first, name_last, email_primary, 
                        phone_home, home_zip, terms, 
                        income_source, 
                        home_street, home_city, military):
    testData = TestDataStructure()
    testData.home_state = home_state
    testData.loan_amount = loan_amount
    testData.name_first = name_first
    testData.name_last = name_last
    testData.email_primary = email_primary
    testData.phone_home = phone_home
    testData.home_zip = home_zip
    testData.terms = terms
    testData.income_source = income_source
    testData.home_street = home_street
    testData.home_city = home_city
    testData.military = military
    return testData

def setUpTestDataForTC7(home_state, loan_amount, 
                        name_first, name_last, email_primary, 
                        phone_home, home_zip, terms, 
                        income_source, 
                        home_street, home_city, military, income_monthly_net):
    testData = TestDataStructure()
    testData.home_state = home_state
    testData.loan_amount = loan_amount
    testData.name_first = name_first
    testData.name_last = name_last
    testData.email_primary = email_primary
    testData.phone_home = phone_home
    testData.home_zip = home_zip
    testData.terms = terms
    testData.income_source = income_source
    testData.home_street = home_street
    testData.home_city = home_city
    testData.military = military
    testData.income_monthly_net = income_monthly_net
    return testData

def setUpTestDataForTC8(home_state, loan_amount, 
                        name_first, name_last, email_primary, 
                        phone_home, home_zip, terms, 
                        income_source, 
                        home_street, home_city, military, income_monthly_net,
                        bank_account_type):
    testData = TestDataStructure()
    testData.home_state = home_state
    testData.loan_amount = loan_amount
    testData.name_first = name_first
    testData.name_last = name_last
    testData.email_primary = email_primary
    testData.phone_home = phone_home
    testData.home_zip = home_zip
    testData.terms = terms
    testData.income_source = income_source
    testData.home_street = home_street
    testData.home_city = home_city
    testData.military = military
    testData.income_monthly_net = income_monthly_net
    testData.bank_account_type = bank_account_type
    return testData

def setUpTestDataForTC9(home_state, loan_amount, 
                        name_first, name_last, email_primary, 
                        phone_home, home_zip, terms, 
                        income_source, 
                        home_street, home_city, military, income_monthly_net,
                        bank_account_type, direct_deposit):
    testData = TestDataStructure()
    testData.home_state = home_state
    testData.loan_amount = loan_amount
    testData.name_first = name_first
    testData.name_last = name_last
    testData.email_primary = email_primary
    testData.phone_home = phone_home
    testData.home_zip = home_zip
    testData.terms = terms
    testData.income_source = income_source
    testData.home_street = home_street
    testData.home_city = home_city
    testData.military = military
    testData.income_monthly_net = income_monthly_net
    testData.bank_account_type = bank_account_type
    testData.direct_deposit = direct_deposit
    return testData

def setUpTestDataForTC10(home_state, loan_amount, 
                        name_first, name_last, email_primary, 
                        phone_home, home_zip, terms, 
                        income_source, 
                        home_street, home_city, military, income_monthly_net,
                        bank_account_type, direct_deposit, income_frequency,
                        employer_name, phone_work, employment_length):
    testData = TestDataStructure()
    testData.home_state = home_state
    testData.loan_amount = loan_amount
    testData.name_first = name_first
    testData.name_last = name_last
    testData.email_primary = email_primary
    testData.phone_home = phone_home
    testData.home_zip = home_zip
    testData.terms = terms
    testData.income_source = income_source
    testData.home_street = home_street
    testData.home_city = home_city
    testData.military = military
    testData.income_monthly_net = income_monthly_net
    testData.bank_account_type = bank_account_type
    testData.direct_deposit = direct_deposit
    testData.income_frequency = income_frequency
    testData.employer_name = employer_name
    testData.phone_work = phone_work
    testData.employment_length = employment_length
    return testData

def setUpTestDataForTC11(home_state, loan_amount, 
                        name_first, name_last, email_primary, 
                        phone_home, home_zip, terms, 
                        income_source, 
                        home_street, home_city, military, income_monthly_net,
                        bank_account_type, direct_deposit, income_frequency,
                        employer_name, phone_work, employment_length,
                        bank_name, bank_aba, bank_account):
    testData = TestDataStructure()
    testData.home_state = home_state
    testData.loan_amount = loan_amount
    testData.name_first = name_first
    testData.name_last = name_last
    testData.email_primary = email_primary
    testData.phone_home = phone_home
    testData.home_zip = home_zip
    testData.terms = terms
    testData.income_source = income_source
    testData.home_street = home_street
    testData.home_city = home_city
    testData.military = military
    testData.income_monthly_net = income_monthly_net
    testData.bank_account_type = bank_account_type
    testData.direct_deposit = direct_deposit
    testData.income_frequency = income_frequency
    testData.employer_name = employer_name
    testData.phone_work = phone_work
    testData.employment_length = employment_length
    testData.bank_name = bank_name
    testData.bank_aba = bank_aba
    testData.bank_account = bank_account
    return testData

class TestDataStructure(object):
    pass
    """
    def __init__(self, home_state, 
                 loan_amount, 
                 name_first, name_last, email_primary, phone_home, home_zip, terms, 
                 income_source, 
                 home_street, home_city, 
                 military, 
                 income_monthly_net, 
                 bank_account_type, 
                 direct_deposit, 
                 income_frequency, 
                 employer_name, phone_work, employment_length, 
                 bank_name, bank_aba, bank_account, state_issued_id, state_id_number, 
                 dob_m, dob_d, dob_y, ssn_area, ssn_group, ssn_serial):
        self.home_state = home_state
        self.loan_amount = loan_amount
        self.name_first = name_first
        self.name_last = name_last
        self.email_primary = email_primary
        self.phone_home = phone_home
        self.home_zip = home_zip
        self.terms = terms
        self.income_source = income_source
        self.home_street = home_street
        self.home_city = home_city
        self.military = military
        self.income_monthly_net = income_monthly_net
        self.bank_account_type = bank_account_type
        self.direct_deposit = direct_deposit
        self.income_frequency = income_frequency
        self.employer_name = employer_name
        self.phone_work = phone_work
        self.employment_length = employment_length
        self.bank_name = bank_name
        self.bank_aba = bank_aba
        self.bank_account = bank_account
        self.state_issued_id = state_issued_id
        self.state_id_number = state_id_number
        self.dob_m = dob_m
        self.dob_d = dob_d
        self.dob_y = dob_y
        self.ssn_area = ssn_area
        self.ssn_group = ssn_group
        self.ssn_serial = ssn_serial
        """