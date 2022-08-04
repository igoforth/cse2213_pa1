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

    #def __init__(self, id, title):
        #self.id = id
    #    self.year = year
        #self.title = title
    #    self.production_company = production_company
    #    self.genre = genre


    def createTable(self):
        try:#creates moview table upon trying to view
            mycursor.execute("CREATE TABLE movies (product_id int(11) PRIMARY KEY AUTO_INCREMENT, year smallint UNSIGNED, title varchar(40), production_company varchar(40), genre varchar(30), price float(10), item varchar(8))")

            #populates movie table
            query = "INSERT INTO movies(year, title, production_company, genre, price, item) VALUES(%s, %s, %s, %s, %s, %s)"
            data = [
                    ("2017", "A Cure for Wellness", "Twentieth Century Fox", "Drama", "10.99", "movie"),
                    ("2013", "A Haunted House", "Open Road Films", "Comedy", "7.99", "movie"),
                    ("2018", "A Quiet Place", "Paramount Pictures", "Horror", "12.99", "movie"),
                    ("2022", "Elvis", "Warner Bros.", "Drama", "15.99", "movie"),
                    ("2021", "Candyman", "Universal Pictures", "Horror", "12.99", "movie"),
                    ("2016", "Captain America: Civil War", "Walt Disney Studios", "Action/Adventure", "7.99", "movie"),
                    ("2012", "Ice Age: Continetal Drift", "Twentieth Century Fox", "Animation/Adventure", "25.99", "movie"),
                    ("2015", "Goosbumps", "Sony Pictures Entertainment", "Family/Horror", "10.99", "movie"),
                    ("2015", "Daddy's Home", "Paramount Pictures", "Comedy", "7.99", "movie"),
                    ("2015", "Jurassic World", "Universal Pictures", "Thriller", "14.99", "movie")
                    ]

            mycursor.executemany(query, data)
            mydb.commit()
        except:
            print("")






    def viewTable(self):
        #try:
        #viewing the table
        mycursor.execute("SELECT * FROM movies")
        movies = mycursor.fetchall()
        for each in movies:
            print(each)
        mydb.commit()
        #except:
            #print("Sold Out")
