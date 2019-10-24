from tinydb import TinyDB, Query

db = TinyDB('./db.json')
settings = db.table('settings')

class Database:
    def hello():
        print(1)