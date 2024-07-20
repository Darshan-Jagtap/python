str=input("Enter the string: ")
letter=False
number=False

for i in str:
 if(i.isalpha()==True):
    letter=True
 elif(i.isdigit()==True):
    number=True
 
if(letter==True and number==True):
	print("In given string both letter and numbers are present")

else:
	print("In given string both letter and numbers are not present")
	
"""
pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B1_22/SEM 2$ python3 p31.py
Enter the string: python3
In given string both letter and numbers are present
pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B1_22/SEM 2$ python3 p31.py
Enter the string: python
In given string both letter and numbers are not present
"""
