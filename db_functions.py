from add_cust import add,a
from custview import custview,b
from update import update_stat,c
from viewplans import viewplans,d
from planewise import plan_wise,e
import pyodbc as mc
cnx=mc.connect('Driver={SQL Server};Server=localhost;Database=master')
cur=cnx.cursor()

class dbfunctions:
    c=0
    def __init__(self):
        pass
    def insertcustomer(self):
        a.insert_customer()

        '''name=raw_input("enter cust name:")
        cust_id=input("enter cust_id:")
        plan=input("enter plan_id:")
        amount=input("enter emount:")
        payment_status=raw_input("enter payment status:")
        contact=input("enter ph_number:")
        cur.execute("insert into customer_1637249 values(%s,%s,%s,%s,%s,%s)",(cust_id,name,plan,amount,payment_status,contact))
        cnx.commit()
        print "\ncustomer details inserted successfully"'''
    def viewcustomer(self):
        b.view_customer()
        '''cur.execute("select * from customer_1637249")
        a=cur.fetchall()
        for i in a:
            
            print i'''
    def updatestatus(self):
        c.update_status()

        '''idd=input("Enter Customer ID:")
        status=raw_input("payment status?")
        cur.execute("update customer_1637249 set payment_status=%s where custid=%s",(status,idd))
        cnx.commit()
        print "Status updated successfully"'''
    def viewplans(self):
        d.view_plans()
    def planwise(self):
        e.planwise()

db=dbfunctions()
print("welcome to the postpaid bill","what do u want to know",sep="\n")
print("1:account_details","2:view_plans","3:recharge and update_status",sep="\n")
z=int(input("enter the number:"))
if z==1:
 db.insertcustomer()
 x=input("do u want to continue to go furthur(yes/no):")
 if x=="yes":
  print("plans")
  db.viewplans()
  w=input("further you want to proceed(yes/no):")
  if w=="yes":
   print("updating the customer_details")
   db.updatestatus()
elif z==2:
 db.viewplans()
 a=input("furthur you want to go to update(yes/no):").lower()
 if a=='yes':
    db.updatestatus()
elif z==3:
 db.updatestatus()
elif z==' ' or z!=1 or z!=2 or z!=3:
 print("entered number is not in the above mentioned number,please enter another number")

#db.insertcustomer()
#db.viewcustomer()
#db.updatestatus()
