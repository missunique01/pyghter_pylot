# Example3 -- Appending(Adding) data into the file use 'a' for adding new data to existing data in the file
file = open("C:/Users/home/OneDrive/Desktop/DemoFIles/Myfile.txt", 'a')
print(file.write("\n This is line from append mode \n"))
file.close()
print("Program executed")