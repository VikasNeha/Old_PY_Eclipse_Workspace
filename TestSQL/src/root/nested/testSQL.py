'''
Created on 15-Jul-2013

@author: Neha-Vikas
'''
import pyodbc

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=neha-vikas-vaio;DATABASE=sample;UID=sa;PWD=lord@krishna')
cursor = cnxn.cursor()

cursor.execute("select * from Credentials")
row = cursor.fetchone()
if row:
    print 'user:', row[0]          # access by column index
    print 'password:', row[1]   # or access by name