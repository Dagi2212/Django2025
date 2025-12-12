def sqrt(num):
    i = 0
    while i * i <= num:
        i += 1
    return i - 1

print(sqrt(8))
