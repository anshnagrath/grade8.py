
def age():
    try:
        age = sorted(list(map(int,input("Please enter ages comma seperated : "))))
        print("Youngest person age {}".format(age[0]))
        print("Oldest person age {}".format(age[len(age)-1]))
    except:
        print("Please Provide a proper input") 
age();