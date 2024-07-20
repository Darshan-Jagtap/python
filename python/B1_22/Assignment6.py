price=[]
a=3

for i in range (0,3):
 b=input("Enter the items: ")
 c=float(input("Enter the values: "))
 d=(b,c)
 price.append(d)
print(price)
sorted_price=sorted(price,key=lambda x:float(x[1]))
print(sorted_price)

"""
pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B1_22/SEM 2$ python3 Assignment6.py
Enter the items: laptop     
Enter the values: 266.55
Enter the items: TV
Enter the values: 55.5
Enter the items: Mobile
Enter the values: 5550
[('laptop', 266.55), ('TV', 55.5), ('Mobile', 5550.0)]
[('TV', 55.5), ('laptop', 266.55), ('Mobile', 5550.0)]
"""
