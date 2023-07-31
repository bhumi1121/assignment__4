"""1.What is File function in python? What is keywords to create and write file.
ans--> File handaling is important part of any web application.
     - python has a sevral function for creating,reading,updating and delating file.
--> file.x(): is create a file.
    file.w():is write a file ."""

# 2.Write a Python program to read an entire text file.
f = open("myfile.txt",'r')
print(f.read())
f.close()
print("__________________________________________________________________")






