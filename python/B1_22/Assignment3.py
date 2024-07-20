row=int(input("Enter the number of rows "))
a=1
for i in range(0,row):
	for j in range(0,i+1):
	   print(a ,end="")
	   a=a+1
	print()
	
'''pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B1_22/SEM 2$ python3 p25.py
Enter the number of rows 5
1
23
456
78910
1112131415
'''
