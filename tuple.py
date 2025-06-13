# Tuple
# Tuples are used to store multiple items in a single variable.

# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

# A tuple is a collection which is ordered and unchangeable.

# Tuples are written with round brackets.

# a= (1,"Deep","padwale",45,45,100,200,3000)

# print (f"this is the {a}")

# no =a.count(45)
# no1=a.index(45)
# print(f"new tuple {no} {no1}")




# a="Deep"
# b="padwale"

# print(f"this is the full name : {a} and  {b}")



tuple_list=(0,1,2,3,4,5,6,7,8,9,"apple","banana","cherry","mango","potato","deep")


print(tuple_list[1])
print(tuple_list[2])
print(len(tuple_list))
print(tuple_list[1])

if "apple" in tuple_list :
    print("yes  the apple is in tuple list ")
if "deep " in tuple_list:
    print("Not in the tuple list ")


 # slicing 
tuple_list2=tuple_list[1:3]
print(tuple_list2)   

# # append tuple 

tuple_list3=list(tuple_list)
tuple_list3.append("this is the ")     
# tuple_list3.pop(3)
tuple_list3[2]="deep"       

tuple_list=tuple(tuple_list3)

print(tuple_list)
res=tuple_list.index(3,3 ,7)
print(res)


# print the count of the present tuple 

count_tuple=tuple_list.count("deep")
print(count_tuple)
