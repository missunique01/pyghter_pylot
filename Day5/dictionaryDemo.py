#Example1 -- Creating a dictionary
mydic_ex_one = {101:"x",102:"y",103:"z"}
print(mydic_ex_one)

#Example 2 -- accessing items from dictionary
#When we want to access the items we need to use the key
mydic_ex_two = {"brand":"Hundai",
                "model":"i10",
                "year":"2021"
                }
print(mydic_ex_two["brand"])
print(mydic_ex_two["model"])
print(mydic_ex_two["year"])
#Using get() function also we can access the dictionary
print(mydic_ex_two.get("brand"))

# Example3 -- Changing the values(Not keys) in the dictionary
mydic_ex_three = {
    "brand":"Hundai",
    "model":"i10",
    "year":"2021"
}
mydic_ex_three["year"] = 2022
print(mydic_ex_three)

# Example 4 - reading dictionary using loop
mydic_ex_four ={
    "brand":"Hundai",
    "model":"i10",
    "year":"2021"
}
for i in mydic_ex_four:
    print(i) #prints only keys from dictionary
    print(mydic_ex_four[i])  # Prints the values from dictionary
 #Prints values only from dictionary
for i in mydic_ex_four.values():
    print(i)
#Printing keys along with values
for x,y in mydic_ex_four.items():
    print(x,y)

#Example 5 -- check key is existing in the dictionary or not
mydic_ex_five = {
    "brand":"Hundai",
    "model":"i10",
    "year":"2021"
}

#Approach1
if "model" in mydic_ex_five:
    print("Exist")
else:
    print("Not Exist")
#Approach2
print("model" in mydic_ex_five)

#Example 6 -- find number of items in dictionary
mydic_ex_six = {
    "brand":"Hundai",
    "model":"i10",
    "year":"2021"
}

print(len(mydic_ex_six))

#Example7 -- Adding items to dictionary
mydic_ex_seven = {
    "brand":"Hundai",
    "model":"i10",
    "year":"2021"
}
mydic_ex_seven["color"] = "red"
print(mydic_ex_seven)

#Example 8 -- Remove item from dictionary
#pop(), dek keyword
mydic_ex_eight = {
    "brand":"Hundai",
    "model":"i10",
    "year":"2021"
}
mydic_ex_eight.pop("year")
print(mydic_ex_eight)
mydic_ex_eight1 = {
    "brand":"Hundai",
    "model":"i10",
    "year":"2021"
}
del mydic_ex_eight1["year"]
print(mydic_ex_eight1)

#Example 9 -- Deleting dictionary along with items use del keyword
mydic_ex_nine ={ "brand":"Hundai",
    "model":"i10",
    "year":"2021"
}
del mydic_ex_nine  #It will remove the dictionary
#print(mydic_ex_nine) #if we try to print it will throw error NameError: name 'mydic_ex_nine' is not defined.
#Example 10 -- clear the items in the dictionary but dictionary should be available use clear()
mydic_ex_ten = { "brand":"Hundai",
    "model":"i10",
    "year":"2021"
}
mydic_ex_ten.clear()
print(mydic_ex_ten)

#Example 11 -- Copy one dictionary to another dictionary
mydic_ex_eleven =  { "brand":"Hundai",
    "model":"i10",
    "year":"2021"
}
#Approach1 - without using copy function
mydic_ex_eleven2 = mydic_ex_eleven  #Copying one dictionary to other dictionary
print(mydic_ex_eleven2)
#Approch2 -- Using copy() function
mydic_ex_eleven3 = mydic_ex_eleven.copy()
print(mydic_ex_eleven3)

