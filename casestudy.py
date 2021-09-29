class employee:
    empname=""
    empid=0
    empsal=0
    empdept=""
    def __init__(self,empname,empid,empsal,empdept):
        self.empname=empname
        self.empid=empid
        self.empsal=empsal
        self.empdept=empdept
    def display(self):
        print(self.empname)
        print(self.empid)
        print(self.empsal)
        print(self.empdept)
class timesheet(employee):
    def __init__(self,date,hours,activity,description,status):
        self.date=date
        self.hours=hours
        self.activity=activity
        self.description=description
        self.status=status
    def display(self):
        print("date:",self.date)
        print("hours:",self.hours)
        print("Activity:",self.activity)
        print("description:",self.description)
        print("status:",self.status)
emp=employee("nithin","20871","20000","analyst")
emp.display()
time_sheet=timesheet("29-09-2021","8","Training","python training","Approved")
time_sheet.display()

