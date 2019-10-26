from tinydb import TinyDB, Query
import csv
from io import StringIO

db = TinyDB('./db.json')
settingsTable = db.table('settings')
dataTable = db.table('data')

class Database:
    
    def getLocale(self):
        """
        will be implemented in the future to allow the user to choose the language
        """
        return 12

    def addDataToDatabase(self, surveyData):
        dataTable.insert(surveyData)

    def toCsvDownload(self):
        """
        returns all the data as a csv string which will then be downloaded to the users computer
        """
        f = StringIO()
        # with open('study_data.csv', mode='w') as studyFile:
        dataWriter = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # we must add a header dataWriter.writerow()
        for line in dataTable.all():
            dataWriter.writerow(line.values())
        return f.getvalue().encode('utf-8')

    def toCsvFile(self):
        with open('study_data.csv', mode='w') as studyFile:
            dataWriter = csv.writer(studyFile, dialect='excel')
            # adding the header
            dataWriter.writerow(["q1","q2","q3","q4","q5","q6","q7","q8","q9","q10","open1","open2","open3","open4","open5"])
            for line in dataTable.all():
                dataWriter.writerow(line.values())
                