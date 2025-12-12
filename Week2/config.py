with open ("config.txt", "w") as file:
    content= file.write("Dagi")
try :
    with open ("config.txt", "r") as file:
     content = file.read()
     print("Welcome", content)
except :
    with open ("config.txt", "w") as file:
       content= file.write("Guest")
       print(content)

    