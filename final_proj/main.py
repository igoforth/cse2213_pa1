import mysql.connector
import sys
import user
import cart
import movies
import books


try:
    mydb = mysql.connector.connect(
        user="root",
        password="",
        host="localhost",
        database="methods"
    )

    print("Successful connection.")

except:
    print("Failed connection.")
    sys.exit()
mycursor = mydb.cursor()


def main():
    u_name = ''
    p_word = ''
    f_name = ''
    l_name = ''
    u = user.User(u_name, p_word,f_name, l_name)
    c = cart.Cart()

    flag = True
    while (flag == True):
        print()
        print("Welcome to the shop.")
        print()
        print("1.Create User")
        print("2.Sign in")
        print("3.Exit")
        print()
        try:
            in1 = input("Enter here (1,2 or 3): ")
        except:
            print("ERROR: Invalid Entry.")

        if (in1 == '1'):
            flag = True
            u_name = str(input("Enter a username: "))
            p_word = str(input("Enter a password: "))
            f_name = str(input("Enter your first name: "))
            l_name = str(input("Enter your last name: "))

            u.createUser(u_name, p_word, f_name, l_name)
            c.createCart(u_name)

            in2 = str(input("Would you like to continue? (y/n) "))
            if (in2 == 'y'):
                continue
            if(in2 == 'n'):
                flag = False
                print("Come again!")
                exit()

        if (in1 == '2'):
            u_name = str(input("Enter a username: "))
            p_word = str(input("Enter a password: "))
            if(u.sign_in_User(u_name,p_word) == True):
                print("Thank you for joining us.")
                flag2 = True
                m = movies.Movies()
                b = books.Books()
                while(flag2 == True):

                    print()
                    print("1.View Cart")
                    print("2.View Books")
                    print("3.View Movies")
                    print("4.Add items to cart")
                    print("5.Log out")
                    print()

                    try:
                        in3 = input("Enter here (1,2,3..): ")
                    except:
                        print("ERROR: Invalid Entry.")

                    if(in3 =='1'):
                        c.viewCart(u_name)
                    if(in3 == '2'):
                        b.createTable()
                        b.viewTable()
                    if(in3 == '3'):
                        m.createTable()
                        m.viewTable()
                    if(in3 == '4'):
                        print()
                    if(in3 == '5'):
                        flag2 == False
                        print("Come again!")
                        u.sign_out_User()
                        mycursor.close()
                        mydb.close()
                        exit()





        if(in1 == '3'):
            flag = False
            print("Come again!")
            mycursor.close()
            mydb.close()
            exit()





main()
