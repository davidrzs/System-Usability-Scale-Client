from tinydb import TinyDB, Query

db = TinyDB('./db.json')
settingsTable = db.table('settings')
dataTable = db.table('data')

class Database:
    
    def addDataToDatabase(self, surveyData):
        dataTable.insert(surveyData)

    def resetStudy(self):
        pass

    def getAllData(self):
        print(dataTable.all())