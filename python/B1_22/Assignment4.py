number=False
upper=False
lower=False

password=input("enter your password: ")
if len(password)>=8 :
	length=True
for i in password:
	if (i.isdigit()==True):
		number=True
	if(i.isupper()==True):
		upper=True
	if(i.islower()==True):
		lower=True
	
if(number==True and upper==True and lower==True):	
	print("password is valid")
else:
	print("password is invalid")
	
"""
pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B1_22/SEM 2$ python3 Assignment4.py
Enter the password: DArshan2005
Password is valid
"""
