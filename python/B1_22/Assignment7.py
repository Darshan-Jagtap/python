text=input("ENTER THE STRING:")
words=text.split()
d={ }

for i in words:
	if len(i)in d:
		d[len(i)]=d[len(i)]+1
	else:
		d[len(i)]=1
print(d)


''''pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B1_22/SEM2$ python3 Assignment7.py
ENTER THE STRING: I AM THE STUDENT OF KKWIEER COLLEGE WHICH IN IN NASHIK
{1: 1, 2: 4, 3: 1, 7: 3, 5: 1, 6: 1}
'''
