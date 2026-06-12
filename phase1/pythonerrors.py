# try expect finally
try:
    num=int(input("Enter the number"))
    print(10/num)
except ZeroDivisionError:
    print("can't be divide by zero")


try:
    num1 = int(input("Enter the nnumber"))
    print(10/num1)
except ValueError:
    print("Enter the number not other types")
except ZeroDivisionError:
    print("can't be divide by zero")

# create own error
age = int(input('Enter the age'))

if age<0:
    raise ValueError("Age cannot be negative")

class ProductNotFound(Exception):
    pass
try:
    raise ProductNotFound("Product does not exist")
except ProductNotFound as e:
    print(e)

# logging 
import logging
logging.info("Starting server")
logging.info("User logged in")
logging.error("Payment failed")



def add(a, b):
    result = a + b
    breakpoint()   # Debugger stops here
    return result

x = add(10, 20)
print(x)
