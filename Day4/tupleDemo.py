# Example1 - Creating a tuple
mytuple = ("apple", "mango", "cherry")
print(mytuple)
mytuple_empty = ()

#Example 2 - Accessing individual items in tuple
#Negtive index is also allowed in python
mytuple1 = ("apple","mango","cherry") # index starts from 0
print(mytuple1[1])
print(mytuple1[-2])

#Example 3 - range of indexes (Just like string slicing [startindex : endindex]
mytuple_ex_three = ("apple","mango","cherry","banana","orange","Kiwi","melon")
print(mytuple_ex_three[2:5])
print(mytuple_ex_three[-3:-1])

#Example 4 - changing the items/values in tuple
# By default tuples are immutable
#But there is a workaround
# tuple --> list(modify)--tuple
mytuple_ex_four = ("apple","mango",100)
print(mytuple_ex_four)
mylist = list(mytuple_ex_four)  #Changing the tuple to list
mylist[0] = "banana" #Modification of list
mytuple_ex_four = tuple(mylist) #Again changing the list to tuple
print(mytuple_ex_four)

#Example 5 -- Reading tuples items using loops
mytuple_ex_five = ("apple","mango","banana","cherry")
for i in mytuple_ex_five:
    print(i)

#Example 6 - Checking an item exist or not in the tuple
mytuple_ex_six = ("apple","mango","banana","cherry")
if "banana" in mytuple_ex_six:
    print("Yes, Banana is in the tuple")
else:
    print("No, Banana is not there in the tuple")

#Example 7 - Find the total no of items in tuple
mytuple_ex_seven = ("apple","mango","banana","cherry")
print(len(mytuple_ex_seven))

#Example 8 - Add items into the tuple
#Because tuple is immutable, we can't change the items or values
#mytuple_ex_eight = ("apple","mango","banana","cherry")
#mytuple_ex_eight[0] = "kiwi"  #TypeError: 'tuple' object does not support item assignment
#print(mytuple_ex_eight)

#Example 9 - copying the tuple
mytuple_ex_nine = ("apple","mango","banana","cherry")
mytuple_ex_nine2 = mytuple_ex_nine
print(mytuple_ex_nine2)

#Example 10 - removing items from tuple
#Not possible becasue tuple is iimutable
#Del tuple keyword will delte whole tuple
#mytuple_ex_ten = ("apple","mango","banana","cherry")
#del mytuple_ex_ten
#print(mytuple_ex_ten)


#Example 11 - combain/join tuples
mytuple_ex_eleven1 = ("apple","banana")
mytuple_ex_eleven2 = ("orange",100,200)
print(mytuple_ex_eleven1+mytuple_ex_eleven2)

#Example 12 - comparing two tuples are equal ot not
tuple1 = ("apple","mango")
tuple2 = (1,2,3)
if tuple1 == tuple2:
    print("tuples are equal")
else:
    print("Tuples are not equal")