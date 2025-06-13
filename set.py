# # crete a programe to get the input form user and print the input in form of set data type 

set_list=()

new_list=list(set_list)

print(type(new_list))

set1=input("Enter a  firts set number ")

new_list.append(set1)

set2=input("Enter a second number")
new_list.append(set2)

set3= input("Enter a number thired")
new_list.append(set3)

set4= input("Enter a number four")
new_list.append(set4)

set5= input("Enter a number five")
new_list.append(set5)

set6= input("Enter a number six")
new_list.append(set6)

set7= input("Enter a number Seven")
new_list.append(set7)

set_list=set(new_list)

print(set_list)

print(type(set_list))




set_items={'Ajay', '80', 'Shubham 100', ' Radha ', '90', '100', 'Deep'}
set_list.update(set_items)
print(set_list)

# To add items from another set into the current set, use the update() method.



# The union() and update() methods joins all items from both sets.

# The intersection() method keeps ONLY the duplicates.

# The difference() method keeps the items from the first set that are not in the other set(s).

# The symmetric_difference() method keeps all items EXCEPT the duplicates.