# Python If ... Else


# Python Conditions and If statements


a=134,555,66666
b=333,4545,65656

if a <b:
    print ("thes is correct format ")

    # Elif
    # The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
    
    print (a) if a < b else print(b)    

# And  
# The and keyword is a logical operator, and is used to combine conditional statements:


# Test if a is greater than b, AND if c is greater than a:

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#   The or keyword is a logical operator, and is used to combine conditional statements

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")



#   neated if statement

# create a voting manegment system 
 
       
age=int(input("Enter you age "))

if age >=18:
   print("you are eligibel for the voat ")

   if age >=21 or age <=25 :
      print ("you are eligible and young person")

      if age >=30 and age <= 40 :
         print("cogratulation you are sinior cityzon")
else:
   print ("you are not eligible for vote")
