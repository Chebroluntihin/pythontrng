class Timesheet(Exception):
    def __init__(self,message):
        self.message=message
        print(message)
        print("you cannot submit")