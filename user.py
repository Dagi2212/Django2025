def user_activity():

    with open ("log.txt", "a") as file:
        content= file.write("User logged in \n")
    with open ("log.txt", "r") as file:
        content= file.read()
        print("\nFull log history:\n", content)

user_activity()