import pprint
from bs4 import BeautifulSoup
import requests
import re

res = requests.get('https://news.ycombinator.com/front')
res2 = requests.get('https://news.ycombinator.com/front?day=2024-05-20&p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
links = soup.select('.titleline')
links2 = soup2.select('.titleline')
votes = soup.select('.score')
votes2 = soup2.select('.score')

mass_links = links + links2
mass_votes = votes + votes2


def sort_stories_by_votes(li):
    pprint.pprint(sorted(li, key=lambda k: k['points'], reverse=True))


def custom_news(links, votes):
    global href_link
    hn = []
    for inx, item in enumerate(links):
        if votes:
            points = votes[inx].getText()
            points_adjusted = int(re.sub("[A-Za-z]", "", points))
            title = links[inx].getText()
            href = links[inx].select('a', href=True)
            for a in href:
                if 'https' in a['href']:
                    href_link = (a['href'])
            if points_adjusted > 99:
                hn.append({'title': title, 'link': href_link, 'points': points_adjusted})
        else:
            pass
    return sort_stories_by_votes(hn)

custom_news(mass_links,mass_votes)










