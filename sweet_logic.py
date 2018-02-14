# sweet_logic.py

import requests
from bs4 import BeautifulSoup as bs
import datetime
import json


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
}

# jukjeon 555 56 57
# cheonan 560 61 62
total_menu = {}
jukjeon_menu = {}
jukjeon_cafe = []
cheonan_menu = {}
cheonan_cafe = []


def get_menu():

    # find day of the week
    def get_day():
        today = str(datetime.date.today().day)
        today_num = 0
        compare_days = []
        # only get day (ex: 2018-02-12 -> 12)
        print(f"Today : {today}")

        # get dates to compare
        html = requests.get('http://www.dankook.ac.kr/web/kor/-555', headers=headers).text
        soup = bs(html, 'lxml')

        # check day
        days = soup.select('#p_p_id_Food_WAR_foodportlet_ > div > div > div > form > div.food_list > table > tbody > tr > td > label > span.name_date')
        for i in days:
            compare_days.append(i.text.strip())
        print(compare_days)

        # find today as num, EX: 1 - Monday, 6 - Saturday
        for num, day in enumerate(compare_days, start=1):
            print(num, day)
            which_day = day.find(today)
            if which_day > 0:
                today_num = num
        return today_num

    # Jukjeon Campus
    def jukjeon_find_menu(today):
        # make Jukjeon cafeteria list
        html = requests.get('http://www.dankook.ac.kr/web/kor/-555', headers=headers).text
        soup = bs(html, 'lxml')

        cafeteria = soup.select('#p_p_id_TabMenu_WAR_tabMenuportlet_INSTANCE_cqhqkm0mCBIC_ > div > div > div > ul > li > a > span')
        for i in cafeteria:
            jukjeon_cafe.append(i.text.strip())
        print(f"Jukjeon Cafeteria: {jukjeon_cafe}")

        # get menu from Jukjeon cafeterias
        for i in range(555, 558):
            html = requests.get(f'http://www.dankook.ac.kr/web/kor/-{i}', headers=headers).text
            soup = bs(html, 'lxml')
            j_menu = soup.select(f'#p_p_id_Food_WAR_foodportlet_ > div > div > div > form > div.food_list > table > tbody > tr:nth-of-type({today}) > td:nth-of-type(2)')

            print(jukjeon_cafe[i-555])
            print(j_menu, end='\n\n')

            jukjeon_menu[jukjeon_cafe[i-555]] = j_menu[0].text.strip()

    # Cheonan Campus
    def cheonan_find_menu(today):
        # make cheonan cafeteria list
        html = requests.get('http://www.dankook.ac.kr/web/kor/-560', headers=headers).text
        soup = bs(html, 'lxml')

        cafeteria = soup.select('#p_p_id_TabMenu_WAR_tabMenuportlet_INSTANCE_tYzf2XU6dlSR_ > div > div > div > ul > li > a > span')
        for i in cafeteria:
            cheonan_cafe.append(i.text.strip())
        print(f"Cheonan Cafeteria: {cheonan_cafe}")

        # get menu from Cheonan cafeterias
        for i in range(560, 563):
            html = requests.get(f'http://www.dankook.ac.kr/web/kor/-{i}', headers=headers).text
            soup = bs(html, 'lxml')
            c_menu = soup.select(f'#p_p_id_Food_WAR_foodportlet_ > div > div > div > form > div.food_list > table > tbody > tr:nth-of-type({today}) > td:nth-of-type(2)')

            print(cheonan_cafe[i-560])
            print(c_menu, end='\n\n')

            cheonan_menu[cheonan_cafe[i-560]] = c_menu[0].text.strip()

    # load functions
    today_as_number = get_day()
    print(f"Today: {today_as_number}\n")

    print("Searching Jukjeon menu...\n")
    jukjeon_find_menu(today_as_number)

    print("Searching Cheonan menu...\n")
    cheonan_find_menu(today_as_number)

    # save as total menu with Jukjeon and Cheonan
    total_menu['jukjeon'] = jukjeon_menu
    total_menu['cheonan'] = cheonan_menu

    return total_menu

    # with open('menumenu.json', 'w', encoding='utf-8') as fp:
    #     json.dump(total_menu, fp, ensure_ascii=False)


# Start crawling Dankook Univ. Menu
if __name__ == "__main__":
    get_menu()
    print(total_menu)
