#9 Write a Python program to count the frequency of words in a file. .
f = open("myfile.txt2",'r')
print(f.readlines(0,))
f.close()
print("-------------------------------------------------------------")

#10 Write a Python program to write a list to a file.
f = open("myfile.txt2",'r')
print(f.readlines())
f.close()
print("------------------------------------------------------------")

#11 Write a Python program to copy the contents of a file to another file

f2= "myfile.txt2"
f3= "myfile.txt3"
f2=open(f2,"r")
content = f2.read()
f3=open(f3,"w")
f3.write(content)
print("File copied successfully.")
print("--------------------------------------------------------------")
