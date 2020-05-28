import pyodbc as mc
cnx=mc.connect('Driver={SQL Server};Server=localhost;Database=master')
cur=cnx.cursor()

class custview:
 def view_customer(self):
                cur.execute("select * from customer_1637249")
                a=cur.fetchall()
                for i in a:
                        print(i,"\n")


b=custview()
