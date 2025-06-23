day=int(input("Enter a number"))

match day:
    case 1:
      print("Monday")
    case 2:
      print("tuesday")
    case 3:
      print("wednesday")
    case 4:
      print("thuseday")
    case 5:
     print("Friday")
    case 6:
     print("saturday")


# Default Value

# Use the underscore character _ as the last case value if you want a code block to execute when there are not other matches:



day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")



    mark=int(input("Enter a number "))

    match mark:
      
      case 100 |  95 | 90 | 85 if mark >=85: 
        print ("student have got excelant marks ")
      
      case 80 | 75 | 70 :
        print("student have got B gread ")
      
      case 65 | 60 if  mark< 60 :
        print ("student have got c grade")   

