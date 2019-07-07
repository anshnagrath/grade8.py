def isSquare():
    try:
      length = input("Please enter the length of rectangle: ")
      breadth = input("Please enter the breadth of rectangle: ")
      if isinstance(length,int) == isinstance(breadth,int):
        print("It is a sqaure")
      elif isinstance(length,float) == isinstance(breadth,float):
        print("It is a sqaure")   
      else:
           print("It is a sqaure") 

    except:
        print("Please provide a integer or float")
isSquare()