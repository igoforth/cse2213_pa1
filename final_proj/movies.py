import mysql.connector
import sys


mydb = mysql.connector.connect(
    user="root",
    password="",
    host="localhost",
    database="methods"
)
mycursor = mydb.cursor()
class Movies:

    #def __init__(self, id, year, title, production_company, genre):
    #    self.id = id
    #    self.year = year
    #    self.title = title
    #    self.production_company = production_company
    #    self.genre = genre


    def createTable():
        try:

            mycursor.execute("CREATE TABLE movies (id int(11) PRIMARY KEY AUTO_INCREMENT, year smallint UNSIGNED, title varchar(40), production_company varchar(40), genre varchar(30), price varchar(10))")
        except:
            print()

    def insertTable():
        try:
            query = "INSERT INTO movies(year, title, production_company, genre, price) VALUES(%s, %s, %s, %s, %s)"
            data = [
                ("2017", "A Cure for Wellness", "Twentieth Century Fox", "Drama", "$10.99"),
                ("2013", "A Haunted House", "Open Road Films", "Comedy", "$7.99"),
                ("2018", "A Quiet Place", "Paramount Pictures", "Horror", "$12.99"),
                ("2022", "Elvis", "Warner Bros.", "Drama", "$15.99"),
                ("2021", "Candyman", "Universal Pictures", "Horror", "$12.99"),
                ("2016", "Captain America: Civil War", "Walt Disney Studios", "Action/Adventure", "$7.99"),
                ("2012", "Ice Age: Continetal Drift", "Twentieth Century Fox", "Animation/Adventure", "$25.99"),
                ("2015", "Goosbumps", "Sony Pictures Entertainment", "Family/Horror", "$10.99"),
                ("2015", "Daddy's Home", "Paramount Pictures", "Comedy", "$7.99"),
                ("2015", "Jurassic World", "Universal Pictures", "Thriller", "$14.99")
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
