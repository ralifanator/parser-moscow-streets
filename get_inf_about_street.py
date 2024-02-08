from bs4 import BeautifulSoup
import requests


def get_house_numbers(req):
    soup = BeautifulSoup(req.text, "lxml")
    houses = soup.find("div", class_="dom_list")
    try:
        houses_list = map(lambda x: x.text, houses.contents)
    except:
        return []
    houses_list = filter(lambda x: x != '\n', houses_list)
    return list(houses_list)

def get_district(req):
    soup = BeautifulSoup(req.text, 'lxml')
    district = soup.find("div", class_="opis_ulica")
    district = district.findAll("a")
    try:
        district = list(map(lambda x: x.text, district))
    except:
        return []
    if len(district) == 1:
        district = district[0].split()[1:]

    return district

def get_crossroads(req):
    soup = BeautifulSoup(req.text, 'lxml')
    crossroads = soup.find("div", class_="cross_list")
    try:
        crossroads = filter(lambda x: x != '\n', crossroads.contents)
    except:
        return []
    crossroads_list = map(lambda x: x.a.text, crossroads)

    return list(crossroads_list)

def clean_string(s):
    symbols="'[]"
    s = s.replace("',", ";")
    for sym in symbols:
        s = s.replace(sym, "")
    return s

page = requests.get('https://ginfo.ru/ulicy/1-y_ternovyy_pereulok/')
print(get_house_numbers(page))