import mysql.connector
import sys
from movies import *
from books import *

mydb = mysql.connector.connect(
    user="root",
    password="",
    host="localhost",
    database="methods"
)

mycursor = mydb.cursor()

class User:
    def __init__(self, username,p_word, first_name, last_name):
        self.username = username
        self.p_word = p_word
        self.first_name = first_name
        self.last_name = last_name



    def createUser(self,username, p_word, first_name, last_name):

        try:
            mycursor.execute("CREATE TABLE user (id int(8) PRIMARY KEY AUTO_INCREMENT, username varchar(20),p_word varchar(30), first_name varchar(10), last_name varchar(10),flag int(5))")
        except:
            print()
        #checks if username exists already
        mycursor.execute("SELECT username FROM user WHERE username=%s",(username,))
        check = mycursor.fetchone()
        try:
            if check[0] != username:
                query = ("INSERT INTO user (username, p_word, first_name, last_name) VALUES (%s,%s,%s,%s)")
                data = (username, p_word, first_name,last_name)
                mycursor.execute(query, data)
                mydb.commit()
                print("Username added!")
            else:
                print("Username already exists!")
        except TypeError:
            query = ("INSERT INTO user (username, p_word, first_name, last_name) VALUES (%s,%s,%s,%s)")
            data = (username, p_word, first_name,last_name)
            mycursor.execute(query, data)
            mydb.commit()
            print("Username added!")





    def sign_in_User(self,username, p_word):
        sign_flag = False
        mycursor.execute("SELECT username,p_word FROM user WHERE username=%s AND p_word =%s",(username, p_word))
        check = mycursor.fetchone()
        if check[0] == username and check[1] == p_word:
            print("Signed in")
            mycursor.execute("UPDATE user SET flag='1' WHERE username=%s",(username,))
            mydb.commit()
            sign_flag = True
            return sign_flag
        if check[0] == username and check[1] != p_word:
            print("Incorrect username or password!")
            sign_flag = False
            return sign_flag
        if check[0] != username and check[1] == p_word:
            print("Incorrect username or password")
            sign_flag = False
            return sign_flag
        if check[0] != username and check[1] != p_word:
            print("Account does not exist")
            sign_flag = False
            return sign_flag

        def sign_out_User():
            mycursor.execute("UPDATE user SET flag='0' WHERE username=%s",(username,))
            mydb.commit()
