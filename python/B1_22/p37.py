a=[]
even=[]
odd=[]
b=int(input("Enter the number of inputs: "))
for i in range (0,b):
	c= int(input("Enter the number: "))
	a.append(c)
print(a)

for i in range (0,b):
	if a[i]%2==0 :
	 c=a[i]
	 even.append(c)
	else:
	 d=a[i]
	 odd.append(d)
print(even)
print(odd)

"""
pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B1_22/SEM 2$ python3 p37.py
Enter the number of inputs: 9
Enter the number: 11
Enter the number: 12
Enter the number: 13
Enter the number: 15
Enter the number: 14
Enter the number: 16
Enter the number: 17
Enter the number: 18
Enter the number: 19
[11, 12, 13, 15, 14, 16, 17, 18, 19]
[12, 14, 16, 18]
[11, 13, 15, 17, 19]
"""
