from tinydb import TinyDB, Query
import csv
from io import StringIO

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

    def toCsvDownload(self):
        f = StringIO()
        # with open('study_data.csv', mode='w') as studyFile:
        dataWriter = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # we must add a header dataWriter.writerow()
        for line in dataTable.all():
            dataWriter.writerow(line.values())
        return f.getvalue().encode('utf-8')

    def toCsvFile(self):
        with open('study_data.csv', mode='w') as studyFile:
            dataWriter = csv.writer(studyFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # we must add a header dataWriter.writerow()
            for line in dataTable.all():
                dataWriter.writerow(line.values())
                