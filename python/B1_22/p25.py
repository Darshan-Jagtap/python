row=int(input("Enter the number of rows "))
i=0
for i in range (0,row):
	for j in range (0,i+1):
		print("*",end="")
	print()
for i in range (row,0,-1):
	for j in range (0,i):
		print("*",end="")
	print()
	
'''pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B1_22/SEM 2$ python3 p25.py
Enter the number of rows 5
*
**
***
****
*****
*****
****
***
**
*
'''
