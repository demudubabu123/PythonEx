from add_cust import add, a
from update import update_stat, c
from viewplans import viewplans, d
from planewise import plan_wise, e
import pyodbc as mc
cnx = mc.connect("Driver={SQL Server};"
                 "Server=DESKTOP-SFPRKLP\SQLEXPRESS;"
                 "Database=postpaid;"
                 )
cur = cnx.cursor()


class db_functions:
    c = 0

    def __init__(self):
        pass

    def insertcustomer(self):
        a.insert_customer()

    def updatestatus(self):
        c.update_status()

    def viewplans(self):
        d.view_plans()

    def planwise(self):
        e.planwise()


db = db_functions()
print("welcome to the postpaid bill", "what do u want to know", sep="\n")
print("1:account_details", "2:view_plans", "3:recharge and update_status", sep="\n")
z = int(input("enter the number:"))
if z == 1:
    db.insertcustomer()
    x = input("do u want to continue to go furthur(yes/no):")
    if x == "yes":
        print("plans")
        db.viewplans()
        w = input("further you want to proceed(yes/no):")
        if w == "yes":
            print("updating the customer_details")
            db.updatestatus()
elif z == 2:
    db.viewplans()
    a = input("furthur you want to go to update(yes/no):").lower()
    if a == 'yes':
        db.updatestatus()
elif z == 3:
    db.updatestatus()
elif z == ' ' or z != 1 or z != 2 or z != 3:
    print("entered number is not in the above mentioned number,please enter another number")

# db.insertcustomer()
# db.viewcustomer()
# db.updatestatus()
