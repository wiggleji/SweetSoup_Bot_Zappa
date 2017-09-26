# sweet_logic.py

import requests
from bs4 import BeautifulSoup as bs



    # for i in menu_code:
    #     menu = bs(i.prettify().replace('<br/>', '\n'), 'html.parser')
    #     daily_menu = menu.text
    #     print(daily_menu)
    # ---- SAME ----

def get_menu():
    html = requests.get('https://portal.dankook.ac.kr/web/portal').text
    soup = bs(html, 'html.parser')
    daily_menu = soup.select('div.tab_content > div.tab_content')
    seperate_menu = []

    # print(daily_menu)

    for i in daily_menu:
        menu_info = bs(i.prettify().replace('<br/>','\n'), 'html.parser')
        infos = menu_info.select('div')
        for j in infos:
            print(j.text)

get_menu()