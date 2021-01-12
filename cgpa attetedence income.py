class attendanceshortageexception(Exception):
   def __init__(self, arg):
       self.msg=arg
class incomeexception(Exception):
   def __init__(self, arg):
       self.msg=arg
class gpaexception(Exception):
   def __init__(self, arg):
       self.msg=arg
gpa = int(input("Enter cgpa:"))
if gpa<7:
   raise gpaexception("your cgpa is less than 7")

attendance = int(input("enter your attendance:"))
if attendance<75:
   raise attendanceshortageexception("your attendence is below 75")

income = int(input("enter your income:"))
if income>500000:
   raise attendanceshortageexception("your parents income is higher than 500000")

else:
   print( "CGPA:", gpa, "Attendance:", attendance,  "Parents Income:", income)