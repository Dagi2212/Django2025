total = 0
numbers = [200, 450, 'abc', 700]
with open("numbers.txt", "w") as file:
   for item in numbers:
        file.write(f"{item}\n")
with open("numbers.txt", "r") as file:
    for value in file:
        value = value.strip()
        if value:  
            try:
                total += int(value)
            except ValueError:
                pass  

print(f"Sum = {total}")
#same with question num 12