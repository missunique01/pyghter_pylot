# create string variables
#Eaxmple 1 creating variable in different ways
s1 = "welcome"
s2 = 'welcome'
s3 = str('welcome')
s4 = str("welcome")
# creating empty string variables
name = " "
name1 = ' '
name2 = str( )

# way of creating string variables
# Operations on variables
# Mutable & Immutable strings
# Mutable - can change the value of the variable
# Immutable - can't change the value of the variable
# string is mutable or immutable?
# strings are immutable
str1 = "Welcome"
print(id(str1)) #ID = 2007447430448

str1 = str1 + "to Python Class"
print(id(str1)) #ID = 2081250103648

# if the value is changed After updation then it is immutable

#xample 3 + and * in string

str = "welcome"
print(str + " programming") # Concatenation
print(str * 3) #printing multiple times

# Example 4 -- Slicing in strings  slicing symbol [ ]
str_slice = "welcome"
print(str_slice[1:4]) # Start index & End Index provided
print(str_slice[:3]) # Start index is 0 by default & end index is 5
print(str_slice[3:]) # If we haven't provided ending index it'll take everything
print(str_slice[1:-1]) # as the end index is -1 it won't consider the last 1 character

#Example 5 - ord() & chr()
# we have ascii characters
# to get ascii character number we need to use ord() function
# to get the ascii character represented by number
print(ord('A'))
print(chr(65))

#Example -6 max() min() len() functions

print(max('abc'))
print(min('abc'))
print(len("welcome"))

#Example 7 - Using IN , NOT IN Operators - returns true or false

s= "welcome"
print("we" in s)
print("Na" in s)
print("we" not in s)
print("Done Example 7")
# Example 8 - Comparing strings
print("tim" == "tie") #False
print("Free" != "Freedom") #True
print("arrow" > "aron")  # True A = a, r= r, r >o, o >n, and the word "Arrow" has 5 letters then the word "aron"
print("right" >= "left") #True right has 5 words & left has 4 letters
print("teeth" < "tee")  #False because teeth has 5 letters & tee has 3 letters which is teeth is > tee
print("yellow" <= "fellow") # false because y not less than f
print("abc" > " ") #True
print("Done Example 8")
# example 9 Testing strings True/False
s_str= "welcome To Python"
print(s_str.isalnum())  # False no numbers available in the string
print("welcome".isalpha()) # True - As we are having alphabets in the string

print("2001".isdigit())  # Returns True as we have only digits in the string

print("welcome".islower())  # True as every letter in the word is in lower case
print("Welcome".islower())
print("Welcome".isupper()) # False as we one letter is upper case & other letters are in lower case
print("WELCOME".isupper()) # Returns True as every letter in the word is in upper case

print(" ".isspace()) # If the string contains whitespaces then it'll return true otherwise fasle
print(s_str.isspace())  #False

# Example 10 - Searching for substrings
example_ten_String = "welcome to python"
print(example_ten_String.endswith("hon"))
print(example_ten_String.startswith("wel"))
print(example_ten_String.find("wel"))  #gives the index number of string starting
print(example_ten_String.find("becomes")) #Returns -1 if we dont have that string the string
print(example_ten_String.count("o"))  # Gives the number of occurences of substring in the string

#Example 11 - Converting the strings
ex_eleven_string = "String in Python"
print(ex_eleven_string.capitalize()) #this function used to make first word in paragraph to upper case & others in lowercase
print(ex_eleven_string.title()) #It will give string in title format
print(ex_eleven_string.lower()) # converts all words to lower case
print(ex_eleven_string.upper()) # converts all words to upper case
print(ex_eleven_string.swapcase()) # Converts the upper case characters to lowercase &vice versa
print(ex_eleven_string.replace("in", "on")) # replace the words with given inputs

#Example 12 - Reverse a string
ex_twelve_string = "welcome"
#Method1
rev_str = " "
for i in ex_twelve_string:
    rev_str = i + rev_str
print("Reversed string is ", rev_str)
#method2
print(ex_twelve_string[::-1])  # Slicing string startindex & End index not provided so it will from start to end and as we give -1 it will take from ending

