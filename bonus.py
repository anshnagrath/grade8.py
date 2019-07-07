def cal_bonus():
    try:
        salary = input("Please provide your salary amount :")
        years = input("Please enter the year of service :")
        if years>5:
            bonusAmount = 5/float(100) *salary
            netamount = salary + bonusAmount
            print("Your bonus Ammount {}".format(bonusAmount))
            print("Your net Ammount {}".format(netamount))
        else:
            print("you are not elegible for bonus")
            print("Your net Ammount {}".format(salary))    
    except:
        print("Please provide a proper input")        
cal_bonus()        