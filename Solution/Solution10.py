#was to enter any number and check  it is palindrom number or not.
no=int(input("Enter any number:"))
sum=0
temp=no
while(no>0):
    x=no%10
    sum=sum*10+x
    no=no//10
if (temp==sum):
    print ("It is a palindrom number" ,format(temp))
else:
    print ("It is a not palindrom Number" ,format(temp))
