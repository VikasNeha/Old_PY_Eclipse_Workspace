'''
Created on 15-Jul-2013
@author: Neha-Vikas
'''
import pyodbc
from Userdata import classUserdata

def getUserdataFromDatabase():
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=neha-vikas-vaio;DATABASE=sample;UID=sa;PWD=lord@krishna')
    cursor = cnxn.cursor()
    
    cursor.execute("select * from Userdata")
    row = cursor.fetchone()
    userData = classUserdata(row.Company_Name, row.Country, row.State, row.Federal_Tax_ID, 
                 row.Address1, row.Address2, row.Address3, row.City, row.Postal_Code, 
                 row.Phone_AreaCode, row.Phone_Number, row.Fax_AreaCode , row.Fax_Number,
                 row.Contact_Name, row.Title, row.Contact_Email,
                 row.Contact_Phone_AreaCode, row.Contact_Phone_Number, row.Contact_Fax_AreaCode, row.Contact_Fax_Number,
                 row.Gmail_Username, row.Gmail_Password)
    return userData

def updateUserdataActivationStatus(userData, activationStatus):
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=neha-vikas-vaio;DATABASE=sample;UID=sa;PWD=lord@krishna')
    cursor = cnxn.cursor()
    
    cursor.execute("UPDATE UserData SET [Activation_Status] = ? WHERE Contact_Email = ?", activationStatus, userData.Contact_Email)
    print cursor.rowcount, 'users updated'
    cnxn.commit()