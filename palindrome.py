n=input("Enter a word or a number: ")
inverse=n[::-1]
if n==inverse:
    print(f"{n} is a palindrome")
else:
    print(f"{n} is not a palindrome")