def main():
    login =1
    while login!= 0:
        print("\n1.Sign in"
        "\n2.Sign up"
        "\n3.Exit")
        answer = input("~~~:")

        if answer == "1":
            username = input("Enter in a username:~~~~")
            password = input("enter in a password:~~~~")
            #if username = a username and if password = a password
                #login = 0
                #app.py
        elif answer =="2":
                username = input("Enter in a desired username:~~~~~")
                password = input("Enter in a desired password:~~~~~")
        else:
            exit()

main()