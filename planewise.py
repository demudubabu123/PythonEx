import pyodbc as mc

cnx = mc.connect("Driver={SQL Server};"
                 "Server=DESKTOP-SFPRKLP\SQLEXPRESS;"
                 "Database=postpaid;"
                 )
cur = cnx.cursor()


class plan_wise:
    def planwise(self):
        cur.execute("select p.plan_id,p.plan_name,p.plan_amount,c.custid,c.name from customer_1637249 c,plan_1637249 "
                    "p where p.plan_id=c.plans")
        a = cur.fetchall()

        for i in a:
            print(i, "\n")


e = plan_wise()
