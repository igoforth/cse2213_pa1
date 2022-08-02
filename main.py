from database import Database


def main():
    with Database() as d:
        login = 1
        while login!= 0:
            print("\n1.Sign in"
            "\n2.Sign up"
            "\n3.Exit")
            answer = input("~~~:")

            if answer == "1":
                username = input("Enter in a username:~~~~")
                password = input("Enter in a password:~~~~")
                if len(d.userGet(username=username, password=password)) > 0:
                    print("Welcome back, {}!".format(username))
                    login = 0
                else:
                    print("Username or password is incorrect")
            elif answer =="2":
                username = input("Enter in a desired username:~~~~~")
                password = input("Enter in a desired password:~~~~~")
                d.userSet(username, password)
                print("Result is:", d.userGet(username=username, password=password))
            else:
                d.close()
                exit()

main()