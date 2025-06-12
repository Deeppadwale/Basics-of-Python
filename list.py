# list  :

# list are used to store multiple items in single variable 
# list are one of four bilt in data types in python used to store collection of data . 
# and other three are set , tuple ,dictionaty 
# list are created in square brackets 
# list items are ordered,changeble,and allow duplicate value
# lsit items are indexed first is [0] index and second is a [1] index 
# when we was say that the item is ordered itmeans that the item have diffrent 
# lsit are changebale means list are add and remove items in a list  has been changed 
# list allow duplicates 
# list item can be any data type 
# # lsit can be store any data type 
# myList=["deep","nadkuma","padwale"]
# print(f"this is the list example {myList}")


# mygymdit=["pinut buttor","banana","apple",]
# price=38
# print(f"this is my GYM plane:{mygymdit} {price:.2f}")

# # allow duplicates

# My_Account=[10000,2000,50000,4000,10000,3000.10000]
# print(f"Alll duplicates{My_Account}")



# # to dermine how meany item are present in list use len() method 

# print(len(My_Account))


# # list item can be any data type


# my_name=['deep','nadkumar','padwale']
# my_salary=[10000,15000,20000]
# my_work=[True,False]

# print (f"......{my_name}.......{my_salary}.......{my_work}")


# #  A list can cotain any data types 


# any_data_type=['deep','ajay',200,500]
# print(any_data_type)

# # It is also possible to use the list() constructor when creating a new list.

# lsit_constructor=list(("deep","ajay","vijay","patil"))
# print(lsit_constructor)

# # list items handel 

list_item_handel=['apple','banan','penutbutter','deep','padwle']
list_item_handel[2]="cherry"

print(list_item_handel)
print(list_item_handel[0:3])
print(list_item_handel[-3:-2])


# Append Items
# add the item in the end 

append_items=["orange","apple","banana"]
append_items.append("orange")
print(append_items)

# insert the item

append_items.insert(1,"deep")
print(append_items)

# Extend List

# To append elements from another list to the current list, use the extend() method.

x=['orange,','banana','yello','pink','salad','jk']

y=['weyprotin','pink','orange','shubham']
x.extend(y)
print(x)

# remove list items 


remove_items=['deep','nandkumar','padwale','ajay']
remove_items.remove('ajay')
print(remove_items)

# If you do not specify the index, the pop() method removes the last item.
remove_items.pop()
print(remove_items)

# The del keyword also removes the specified index:
# The del keyword can also delete the list completely.

del remove_items[1]
print(remove_items)
print('deep'in remove_items)


# create a program to add the marks in list  


# marks=[]
# marks1 = int(input("Enter a marks"))
# marks.append(marks1)
 
# marks2= int(input("Enter a  marks "))
# marks.append(marks2)

# marks3=int(input("Enter a marks"))
# marks.append(marks3)
# print (marks)

# Loop Through a List
# You can loop through the list items by using a for loop:

inlisst=["deep","padwale"]
for x in inlisst:
 print (x)
print(type(x))

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


new_name=["deep","is","good","programmer"]
for i in range(len(new_name)):
  print(new_name[i])


  thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


  my_list=["deep","is","good","programmer","and","he learning","python"]
  i=0
  while i < len(my_list):
    print(i)
    i=i+1

 # Looping Using List Comprehension
hello=["7","0""frrrrr"]
[print(x) for x in hello]





# create a program to   MOst inportan program to learn coditions 


my_lists=['apple', 'banana', 'orange', 'kivi']
new_list=[]
for x in my_lists:
  if "e" in x:
      new_list.append(x)
 
  

print(f'{new_list}')

# -------------------------------------------------------------------------------------------
account_comprension=['Deep','is','good','programmer']
newaccount=[x for x in account_comprension if "e" in x]

newaccounts=[x for x in account_comprension  if x !="Deep"]

print (newaccount)

print (newaccounts)



salary_list = [1000, 2000, 15000, 18000, 23000, 45000, 60000, 70000, "apple", "banana", "orang", "mango"]

# Remove 23000
adjust_for_this_month = [y for y in salary_list if y != 23000]

# Keep only numbers greater than 23000
adjust_for_this_month_new = [y for y in salary_list if isinstance(y, (int, float)) and y > 23000]

# Remove "banana"
adjust_for = [x for x in salary_list if x != "banana"]

# Remkov
new= [x if x != "apple" else "deep is good programmer " for x in salary_list ]

newlist = [x if x != "banana" else "orange" for x in salary_list]

#  TypeError: '>=' not supported between instances of 'str' and 'int' to avoid this Error use isinstance
gen_knowlege=[y for y in salary_list if isinstance(y,(int,float)) and y>1000]

print("Without 23000:", adjust_for_this_month)
print("Salaries > 23000:", adjust_for_this_month_new)
print("Without 'banana':", adjust_for)
print(f"replace apple with deep is good programmer{new}")
print(f"salary >10000 :{gen_knowlege}")

#-----------------------------------------------------------------------------------


