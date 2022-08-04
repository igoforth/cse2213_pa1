

import mysql.connector
import sys

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

print("You got here!")
