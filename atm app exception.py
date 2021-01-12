from pip._vendor.distlib.compat import raw_input
class  LimitExceedException(Exception):
   def __init__(self, arg):
       self.msg=arg
class  InvalidMinimumException(Exception):
    def __init__(self, arg):
        self.msg = arg
class   InsufficientFundException(Exception):
    def __init__(self, arg):
        self.msg = arg
ans=True
while ans:
    print ("""
    1.withdraw
    2.deposit
    """)

    ans=raw_input("choose option : ")
    if ans=="1":
        amount = int(input("Enter amount:"))
        if amount > 10000:
            raise LimitExceedException("your enter exceed amount")
        if amount < 100:
            raise InvalidMinimumException("your enter low(invalid) amount")
        balance = 1000
        if amount < balance:
            raise InsufficientFundException("you have insufficient fund")


        else:
            print("your withdraw amount:", amount)
    elif ans=="2":
        amount = int(input("Enter amount:"))
        print("your deposited amount:", amount)
