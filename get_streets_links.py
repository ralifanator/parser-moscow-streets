from bs4 import BeautifulSoup
import requests

def write_streets_links(streets, file):
    
    with open(file, 'w') as f:
        for i in range(len(streets['names'])):
            s = f"{streets['names'][i]};{streets['urls'][i]}\n"
            f.write(s)
        
def parse_streets():
    url = 'https://ginfo.ru/ulicy/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "lxml")
    streets = soup.findAll("div", class_="street_unit")
    streets_names = [street.a.text for street in streets]
    streets_urls = [street.a['href'] for street in streets]

    print(streets_names)
    print(streets_urls)
    return {'names' : streets_names, 'urls' : streets_urls}





#write_streets_links(parse_streets(), 'streets_urls.txt')

        
