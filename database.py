import json

def initialize():
    return

def database(mode, data):
    modes = ["user", "pay", "cart", "catalog", "history", "shipping"]
    return

def catalogGet():
    catalog = open("database/catalog.txt", "r")
    for line in catalog.readline():
        
        return
    catalog.close()

def catalogSet(id, name, price, category):
    catalog = open("database.json", "w")
    catalog.write(id + " " + name + " " + price + " " + category)
    catalog.close()

class Item:
    def __init__(self, id, name, price, category):
        self.id = id
        self.name = name
        self.price = price
        self.category = category