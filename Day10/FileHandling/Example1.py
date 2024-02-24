#Example1 - Writing data into text files
#We have pre-defined funciton called open()
#in the open() funciton we need to give the path of the file
#need to give specify the purpose of file for opening like are writing (w) or read(r)
#\n is used to print in the next lines
file = open("C:/Users/home/OneDrive/Desktop/DemoFIles/Myfile.txt", 'w')
file.write("This is my first statement \n")
file.write("This is my Second statement \n")
file.write("This is my third statement \n")
file.write("This is my fourth statement \n")
file.close()
print("Program completed")
