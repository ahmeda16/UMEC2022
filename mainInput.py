from lib.pymongo import MongoClient


class mainProject:

    def __init__ (self, mainName, description):
        self.mainName = mainName
        self.description = description 

    def getMainName(self):
        return self.mainName

    def getDescription(self):
        return self.description
        
