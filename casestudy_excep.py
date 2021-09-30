from exception import *
def time(hours):
    if hours<40:
        raise Timesheet("less tha 40 hours")
    else:
        print("submit the timesheet")
try:
    time(20)
except(Timesheet):
    print("message")
time(40)