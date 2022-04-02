def fact(n):
    #if (n == 1 or n == 0):
    #   return 1
    #else:
    #   return (n * fact(n-1))

    return 1 if (n==1 or n==0) else n * fact(n - 1)
a = int(input("Enter the number : "))
print("The factorial of the number",a,"is : ",fact(a))