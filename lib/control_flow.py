#!/usr/bin/env python3

#def admin_login(username, password):
#    # your code here
#    pass

def hows_the_weather(temperature):
  if temperature < 40 :
    return("It's brisk out there!")
  elif temperature <= 65 and temperature >= 40 :
    return("It's a little chilly out there!")
  elif temperature >= 85 :
    return("It's too dang hot out there!")
  else:
    return("It's perfect out there!")


def fizzbuzz(num):
  if num % 15 == 0:
    return "FizzBuzz"
  elif num % 3 == 0:
    return "Fizz"
  elif num % 5 == 0:
    return "Buzz"
  else:
    return(num)





def calculator(operation, num1, num2):
  if(operation == "*"):
    return(num1 * num2)
  elif(operation == "/"):
    return(num1 / num2)
  elif(operation == "-"):
    return(num1 - num2)
  elif(operation == "+"):
    return(num1 + num2)
  else:
    print("Invalid operation!")
    return(None)


def admin_login(username, password):
  if username == "admin" or username == "ADMIN":
    if password == "12345":
      return("Access granted")
    else:
      return("Access denied")
  else:
    return("Access denied")


"""

True and True
# True
False and False
# False
False and True
# False
True or True
# True
False or False
# False
False or True
# True
not True
# False
not not True
# True

"""