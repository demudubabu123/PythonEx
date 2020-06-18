import pyodbc as mc
cnx = mc.connect("Driver={SQL Server};"
                 "Server=DESKTOP-SFPRKLP\SQLEXPRESS;"
                 "Database=postpaid;"
                 )
cur=cnx.cursor()
class update_stat:
    def update_status(self):
        idd=input("Enter Customer ID:")
        cur.execute("select custid from customer")
        a = cur.fetchall()
        b = []
        for i in range(len(a)):
            b.append(a[i][i-i])
        for i in b:
            if i==idd:
             break
        else:
         print("entered customer_id is not in the list,please enter another customer_id or create new account by adding account details")
        cur.execute("select * from plans")
        print("plan details","========", sep="\n")
        a=cur.fetchall()
        for i in a:
         print("\n")
         for j in i:
          print(j,end="|")
        print("\n")
        cur.execute("select rem_balance from customer2 where customer_id=?",idd)
        a=cur.fetchall()
        b=a[0][0]
        l=0
        cur.execute("update customer2 set prev_balance=? where customer_id=?",(b,idd))
        cur.execute("update customer2 set rem_balance=? where customer_id=?",(l,idd))
        a='paid'
        b='unpaid'
        if b!=0:
         cur.execute("update customer2 set status=? where customer_id=?",(b,idd))
        else:
         cur.execute("update customer2 set status=? where customer_id=?", (a,idd))
        print("customer details", "============", sep="\n")
        cur.execute("select * from customer2 where customer_id=?", idd)
        f = cur.fetchall()
        for i in f:
            for j in i:
                print(j, end="|")
        print("\n")

        amount = float(input("enter the amount you want to recharge by choosing the correct plan which is mentioned above:"))
        cur.execute("select plan_amount from plans")
        k=cur.fetchall()

        b=[]
        for i in range(len(k)):
          q=float(k[i][i-i])
          b.append(q)
        for i in b:
          if i==amount:
            break
        else:
          print("entered amount is not in the given plan,please enter another plan")

        cur.execute("update customer2 set bill_amount=(?) where customer_id=(?)",(amount,idd))
        cur.execute("select planid from plans where plan_amount=?", amount)
        y= cur.fetchall()

        q = y[0][0]

        cur.execute("update customer2 set plan_id=(?) where customer_id=(?)",(q,idd))
        cur.execute("select bill_amount from customer2 where customer_id=?",idd)
        c=cur.fetchall()
        cur.execute("select plan_id from customer2 where customer_id=?",idd)
        l=cur.fetchall()
        b=l[0][0]

        cur.execute("select plan_amount from plans where planid=?",b)
        g=cur.fetchall()

        try:
         a=float(input("how much you want to pay:"))
        except:
          print("please enter correct values or you might entering alphabets")
        cur.execute("select rem_balance from customer2 where customer_id=?",idd)
        b=cur.fetchall()
        cur.execute("select prev_balance from customer2 where customer_id=?",idd)
        z=cur.fetchall()
        a=float(a)
        g[0][0]=float(g[0][0])
        z[0][0]=float(z[0][0])
        if a>g[0][0]:
         if z[0][0]>0:
          b=input("you are paying extra money,do u want to pay the previous balance also(yes/no):")
          if b=='yes':
            cur.execute("select prev_balance from customer2 where customer_id=?",idd)
            o=cur.fetchall()
            e=o[0][0]
            print("your previous balance is{0}".format(e))
            rem=g[0][0]-a
            l='paid'
            j='unpaid'
            if rem==z[0][0]:
              k=rem-z[0][0]
              print("your balance is totally cleared")
              cur.execute("update customer2 set status=(?) where customer_id=(?)",(l,idd))
              cur.execute("update customer2 set rem_balance=(?) where customer_id=(?)",(k,idd))
              cnx.commit()
            elif rem>z[0][0]:
              k=rem-z[0][0]
              print("your balance is not yet cleared")
              cur.execute("update customer2 set status=(?) where customer_id=(?)", (j, idd))
              cur.execute("update customer2 set rem_balance=(?) where customer_id=(?)", (k, idd))
              cnx.commit()
            else:
             k=z[0][0]-rem
             print("your balance is not yet cleared")
             cur.execute("update customer2 set status=(?) where customer_id=(?)", (j, idd))
             cur.execute("update customer2 set rem_balance=(?) where customer_id=(?)", (k, idd))
             cnx.commit()
         else:
          print("you are paying extra money,no need to pay as your previous balance is zero")
        else:
         r=input("do u want to pay the previous balance(yes/no):")
         cur.execute("select prev_balance from customer2 where customer_id=(?)",idd)
         h=cur.fetchall()
         print(h[0][0])
         l='paid'
         k='unpaid'
         if r=="yes":
          z[0][0]=float(z[0][0])
          a=float(a)
          g[0][0]=float(g[0][0])
          if a>z[0][0]:
           rem=g[0][0]-(a-z[0][0])
           cur.execute("update customer2 set status=(?) where customer_id=(?)", (l, idd))
           cur.execute("update customer2 set rem_balance=(?) where customer_id=(?)", (rem, idd))

           cnx.commit()
           print("your insertion is successful")
          else:
            rem = g[0][0]-(z[0][0]-a)
            cur.execute("update customer2 set status=(?) where customer_id=(?)", (l, idd))
            cur.execute("update customer2 set rem_balance=(?)where customer_id=(?)", (rem, idd))
            cnx.commit()
            print("your insertion is successful")
         else:
          rem=g[0][0]-a
          total=rem+z[0][0]
          cur.execute("update customer2 set status=(?) where customer_id=(?)", (k, idd))
          cur.execute("update customer2 set rem_balance=(?) where customer_id=(?)", (total, idd))
          cnx.commit()
          print("your insertion is successful")
    cnx.commit()







c=update_stat()
