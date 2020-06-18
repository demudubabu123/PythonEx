import pyodbc as mc

cnx = mc.connect("Driver={SQL Server};"
                 "Server=DESKTOP-SFPRKLP\SQLEXPRESS;"
                 "Database=postpaid;"
                 )
cur = cnx.cursor()


class add:
    def insert_customer(self):
        name = input("enter customer name(max 10 letters):")
        cust_id = input("enter customer_id(it should be 6 letters starting with 'cu'):")
        contact = int(input("enter the phone number:"))
        cur.execute("select custid from customer")
        f = cur.fetchall()
        l = []
        for i in range(len(f)):
            l.append(f[i][i-1])
        k = str(contact)
        z = cur.fetchall()
        for i in l:
            if len(name) > 10 or len(cust_id) != 6 or cust_id[0] != 'c' or cust_id[1] != 'u' or i == cust_id or len(k) != 10:
                print("you did not follow the above restrictions")
                break
        else:
            cur.execute("insert into customer(custid,name,contact_details) values(?,?,?)", (cust_id, name, contact))
            cur.execute("insert into customer2(customer_name,customer_id)values(?,?)", name, cust_id, )
            cnx.commit()
            print("\ncustomer details inserted successfully")


a = add()
