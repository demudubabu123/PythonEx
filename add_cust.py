import pyodbc as mc

cnx = mc.connect("Driver={SQL Server};"
                 "Server=DESKTOP-SFPRKLP\SQLEXPRESS;"
                 "Database=postpaid;"
                 )
cur = cnx.cursor()


class add:
    def insert_customer(self):
        name = input("enter customer name(max 10 letters):")
        if len(name)!=10:
          print("entered customer name is not in the above given order,please enter in the above given format")
        cust_id = input("enter customer_id(it should be 6 letters starting with 'cu'':").lower()
        if len(cust_id)!=6 or cust_id[0]!='c' or cust_id[1]!='u':
          print("entered customer_id is not in the above given order,please enter in the above given format")
        cur.execute("select customer_id from customer2")
        a = cur.fetchall()
        for i in a:
            if i != ' ':
                if a != cust_id:
                    print("entered customer_id is already in the list,please enter another customer_id")
                    break
        k = 0
        contact = int(input("enter phone number:"))
        cur.execute("insert into customer(custid,name,contact_details) values(?,?,?)", (cust_id, name, contact))
        cur.execute("insert into customer2(customer_name,customer_id)values(?,?)", name, cust_id, )
        cnx.commit()
        print("\ncustomer details inserted successfully")


a = add()
