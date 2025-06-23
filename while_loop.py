i = 1
while i < 6:
  print(i)
  i += 1


x=1
while x < 6 :
  print (x)
  x=x+1


password = ""
attemt=0
while password != "open123":
    password = input("Enter the password: ")
    attemt=attemt+1
    
    if attemt>3 and password != "open123":
         attemt=attemt+1
         print("too much enter password is wrong ")

print("Access granted!")


password=""

attempt=0

max_a=5

while password !="open123" and attempt < max_a :
    password=input("enter a password")
    attempt=attempt+1

    if attempt == 3 and password != "open123":
     print ("Enter password is 3 time wrong ")

    elif attempt == 4 and password !="open123":
     print ("Enter a password is 4 time wrong you have last chance left")


if password=="opn123":
 print ("access is grant !")
else:
 print("Access denied. You have exceeded the maximum number of attempts.")


# ATM PIN Entry (Limited Tries)


pin="123"
attemt=1

while attemt<=3:
    enter=input ("Enter a password")
    if pin==enter:
        print ("Enter password")
        break
    else :
     print("incorrect password")
     attemt +=1
else:
    print("Too many attempts. Card blocked.")


import time

seconds = 5
while seconds > 0:
    print(seconds)
    time.sleep(1)
    seconds -= 1
print("Time's up!")


battery=0

while battery <100:
    battery+=10   
    print (f"{battery}%")

   
print ("battery is fill")   

