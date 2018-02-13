# Sweetbot.py

import os
import requests
import json


@app.route('/', methods=['POST'])
def index():
    return 'Hello World!'

@app.route('/keyboard', methods=['GET'])
def Keyboard():

    dataSelect = {
        "type": "buttons",
        "buttons" : ["오늘의 학식", "MS오피스 설치", "중고서적(추가예정)", "도움말"],
    }
    return jsonify(dataSelect)

@app.route('/message', methods=['POST'])
def Message():

    dataReceive = request.get_json()
    content = dataReceive['content']

    if content == "오늘의 학식":
        dataSend = {
            "message": {
                "text": "학식 list"   #not yet
            }
        }
    elif content == "MS오피스 설치":
        dataSend = {
            "message": {
                "text": "오피스 설치 url" #not yet
            }
        }
    elif content == "중고서적":
        dataSend = {
            "message": {
                "text": "SweetSoup 연결" #not yet
            }
        }
    elif content == "도움말":
        dataSend = {
            "message": {
                "text": "피드백 보내기\n"
                        "E-mail : roamgom@gmail.com\n"
                        "SweetSoup(중고서적) : URL"
            }
        }

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 8020)
