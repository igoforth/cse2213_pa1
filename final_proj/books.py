import mysql.connector
import sys


mydb = mysql.connector.connect(
    user="root",
    password="",
    host="localhost",
    database="methods"
)
mycursor = mydb.cursor()
class Books:

    #def __init__(self, id, year, title, production_company, genre):
    #    self.id = id
    #    self.year = year
    #    self.title = title
    #    self.production_company = production_company
    #    self.genre = genre


    def createTable(self):
        try:
            mycursor.execute("CREATE TABLE books (id int(11) PRIMARY KEY AUTO_INCREMENT, year smallint UNSIGNED, title varchar(40), author varchar(40), genre varchar(30), price float(10), item varchar(8))")

            query = "INSERT INTO books(year, title, author, genre, price, item) VALUES(%s, %s, %s, %s, %s, %s)"
            data = [
                ("1614", "The Odyssey", "Homer", "Epic Poetry", "18.99", "book"),
                ("1995", "The Lost World", "Michael Crichton", "Science-Fiction", "6.99", "book"),
                ("1864", "Journey to the Center of the Earth", "Jules Verne", "Science-Fiction", "12.99", "book"),
                ("1892", "Sherlock Holmes", "Arthur Conan Doyle", "Mystery", "11.99", "book"),
                ("1960", "To Kill a Mockingird", "Harper Lee", "Coming-of-age", "12.99", "book"),
                ("1925", "The Great Gatsby", "F.Scott Fittzgerald", "Tragedy", "17.99", "book"),
                ("1987", "Beloved", "Toni Morrison", "American Literature", "25.99", "book"),
                ("1600", "Hamlet", "William Shakespeare", "Tragedy", "15.99", "book"),
                ]

            mycursor.executemany(query, data)
            mydb.commit()
        except:
            print("")


    def viewTable(self):
        #try:
        mycursor.execute("SELECT * FROM books")
        books = mycursor.fetchall()
        for each in books:
            print(each)
        mydb.commit()
        #except:
            #print("Sold Out")
