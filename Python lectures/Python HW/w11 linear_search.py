def linear_search(arr, target_value):
    for i in range(len(arr)):
        if arr[i] == target_value:
           return i
    return -1

my_list =[25,30,35,40,45,50,55] 
x = 50

result = linear_search(my_list,x)

if result != -1:
   print ("The number is found", result)
else:
   print ("The number is not found!")

my_list_fruits =["banana","orange","kiwi","apple"] 
x = "orange"

result = linear_search(my_list_fruits,x)

if result != -1:
   print ("The number is found", result)
else:
   print ("The number is not found!")

my_list_birthyear =[1960, 1988,2003,2009,2015] 
x = 2020

result = linear_search(my_list_birthyear,x)

if result != -1:
   print ("The number is found", result)
else:
   print ("The number is not found!")

        