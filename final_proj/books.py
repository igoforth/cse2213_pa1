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


    def createTable():
        try:

            mycursor.execute("CREATE TABLE books (id int(11) PRIMARY KEY AUTO_INCREMENT, year smallint UNSIGNED, title varchar(40), author varchar(40), genre varchar(30), price varchar(10))")
        except:
            print()

    def insertTable():
        try:
            query = "INSERT INTO movies(year, title, author, genre, price) VALUES(%s, %s, %s, %s, %s)"
            data = [
                ("1614", "The Odyssey", "Homer", "Epic Poetry", "$18.99"),
                ("1995", "The Lost World", "Michael Crichton", "Science-Fiction", "$6.99"),
                ("1864", "Journey to the Center of the Earth", "Jules Verne", "Science-Fiction", "$12.99"),
                ("1892", "Sherlock Holmes", "Arthur Conan Doyle", "Mystery", "$11.99"),
                ("1960", "To Kill a Mockingird", "Harper Lee", "Coming-of-age", "$12.99"),
                ("1925", "The Great Gatsby", "F.Scott Fittzgerald", "Tragedy", "$17.99"),
                ("1987", "Beloved", "Toni Morrison", "American Literature", "$25.99"),
                ("1600", "Hamlet", "William Shakespeare", "Tragedy", "$15.99"),
                ]

            mycursor.executemany(query, data)
            mydb.commit()
        except:
            print()


    def viewTable(self):
        #try:
            mycursor.execute("SELECT year, title, production_company, genre, price FROM movies")
            mydb.commit()
        #except:
            #print("Sold Out")
