# Sweetbot.py

from flask import Flask
from flask import request
from flask import json, jsonify

from sweet_logic import get_menu


app = Flask(__name__)

whole_menu = get_menu()

@app.route('/', methods=['POST'])
def index():
    return 'Hello World!'


@app.route('/keyboard', methods=['GET'])
def keyboard():

    data_select = {
        "type": "buttons",
        "buttons": ["오늘의 학식(죽전)", "오늘의 학식(천안)", "MS오피스 설치", "도움말"],
    }
    return jsonify(data_select)


@app.route('/message', methods=['POST'])
def message():

    data_receive = request.get_json()
    content = data_receive['content']

    if content == "오늘의 학식(죽전)":
        juk_menu = whole_menu['jukjeon']
        data_send = {
            "message": {
                "text": f"죽전, 오늘의 학식\n {juk_menu}"
            }
        }
        return jsonify(data_send)

    elif content == "오늘의 학식(천안)":
        chn_menu = whole_menu['cheonan']
        data_send = {
            "message": {
                "text": f"천안, 오늘의 학식\n {chn_menu}"
            }
        }
        return jsonify(data_send)

    elif content == "MS오피스 PC 설치":
        pc_link = 'http://cms.dankook.ac.kr/web/office'
        ios_link = 'https://itunes.apple.com/kr/developer/microsoft-corporation/id298856275'
        and_link = 'https://play.google.com/store/apps/dev?id=6720847872553662727'
        data_send = {
            "message": {
                "text": "Office365 설치를 위해, 단국대 학교 이메일과 패스워드를 알고 있어야 합니다!\n"
                        "최초로 부여받은 비밀번호(생년월일)의 경우 로그인이 불가하여\n"
                        "꼭! 비밀번호 변경 후 이용해주시길 바랍니다.\n"
                        "\n-PC설치방법-\n"
                        f"사이트: {pc_link}\n"
                        "오피스 포털 접속 -> Office364 포털 클릭 -> Office앱 설치\n",
                "message_button": {
                    'label': ['iOS 다운로드', 'Android 다운로드'],
                    'url': [ios_link, and_link]
                }
            }
        }
        return jsonify(data_send)

    elif content == "도움말":
        data_send = {
            "message": {
                "text": "피드백 보내기\n"
                        "E-mail : roamgom@gmail.com\n"
                        "SweetSoup(중고서적) : URL"
            }
        }
        return jsonify(data_send)


if __name__ == "__main__":
    print(whole_menu)
    app.run()
