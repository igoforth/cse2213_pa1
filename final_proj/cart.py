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
class Cart:


    def createCart(self,username):
        try:

            mycursor.execute("CREATE TABLE user_cart AS SELECT id,flag,%s FROM user",(username,))
            query = ["ALTER TABLE user_cart ADD product_id int(10)","ALTER TABLE user_cart ADD year int(5)",
                    "ALTER TABLE user_cart ADD title varchar(50)", "ALTER TABLE user_cart ADD genre varchar(30)",
                    "ALTER TABLE user_cart ADD price varchar(10)"]
            for each in query:
                mycursor.execute(each)
            query2 = "ALTER TABLE user_cart RENAME to {}_cart".format(username)
            mycursor.execute(query2)
        except:
            print("")

    def viewCart(self,username):
        try:
            mycursor.execute("select c.product_id, c.year, c.title, c.genre, c.price FROM {}_cart AS c, user AS u WHERE u.flag = c.flag")
        except:
            print()
            print("Cart is Empty")
