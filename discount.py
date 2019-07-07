def cal_discount():
    try:
     quantity = int(input("Please Enter the quantity purchased: "))
     price_per_item = 100
     total = quantity * price_per_item
     if total > 1000:
        discount =  10/float(100) * total
        after_discount = total - discount
        print("You got a discount of {}".format(discount))
        print("Amount to be paid after discount : {}".format(after_discount))
     else:
        print("Amount to be paid : {}".format(total))    
    except:
          print("Please enter a integer")        
cal_discount()
