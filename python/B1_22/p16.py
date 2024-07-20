a=int(input("Enter the units used "))
if(a<=100):
  print("No charge")
elif(100<a<=200):
  print("Total bill amount is ",(a-100)*5)
elif(200<a):
  a=a-100
  bill1=100*5
  b=a-100
  bill2=b*10
  bill=bill1+bill2
  print("Total bill amount is ",bill)
 
'''pl-ii@plii-HP-Pro-Tower-280-G9-PCI-Desktop-PC:~/B1_22/SEM 2$ python3 p16.py
Enter the units used 350
Total bill amount is  2000'''
