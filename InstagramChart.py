from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


URL = "https://www.instagram.com/{}/"


def scrape(username):
    fullUrl = URL.format(username)
    urlRead = urllib.request.urlopen(fullUrl).read()
    soup = BeautifulSoup(urlRead, 'html.parser')

    metaTag = soup.find('meta', attrs={'property': 'og:description'})
    text = metaTag.attrs['content']
    main_text = text.split("-")[0]

    return main_text

name = "eye.tattoo.girl"
data = scrape(name)
print(data)


objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(objects))
performance = [10,8,6,4,2,1]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Programming language usage')

plt.show()


















# import requests
# from bs4 import BeautifulSoup
#
# URL = "https://www.instagram.com/{}/"
#
#
# def scrape(username):
#     full_url = URL.format(username)
#     r = requests.get(full_url)
#     s = BeautifulSoup(r.text, "lxml")
#
#     tag = s.find("meta", attrs = {"name":"description"})
#     text = tag.attrs['content']
#     main_text = text.split("-")[0]
#
#     return main_text
#
#
# USERNAME = "eye.tattoo.girl"
# data = scrape(USERNAME)
# print(data)




