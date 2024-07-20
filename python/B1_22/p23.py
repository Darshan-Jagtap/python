row=int(input("Enter the number of rows "))

for i in range(row,0,-1):
	for j in range(0,i):
          print("*",end="")
	print()
	
'''pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B1_22/SEM 2$ python3 p23.py
Enter the number of rows 5
*****
****
***
**
*
'''
