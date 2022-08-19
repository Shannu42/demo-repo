file=open("swap.txt","r")
s=file.read()
file1=open("swapped.txt","r")
s1=file1.read()
file.close()
file1.close()


file2=open("swap.txt","w")
file2.write(s1)
file3=open("swapped.txt","w")
file3.write(s)
file2.close()
file3.close()

