from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
# from flask import Flask, url_for, render_template, send_from_directory

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run()



MONGO_ID = "634af07248a321b8c5475e7f"
MONGO_KEY = "bfFfyFERzLuUKXzGofdSRqBaODyOARolgQjyveuTo5EuhIerYL5UknSwAG3ZLMGo"
MONGO_CLUSTER = "input"

client = MongoClient("mongodb+srv://umec2022:SteeledWharfBackback12@input.awyknuf.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
db = client.masterDB
collection = db.test_project

class mainProject:

    def __init__ (self, mainName, description):
        self.mainName = mainName
        self.description = description 

    def getMainName(self):
        return self.mainName

    def getDescription(self):
        return self.description 

project1 = mainProject("Building A Table", "Building a table for my father")       
project = {"mainproject": project1.getMainName(),
           "description": project1.getDescription()}

test_project_id = collection.insert_one(project).inserted_id
test_project_id.ObjectId('1')
