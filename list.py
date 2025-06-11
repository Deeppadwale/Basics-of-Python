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
# lsit can be store any data type 
myList=["deep","nadkuma","padwale"]
print(f"this is the list example {myList}")


mygymdit=["pinut buttor","banana","apple",]
price=38
print(f"this is my GYM plane:{mygymdit} {price:.2f}")

# allow duplicates

My_Account=[10000,2000,50000,4000,10000,3000.10000]
print(f"Alll duplicates{My_Account}")



# to dermine how meany item are present in list use len() method 

print(len(My_Account))


# list item can be any data type


my_name=['deep','nadkumar','padwale']
my_salary=[10000,15000,20000]
my_work=[True,False]

print (f"......{my_name}.......{my_salary}.......{my_work}")


#  A list can cotain any data types 


any_data_type=['deep','ajay',200,500]
print(any_data_type)

# It is also possible to use the list() constructor when creating a new list.

lsit_constructor=list(("deep","ajay","vijay","patil"))
print(lsit_constructor)

# list items handel 

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


marks1 = input("Enter a marks")
marks1.append(marks1)
 
marks2= input("Enter a  marks ")
marks2.append(marks2)

marks3=input("Enter a marks")
marks3.append()


