"use strict";

const MONGO_ID = "634af07248a321b8c5475e7f"
const MONGO_KEY = "bfFfyFERzLuUKXzGofdSRqBaODyOARolgQjyveuTo5EuhIerYL5UknSwAG3ZLMGo"

// function getMongo() {
//     var data = JSON.stringify({
//         "collection": "test_project",
//         "database": "masterDB",
//         "dataSource": "input",
//         "projection": {
//             "_id": 1
//         }
//     });
                
//     var config = {
//         method: 'post',
//         url: 'https://data.mongodb-api.com/app/data-cxjvq/endpoint/data/v1/action/findOne',
//         headers: {
//         'Content-Type': 'application/json',
//         'Access-Control-Allow-Origin': '*',
//         'Access-Control-Request-Headers': '*',
//         'api-key': MONGO_KEY,
//         'Accept': 'application/ejson'
//         },
//         data: data
//     };
                
//     axios(config)
//         .then(function (response) {
//             console.log(JSON.stringify(response.data));
//         })
//         .catch(function (error) {
//             console.log(error);
//         });
// }

// function getMongo() {
//     let action = "/action/findOne"
//     let baseUrl = `https://data.mongodb-api.com/app/data-cxjvq/endpoint/data/v1${action}`

//     $.ajax(baseUrl, {
//         dataType: 'json',
//         type: 'POST',
//         crossDomain: true,
//         data: {
//             'dataSource': 'input',
//             'database': 'masterDB',
//             'collection': 'test project',
//             'document': {
//                 "name": "John Sample",
//                 "age": 69,
//             }
//         },
//         headers: {
//             //'Authorization': 'Bearer ' + accessToken
//             'api-key': MONGO_KEY,
//             // 'Access-Control-Allow_Headers': '*',
//             'Content-Type': 'application/json',
//         },
//         success: function(r) {
//             console.log("Request Worked " + JSON.stringify(r));
//             // resolve(r);
//         },
//         error: function(err) {
//             console.log("Request Failed " + JSON.stringify(err));
//             // reject(err);
//         }
//     })
// }

