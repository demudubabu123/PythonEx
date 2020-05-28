import pyodbc as mc
cnx=mc.connect('Driver={SQL Server};Server=localhost;Database=master')
cur=cnx.cursor()
class add:
    def insert_customer(self):
                name=input("enter cust name:")
                cust_id=input("enter cust_id:")




               # payment_status=raw_input("enter payment status:")
                k=0
                contact=int(input("enter phone number:"))
                cur.execute("insert into customer(custid,name,contact_details) values(?,?,?)",(cust_id,name,contact))
                cur.execute("insert into customer2(customer_name,customer_id)values(?,?)", name, cust_id,)

                cnx.commit()
                print("\ncustomer details inserted successfully")



a=add()


