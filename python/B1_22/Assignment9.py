def check_list(lst):
	for i in lst:
		if i.isdigit():
			print(i*3)
		else:
			print(i+"#")
			
l1=list()
a=int(input("ENTER THE NO. OF ELEMENTS: "))
for i in range(a):
	c=input("ENTER THE ELEMENTS: ")
	l1.append(c)
print("the list is : ",l1) 
print(check_list(l1))



'''ENTER THE NO. OF ELEMENTS: 5
ENTER THE ELEMENTS: 2
ENTER THE ELEMENTS: 3
ENTER THE ELEMENTS: Darshan  
ENTER THE ELEMENTS: Karan
ENTER THE ELEMENTS: 22
the list is :  ['2', '3', 'Darshan', 'Karan', '22']
222
333
Darshan#
Karan#
222222
'''
