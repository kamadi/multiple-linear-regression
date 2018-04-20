from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

almaty = "https://krisha.kz/prodazha/kvartiry/almaty/"
almaly = 'https://krisha.kz/prodazha/kvartiry/almaty-almalinskij/'


def num(s):
    try:
        return int(s)
    except ValueError:
        return int(float(s))


with open('index.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for i in range(1, 500):
        if i == 1:
            url = almaly
        else:
            url = almaly + "?page=" + str(i)

        html = urlopen(url)

        t = html.read().decode('utf-8')

        soup = BeautifulSoup(t, "html.parser")

        cards = soup.find_all("div", {"class": "a-card"})

        for card in cards:
            try:
                a = card.find("a", {"class", "a-card__title"})
                c = a.text.split(",")
                room = c[0][0]
                size = c[1][:-2].replace(' ', '')
                floors = c[2][:-3].replace(' ', '').split("/")
                if len(floors) == 2:
                    div = card.find("div", {"class", "a-card__price"})
                    price = div.get_text().strip().replace(' ', '')[:-1]

                    text_preview = card.find("div", {'class', 'a-card__text-preview'})
                    text_preview = text_preview.text.strip().split(',')
                    for t in text_preview:
                        if 'г.п.' in t:
                            year = t[:-4]
                            print(c, "room:", int(room), 'size:', size, 'year:', year, "floor:",floors[0],"top_floor:", floors[1],"price:", int(price))
                            writer.writerow([num(size), int(room), int(year), int(floors[0]), int(floors[1]), int(price)])


            except ValueError:
                print("error")
            except IndexError:
                print("error")
