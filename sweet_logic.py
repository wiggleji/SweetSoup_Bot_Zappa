# sweet_logic.py

import requests
from bs4 import BeautifulSoup as bs


def get_menu():
    html = requests.get('https://portal.dankook.ac.kr/web/portal').text
    soup = bs(html, 'html.parser')
    daily_menu = soup.select('div.tab_content > div.tab_content')
    # j_teacher, j_student, j_dorm, c_teacher, c_student, c_dorm = []
    menu_list = []

    # Insert Menu to list by splitting in ', '
    for i in daily_menu:
        menu_info = i.text.split(', ')
        menu_list.append(menu_info)

    for j in menu_list:
        for i in j:
            print(i)
            print()

get_menu()
