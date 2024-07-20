str=input("Enter the string ")
l=int((len(str))/2)
if(str[ :l]==str[l: ]):
	print("Given string is symetric")
else:
	print("Given string is not symetric")
	
'''pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B1_22/SEM 2$ python3 p29.py
Enter the string abcabc
Given string is symetric
pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B1_22/SEM 2$ python3 p29.py
Enter the string om
Given string is not symetric
'''
