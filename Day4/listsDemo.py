# Example 1 -- Creating a list

mylist1 = ["10", "20", "30"]
mylist2 = ["Apple", "Mango", "Orange"]
mylist3 = ["Apple", "10", "Mango", "40"]
mylist4 = []
print(mylist1)
print(mylist2)
print(mylist3)
print(mylist4)

#Example 2 -- Accessing items from list
#IN list the index will start from 0
#Negative index is also allowed & It will calculate from the end
#If we give -1 it will print the last element
mylist = ["Apple", "Banana", "Mango"]
print(mylist)
print(mylist[0])
print(mylist[2])
print(mylist[-1])

#Example 3 -- Range of indexes -Used to extract multiple elements
mylist_ex_three = ["apple","mango","orange","cherry","banana","kiwi","melon"]
print(mylist_ex_three[2:5]) #orange, cherry,banana
print(mylist_ex_three[-4:-1])

#Example 4 -- Changing the item/element values
mylist_ex_four = ["apple","mango","cherry"]
print(mylist_ex_four)
mylist_ex_four[0] = "cherry"
print(mylist_ex_four)

#Example 5 - read items using loops
mylist_ex_five = ["apple","banana","cherry"]
for i in mylist_ex_five:
    print(i)

#Example 6 - Check the item/element is existing in the list or not
mylist_ex_six = ["apple","banana","cherry"]
if "apple" in mylist_ex_six:
    print("Yes, apple is present")
else:
    print("No, Apple is not present")

#Example 7 -- Counting no of items in the list

mylist_ex_seven = ["apple","banana","cherry"]
print(len(mylist_ex_seven))

#Example 8 - Adding new elemtns in the list -- Two functions are available append() and insert()
# append() function will add the elements at the end of the list
#insert() will add the element at the specified place
mylist_ex_eight = ["apple","banana","cherry"]
mylist_ex_eight.append("Mango")
print(mylist_ex_eight)
mylist_ex_eight.insert(0,"Kiwi")
print(mylist_ex_eight)

#Example 9 - Removing the items from the list
# Three methods we have, pop(), del keyword, clear()
#pop()
mylist_ex_nine = ['Kiwi', 'apple', 'banana', 'cherry', 'Mango']
mylist_ex_nine.pop(0)  #We should provide the index number to be removed
print(mylist_ex_nine)
#Del command
del mylist_ex_nine[2]  #Del command delete the item based on the index we have passsed
print(mylist_ex_nine)
#clear() function - It will clear all the items from the list but list variable will be available
mylist_ex_nine.clear()
print(mylist_ex_nine)

#Example 10 - Copy the list
mylist_ex_ten1 = ["apple","mango","orange"]
#Method1 - bY using list() function
mylist_ex_ten2 = list(mylist_ex_ten1)
print(mylist_ex_ten2)
#Method2 - copy() fucntion
mylist_ex_ten2 = mylist_ex_ten1.copy()
print(mylist_ex_ten2)

#Example 11 - joining/combaining the list
#Approach 1 using + Operator
list_ex_eleven1 = ["a","b","c"]
list_ex_eleven2 = [1,2,3]
print(list_ex_eleven1 + list_ex_eleven2)

#Approach2 using looping statement
mylist_ex_eleven1 = ["a","b","c"]
mylist_ex_eleven2 = [1,2,3]
for i in mylist_ex_eleven2:
    mylist_ex_eleven1.append(i)
print(mylist_ex_eleven1)

#Approach3 by using extend() function
list_ex_eleven1_Approach3 = ["a","b","c"]
list_ex_eleven2_Approach3 = [1,2,3]
list_ex_eleven1_Approach3.extend(list_ex_eleven2_Approach3)
print(list_ex_eleven1_Approach3)

#Example 12 - comparing two list are equal ot not
list1 = ["apple","mango"]
list2 = [1,2,3]
if list1 == list2:
    print("lists are equal")
else:
    print("lists are not equal")