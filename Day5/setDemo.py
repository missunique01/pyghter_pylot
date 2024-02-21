#Example 1 - Creating a set
myset = {"mango","apple","cherry"}
print(myset)

#Example2 - Accessing items/values from set
#we can't specify the value from set, becasue it is unordered list
myset_ex_two = {"mango","apple","cherry"}
for i in myset_ex_two:
    print(i)
#Example 3- value exists or not
myset_ex_three = {"mango","apple","cherry"}
#Approcah1
if "apple" in myset_ex_three:
    print("Yes, apple is available")
else:
    print("No, apple is not available")
#aprpoach2
print("apple" in myset_ex_three)
print("banana" in myset_ex_three)

#Example 4 -- adding items to set
# two functions - add() & update()
#add() - adding only single item to the set
#update() - Adding multiple items at a time to the set
myset_ex_four1 = {"mango","apple","orange"}
myset_ex_four1.add("cherry")
print(myset_ex_four1)
myset_ex_four2 = {"mango","apple","orange"}
myset_ex_four2.update(["banana","cherry"])
print(myset_ex_four2)

#example 5 - finding the length of a set
myset_ex_five = {"mango","apple","orange"}
print(len(myset_ex_five))

#Example 6 - remove items from set
# remove() , discord()
#If we try to remove a value/item which is not available in the set then it will through an error
#discard() wont through any error if we try to discard the non existing value
myset_ex_six = {"mango","apple","cherry","banana","kiwi"}
myset_ex_six.remove("banana")
print(myset_ex_six)
#myset_ex_six.remove("abc")  #KeyError: 'abc'
myset_ex_six2 = {"mango","apple","cherry","banana","kiwi"}
myset_ex_six2.remove("banana")
print(myset_ex_six2)
myset_ex_six2.discard("xyz")

#Example 7 -- Clear all items from the set
#clear() function will clear the values in the set but wont remove the set
myset_ex_seven =  {"mango","apple","cherry","banana","kiwi"}
myset_ex_seven.clear()
print(myset_ex_seven) #we get the variable

#If we want to delete set along with data then use del keyword this through an if we try to print post deletion
#del myset_ex_seven
#print(myset_ex_seven) #NameError: name 'myset_ex_seven' is not defined.

#Example 8 - combain/join two sets - union() function, Update function
set1 = {"a","b","c"}
set2 = {1,2,3}
set3 = set1.union(set2)
print(set3)
set1.update(set2)
print(set1)