basic=int(input("Enter the basic salary "))
HRA= basic*10/100
TA= basic*5/100
total= basic+HRA+TA
tax = total*2/100
final_sal= total-tax
print("Salary after deduction ",final_sal)

'''pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B1_22/SEM 2$ python3 p12.py
Enter the basic salary 21000
Salary after deduction  23667.0
'''
