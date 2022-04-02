def fibonacci(n):
    if (n <= 1):
        return 1
    else:
        return (fibonacci(n-1)+fibonacci(n-2))
a = int(input("Enter the number of terms : "))
for i in range(a):
    print(fibonacci(i), end=' ')