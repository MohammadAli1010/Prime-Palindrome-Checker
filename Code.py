print("*************************WELCOME TO MY PYTHON MINI PROJECT*************************")
print("Name - Mohammad Ali")
print("Roll Number - 19")
print("Registration Number - 12211072 \n ")




n=int(input("Enter the number: "))
flag=0
for i in range(2,n):
    if n%i==0:
        flag=1
        break
if flag==1:
    print(n,"is not a Prime")
else:
    print(n,"is a Prime")

    x=n
    sum=0
    while x>0:
        r=x%10
        sum=sum*10+r
        x=x//10
    if sum==n:
        print(n,"is a Prime Palindrome \n ")
    else:
        print(n,"is not a Prime Palindrome \n ")

print("***************THANK YOU****************")
    
