#WAS to enter any number and print the sum of its digit
a=int(input("Enter  any  number:"))
s=0
while (a>0):
    c=a%10
    a=a/10
    s=s+c

print ("Numbers of digit:", format(s))
