import pyodbc as mc

cnx = mc.connect("Driver={SQL Server};"
                 "Server=DESKTOP-SFPRKLP\SQLEXPRESS;"
                 "Database=postpaid;"
                 )
cur = cnx.cursor()


class viewplans:
    def view_plans(self):
        cur.execute("select * from plans")
        a = cur.fetchall()

        for i in a:
            print(i, "\n")


d = viewplans()
