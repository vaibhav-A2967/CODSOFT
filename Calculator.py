#calculator

while True:
    print("--welcome--\nCalculator options:\n1:Add\n2:subtract\n3:Multiplication\n4:Division\n5:Exit")
    n=int(input("Enter Your Option:"))
    if n==1:
        x=int(input("Enter the First number:"))
        y=int(input("Enter the Second number:"))
        print("The Sum is:",x+y)

    elif n==2:
        x=int(input("Enter the First number:"))
        y=int(input("Enter the Second number:"))
        print("The Difference is:",x-y)
    elif n==3:
        x=int(input("Enter the First number:"))
        y=int(input("Enter the Second number:"))
        print("The Multiplication is:",x*y)
    elif n==4:
        x=int(input("Enter the First number:"))
        y=int(input("Enter the Second number:"))
        print("The Division is:",x/y)
    elif n==5:
        print ("Thank You:)")
        break
    else:
        print("Enter a valid option !!!")
        continue
    
        
        
