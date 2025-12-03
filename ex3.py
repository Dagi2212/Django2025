num = int(input("Enter a number of your choice: "))
def factorial(n):
    i=1
    for j in range (1,n+1):
        i*=j
    return i 
print("Factorial of the number you entered is ", factorial(num))