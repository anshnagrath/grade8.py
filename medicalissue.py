import logging
def medical_issue():
    med = str(input("Do you had a medical condition?(Enter Y fro yes and N for no) : "))
    print(med)
    if med == 'y' or med =='Y':
        print("You are allowed to give exams")
    else:
         print("You are not allowed to give exams") 
def cal_attendancepercentage():
    try:
        totalDays = int(input("Please enter total number of days of classes : "))
        daysAttended =int(input("Please enter number of days you atteneded classes : "))
        percentage = daysAttended/float(totalDays) * 100
        if percentage > 75:

            print("Attandance percentage is {} .You are allowed to give exams".format(percentage))
        else:
            medical_issue()
         
    except ValueError:
        logging.error("Error")
        print("Please enter a proper value")
cal_attendancepercentage()



