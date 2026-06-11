##Input
##Enter two number for Calculation

num1=int(input("Enter 1st number :"))
num2=int(input("Enter 2nd number :"))

ch=input("Enter what you do :")

if ch=='+':
    print(num1+num2)
elif ch=='-':
    print(num1-num2)
elif ch=='*':
    print(num1*num2)
elif ch=='/':
    if num2!=0:
        print(num1/num2)
    else:
        print("ERROR")



