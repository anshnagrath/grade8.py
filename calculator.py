import logging

def add_numbers():
    numbers = []
    numberCount = int(input("Please enter the count of numbers that you want to add: "))
    while(numberCount>0):
          number = int(input("Please insert the number to add: "))
          numbers.append(number) 
          if numberCount == 1:
              s = sum(numbers)
              print("The total is {}".format(s))
          numberCount = numberCount - 1

def sub():
    numbers = []
    numberCount = int(input("Please enter the count of numbers that you want to subtract: "))
    while(numberCount>0):
          number = int(input("Please insert the number to subtract: "))
          numbers.append(number) 
          if numberCount == 1:
              d =numbers[0] - sum(numbers)
              print("The total difference is {}".format(d))
          numberCount = numberCount - 1

def divide():
    numbers = []
    numberCount = int(input("Please enter the count of numbers that you want to divide: "))
    while(numberCount>0):
          number = int(input("Please insert the number : "))
          if len(numbers) > 0:
              val = numbers[len(numbers)-1]/number
              numbers.pop()
              numbers.append(val)
          else:
              numbers.append(number)
          if(numberCount == 1):
            print('value after divisioni is {}'.format(numbers[len(numbers)-1]))     
          numberCount = numberCount -1  
def multiply():
    numbers = []
    numberCount = int(input("Please enter the count of numbers that you want to multiply: "))
    while(numberCount>0):
          number = int(input("Please insert the number to multiply: "))
          if len(numbers) > 0:
              val = numbers[len(numbers)-1] * number
              numbers.pop()
              numbers.append(val)
          else:
              numbers.append(number)
          if(numberCount == 1):

            print('value after multipication is {}'.format(numbers[len(numbers)-1]))    
          numberCount = numberCount -1 
def remainder():
    numbers = []
    numberCount = int(input("Please enter the count of numbers that you want to find the remainder for: "))
    while(numberCount>0):
          number = int(input("Please insert the number : "))
          if len(numbers) > 0:
              val = numbers[len(numbers)-1] % number
              numbers.pop()
              numbers.append(val)
          else:
              numbers.append(number)
          if(numberCount == 1):
                 print('value after multipication is {}'.format(numbers[len(numbers)-1]))    
          numberCount = numberCount -1 


try:
    userInput = str(input("Please Enter 'a' to add , 's' to subtract , 'd' to divide , 'm' to multiply , 'r' to find out remainder:  "))
    if userInput == 'a' or userInput == 'A':
        add_numbers()
    elif userInput == 's' or userInput == 'S':
        sub()    
    elif userInput == 'd' or userInput == 'D':
        divide()   
    elif userInput == 'm' or userInput == 'M':
        multiply()   
    elif userInput == 'r' or userInput == 'R':
        remainder()               

except ValueError:
    logging.error('Error')
    print("Please enter a proper value")   