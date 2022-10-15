"use strict";

const MONGO_ID = "634af07248a321b8c5475e7f"
const MONGO_KEY = "bfFfyFERzLuUKXzGofdSRqBaODyOARolgQjyveuTo5EuhIerYL5UknSwAG3ZLMGo"

function getMongo() {
    let action = "/action/findOne"
    let baseUrl = `https://data.mongodb-api.com/app/${MONGO_ID}/endpoint/data/v1${action}`

    $.ajax("https://api.spotify.com/v1" + baseUrl, {
        dataType: 'json',
        type: 'POST',
        data: {
            'dataSource': 'input',
            'database': 'masterDB',
            'collection': 'test project',
            'document': {
                "name": "John Sample",
                "age": 69,
            }
        },
        headers: {
            //'Authorization': 'Bearer ' + accessToken
            'Access-Control-Allow_Headers': '*',
            'Content-Type': 'application/json',
            'api-key': MONGO_KEY,
        },
        success: function(r) {
            console.log("Request Worked " + JSON.stringify(r));
            // resolve(r);
        },
        error: function(err) {
            console.log("Request Failed " + JSON.stringify(err));
            // reject(err);
        }
    })
}