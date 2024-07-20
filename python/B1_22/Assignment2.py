a=int(input("Enter the marks in first subject: "))
b=int(input("Enter the marks in second subject: "))
c=int(input("Enter the marks in third subject: "))

d=(a+b+c)/3
print("Average of the marks is ",d)
if(90<=d<=100):
   print("Your grade is O ")
elif(80<=d<=89):
   print("Your grade is A ")

elif(70<=d<=79):
   print("Your grade is B ")

elif(60<=d<=69):
   print("Your grade is C ")

elif(40<=d<=59):
   print("Your grade is D ")

else:
   print("Your grade is F ")

"""
pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B1_22/SEM 2$ python3 Assignment2.py
Enter the marks in first subject: 76
Enter the marks in second subject: 45
Enter the marks in third subject: 80 
Average of the marks is  67.0
Your grade is C
"""
