# error_investigation.py
from random import randint

a = 10
b = 0
numbers = [1, 2, 3, 4, 5]
value = "ten"
answer = 0

r = randint(1, 4)
try:
    if r == 1:
        answer = int(value)
    elif r == 2:
        answer = numbers[5]
    elif r == 3:
        answer = a / b
    else:
        answer = 42 # no error on this  branch
except IndexError:
    print ("invalid index")
    answer = numbers[-1]
except ZeroDivisionError:
    print ("You can't divide by zero")
    answer = 0
# except Exception is called the catch-all error handler
# no matter what goes wrong this will be triggered
except Exception as ex:
    print ("Something went wrong")
    print (ex)
    print (ex.__class__.__name__)
    answer = -1  
finally:
    # this code gets run regardless
    # it gets run if an exception occurs
    # it gets run if no exception occurs
    print (f"The answer is {answer}")
print ("finished")