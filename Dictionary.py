# Python Dictionaries

dictionary_lists={"name":"Deep",
                 "age":36,
                 "address":"kolhapur"}
print (dictionary_lists)



dictionary_list = {}

name = input("Enter a Name: ")
last_name=input("Enter a last_name")
id = input("Enter an ID: ")
age=input("Enter a age")


dictionary_list[id] = {"name":name,   "last Name":last_name ,  "age":age}


print(dictionary_list)
print(type(dictionary_list))

X=dictionary_lists.get("name")
print(X)
# Accessing Items