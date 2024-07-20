a=[]
b=int(input("Enter the number of inputs: "))

for i in range (0,b):
	c= int(input("Enter the number: "))
	a.append(c)
print(a)

len(a)
total_sum=sum(a)
avg=total_sum/len(a)
minimum=min(a)
maximum=max(a)
reverse=a[ : :-1]
#print(len(a))
print("Reverse of list is "+ str(reverse))
print("Sum of list is "+ str(total_sum))
print("Average of list is "+ str(avg))
print("Lowest number in list is "+ str(minimum))
print("Highest number in list is "+ str(maximum))

"""
pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B1_22/SEM 2$ python3 Assignment5.py
Enter the number of inputs: 5
Enter the number: 24 
Enter the number: 36
Enter the number: 47
Enter the number: 23
Enter the number: 86
[24, 36, 47, 23, 86]
Reverse of list is [86, 23, 47, 36, 24]
Sum of list is 216
Average of list is 43.2
Lowest number in list is 23
Highest number in list is 86
"""
