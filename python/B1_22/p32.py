str=input("Enter String: ")
s=str.split()
print(s)

for i in s:
	a=i[0].upper() + i[1:-1] + i[-1].upper()
	print(a,end=" ")
	
"""
pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B1_22/SEM 2$ python3 p32.py
Enter String: darshan jagtap
['darshan', 'jagtap']
DarshaN JagtaP 
"""
