a=int(input("Enter the number "))
b=0
while(a>0):
     c=a%10
     b=(b*10)+c
     a//=10
print(b)

'''pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B1_22/SEM 2$ python3 p19.py
Enter the number 4502
2054'''
