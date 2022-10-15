
from flask import Flask, url_for, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()


#from lib.pymongo import MongoClient

# import pymongo
# from pymongo import MongoClient
# from lib.pymongo.main import MongoClient
# from pyodide.http import pyfetch
# import asyncio

MONGO_ID = "634af07248a321b8c5475e7f"
MONGO_KEY = "bfFfyFERzLuUKXzGofdSRqBaODyOARolgQjyveuTo5EuhIerYL5UknSwAG3ZLMGo"
MONGO_CLUSTER = "input"


class mainProject:

    def __init__ (self, mainName, description):
        self.mainName = mainName
        self.description = description 

    def getMainName(self):
        return self.mainName

    def getDescription(self):

        return self.description
        

        return self.getDescription




# import requests
# import json

# def getMongo():
#     url = "https://data.mongodb-api.com/app/data-cxjvq/endpoint/data/v1/action/findOne"
#     payload = json.dumps({
#         "collection": "test_project",
#         "database": "masterDB",
#         "dataSource": "input",
#         "projection": {
#             "_id": 1
#         }
#     })
#     headers = {
#     'Content-Type': 'application/json',
#     'Access-Control-Request-Headers': '*',
#     'api-key': MONGO_KEY,
#     'Accept': 'application/ejson' 
#     }
#     response = requests.request("POST", url, headers=headers, data=payload)
# print(response.text)


# from js import XMLHttpRequest
# async def getSpotify():
#     url = "https://jsonplaceholder.typicode.com/todos/1" #"https://www.adafruit.com/api/quotes.php"
#     # response = await pyfetch(url=url, method="GET")
#     # pyscript.write(f"status: {response.status}, json: {await response.json()}")

#     req = XMLHttpRequest.new()
#     req.open("GET", url, False)
#     req.send(None)
#     print(str(req.response))

# async def getMongo():
#     action = "/action/findOne"
#     baseUrl = f"https://data.mongodb-api.com/app/{MONGO_ID}/endpoint/data/v1" + action

#     req = XMLHttpRequest.new()
#     req.open("POST", baseUrl, False)
#     req.setRequestHeader("Content-Type", "application/json")
#     req.setRequestHeader("Access-Control-Allow_Origin", "False")
#     req.setRequestHeader("api-key", MONGO_KEY)
#     body = {
#         "dataSource": MONGO_CLUSTER,
#         "database": "masterDB",
#         "collection": "test project",
#         #"filter": {"name": "John Sample"}
#     }
#     req.send(body)
#     print(str(req.response))

def printme():
    print("WOWW")
