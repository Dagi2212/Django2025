with open ("uppercase.txt", "w") as file:
    content= file.write("Python is fun")
try :
    with open ("uppercase.txt", "r") as file:
     content = file.read()
     print( content.upper())
except :
       print("File not found!")

    