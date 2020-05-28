from db_functions import dbfunctions

class choice:
    def __init__(self, post):
        self.postpaid = post
        self.dictt = {1: self.addcustomer,
                      2: self.viewcustomer, 3: self.updatestatus, 4: self.viewplanss, 5: self.planswise}

    def addcustomer(self):
        self.postpaid.insertcustomer()

    def viewcustomer(self):

        self.postpaid.viewcustomer()


    def updatestatus(self):
        self.postpaid.updatestatus()


    def viewplanss(self):
        self.postpaid.viewplans()


    def planswise(self):
        self.postpaid.planwise()







