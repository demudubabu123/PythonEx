import pyodbc

driver = 'SQL Server'
server = 'DESKTOP-SFPRKLP\SQLEXPRESS'
db1 = 'postpaid'

cnxn = pyodbc.connect(driver='{SQL Server}', host=server, database=db1)
cursor = cnxn.cursor()

# cnxn = pyodbc.connect(driver='{SQL Server}', host=server, database=db1,
#                       trusted_connection=tcon, user=uname, password=pword)
