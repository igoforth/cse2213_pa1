import mysql.connector
import sys
from user import *

mydb = mysql.connector.connect(
    user="root",
    password="",
    host="localhost",
    database="methods"
)

mycursor = mydb.cursor()
class Cart:#cart class

    #function creates the cart for each user after user creation
    #creates it as user_cart then changes the name
    def createCart(self,username):
        try:
            #creates cart with information from their user table
            #takes the specific user id and flag id from the table
            #flag attribute was used for distinction purposes, but almost serves no purpose at the moment
            mycursor.execute("CREATE TABLE user_cart AS SELECT id,flag FROM user")
            query = ["ALTER TABLE user_cart ADD product_id int(10)","ALTER TABLE user_cart ADD year int(5)",
                    "ALTER TABLE user_cart ADD title varchar(50)", "ALTER TABLE user_cart ADD genre varchar(30)",
                    "ALTER TABLE user_cart ADD price float(10)", "ALTER TABLE user_cart ADD item varchar(10)"]
            for each in query:
                mycursor.execute(each)
            query2 = "ALTER TABLE user_cart RENAME to {}_cart".format(username)
            #changes cart name to {username}_cart for easy distinction
            mycursor.execute(query2)
        except:
            print("")

    #allows user (after signed in) to view their cart
    def viewCart(self,username):
        try:
            #selects everything in cart besides the first row
            #this method is only good for 1 user
            #if another user is added, it pulls all id from the user table, therefore creating viewing errors when viewing the 2nd+ user carts
            mycursor.execute("SELECT product_id,year,title,genre,price,item FROM {}_cart WHERE id != 1".format(username))
            all_cart = mycursor.fetchall()
            for each in all_cart:
                print(each)
            in5 = input("\nRemove from cart?(y/n) ")

            if (in5 == 'y'):
                print("1.Book")
                print("2.Movie")
                in8 = input("What type do you want to remove? ")
                if(in8 == "1"):
                    try:
                        #selects books specifically from cart
                        mycursor.execute("SELECT product_id,year,title,genre,price,item FROM {}_cart WHERE item = 'book'".format(username))
                        book_order = mycursor.fetchall()
                        for each in book_order:
                            print(each)
                        in6 = input("What id would you like to remove? ")
                        mycursor.execute("INSERT INTO books (product_id,year,title,genre,price,item) SELECT product_id,year,title,genre,price,item FROM {}_cart WHERE product_id=%s AND item='book'".format(username),(in6,))
                        mycursor.execute("DELETE FROM {}_cart WHERE product_id=%s".format(username),(in6,))
                        mydb.commit()
                        print("Item Removed")
                    except:
                        print()
                        print("Cart is Empty")

                if(in8 == "2"):
                    try:
                        #selects movies specifically from cart
                        mycursor.execute("SELECT product_id,year,title,genre,price,item FROM {}_cart WHERE item = 'movie'".format(username))
                        movie_order = mycursor.fetchall()
                        for each in movie_order:
                            print(each)
                        in6 = input("What id would you like to remove? ")
                        mycursor.execute("INSERT INTO movies (product_id,year,title,genre,price,item) SELECT product_id,year,title,genre,price,item FROM {}_cart WHERE product_id=%s AND item='movie'".format(username),(in6,))
                        mycursor.execute("DELETE FROM {}_cart WHERE product_id=%s".format(username),(in6,))
                        mydb.commit()
                        print("Item Removed")
                    except:
                        print()
                        print("Cart is Empty")

            elif(in5 == 'n'):
                print()
        except:
            print()
            print("\nCart is Empty!")





    def addtoCart(self, username):
        in4 = input("Enter 1 or 2: ")
        if (in4 == '1'):
            try:#displays all from books
                mycursor.execute("SELECT * FROM books")
            except:
                mycursor.execute("SELECT * FROM books")
            books = mycursor.fetchall()
            for each in books:
                print(each)
            mydb.commit()
            id_num = input("Enter the id you want to buy: ")
            #inserts almost all attributes into the specific user cart -> determined by who is signed in
            mycursor.execute("INSERT INTO {}_cart (product_id, year, title, genre, price,item) SELECT product_id,year,title,genre,price,item FROM books WHERE product_id=%s".format(username),(id_num,))
            mycursor.execute("DELETE FROM books WHERE product_id=%s",(id_num,))
            print("\nItem added to cart")
            mydb.commit()
        if (in4 == '2'):
            try:
                mycursor.execute("SELECT * FROM movies")
            except:
                mycursor.execute("SELECT * FROM movies")
            movies = mycursor.fetchall()
            for each in movies:
                print(each)
            mydb.commit()
            id_num = input("Enter the id you want to buy: ")
            mycursor.execute("INSERT INTO {}_cart (product_id, year, title, genre, price,item) SELECT product_id,year,title,genre,price,item FROM movies WHERE product_id=%s".format(username),(id_num,))
            mycursor.execute("DELETE FROM movies WHERE product_id=%s",(id_num,))
            print("\nItem added to cart.")
            mydb.commit()


    def checkOut(self,username):
    #    try:
            #selects all items that aren't related to the initial creation of the table
            #same problem from view cart applies here
            mycursor.execute("SELECT product_id,year,title,genre,price,item FROM {}_cart WHERE id != 1".format(username))
            all_cart = mycursor.fetchall()
            for each in all_cart:
                print(each)

            in7 = input("\nCheckout?(y/n) ")
            if(in7 == 'y'):
                try: #deletes all from cart to show purchasing
                    mycursor.execute("DELETE FROM {}_cart WHERE id != 1".format(username))
                    print("Sold!")
                    mydb.commmit()
                except:
                    print()
            else:
                print()
        #except:
        #    print()
        #    print("Cart is Empty")
