#Example 2 -- reading the file
file = open("C:/Users/home/OneDrive/Desktop/DemoFIles/Myfile.txt", 'r')
#print(file.read())  #To read entire file
print(file.readline()) #To read first line of the text
file.close()