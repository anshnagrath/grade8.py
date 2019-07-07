import random
def rps():
    try:
        userinput = int(input("Please enter 1 for rock,2 for papper and 3 for scissors: "))
        print("Now its computer turn")
        compareValue = random.randint(1,3)
        if (userinput == 1 and compareValue == 2) or(userinput == 2 and compareValue == 1):
             status = 'loose'
             if userinput == 1:
                 status = 'win'
             print('paper wins => You {}'.format(status))
               
        elif (userinput == 1 and compareValue == 3) or (userinput == 3 and compareValue == 1): 
                status = 'loose'
                if userinput == 1:
                    status = 'win'
                print("Rock wins => You {}".format(status))   

        else:
            status = 'loose'
            if userinput == 3:
                status = 'win'
            print("scisor win ==> You {}".format(status))
    except:
        print("Please enter a proper value")            
rps()      
