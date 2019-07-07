def cal_attendancepercentage():
    try:
        totalDays = int(input("Please enter total number of days of classes : "))
        daysAttended =int(input("Please enter number of days you atteneded classes : "))
        percentage = daysAttended/float(totalDays) * 100
        if percentage > 75:

            print("Attandance percentage is {} .You are allowed to give exams".format(percentage))
        else:
            print("Attandance percentage is {} .You are not allowed to give exams".format(percentage))    
         
    except:
        print("Please enter a proper value")
cal_attendancepercentage()