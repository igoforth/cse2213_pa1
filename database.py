import os
import io
import json
import jsonpickle

class Database:
    def __init__(self):
        self.file = open("database/database.json", "w")
        self.users = {}
        self.catalog = Catalog()
    
    def __enter__(self):
        if os.stat("database/database.json").st_size != 0:
                self = jsonpickle.decode(self.file.read())
        return self

    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        try:
            self.file.write(jsonpickle.encode(self))
        except Exception as e:
            print("Error writing to database: {}".format(e))
            return False
        self.file.close()

    def userGet(self, username="", password=""):
        result = {}
        for key, value in self.users.items():
            if key == username or value.password == password:
                result[key] = value
        return result

    def userSet(self, username, password):
        self.users[username] = User(password)

class Catalog():
    def __init__(self):
        self.items = {}

    def itemGet(self, id=None, name="", price="", category=""):
        result = {}
        for key, value in self.items.items():
            if key == id or value.name == name or value.price == price or value.category == category:
                result[key] = value
        return result

    def itemSet(self, id, name, price, category):
        self.items[id] = Item(name, price, category)

class User():
    def __init__(self, password):
        self.password = password
        self.cart = Cart()
        self.history = History()

    def shippingGet(self):
        return self.shipping

    def shippingSet(self, street, state, city, zip):
        self.shipping = Ship(street, state, city, zip)

    def paymentGet(self):
        return self.payment

    def paymentSet(self, card_num, exp_date, csv):
        self.payment = Pay(card_num, exp_date, csv)

class Ship():
    def __init__(self, street, state, city, zip):
        self.street = street
        self.state = state
        self.city = city
        self.zip = zip

class Pay():
    def __init__(self, card_num, exp_date, csv):
        self.card_num = card_num
        self.exp_date = exp_date
        self.csv = csv

class Cart():
    def __init__(self):
        self.items = []
    
    def itemsGet(self):
        return self.items

    def itemSet(self, name, price, category):
        self.items.append(Item(name, price, category))

class History():
    def __init__(self):
        self.items = []
    
    def itemsGet(self):
        return self.items

    def itemSet(self, id, name, price, category):
        self.items.append(Item(id, name, price, category))

class Item():
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category