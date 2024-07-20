a=[]
b=int(input("Enter the number of inputs: "))

for i in range (0,b):
	c= int(input("Enter the number: "))
	a.append(c)
print(a)
key=int(input("Enter the key value: "))

for i in range (0,b):
	if a[i]==key :
		print("The element index position is " + str(i))
	
	elif i==b :
		print("The element is not present in list")
		
"""
pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B1_22/SEM 2$ python3 p36.py
Enter the number of inputs: 5
Enter the number: 23 
Enter the number: 45
Enter the number: 85 
Enter the number: 43
Enter the number: 86
[23, 45, 85, 43, 86]
Enter the key value: 45
The element index position is 1
"""
