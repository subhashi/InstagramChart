from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


IGURL = "https://www.instagram.com/{}/"


def findDataInIG(igAccountName):
    fullUrl = IGURL.format(igAccountName)
    urlRead = urllib.request.urlopen(fullUrl).read()
    soup = BeautifulSoup(urlRead, 'html.parser')

    metaTag = soup.find('meta', attrs={'name': 'description'})
    numericValues = findNumbers(metaTag)

    return numericValues


def findNumbers(metaTag):
    rawText = metaTag.attrs['content']
    dataTextList = (rawText.split("-")[0]).split(" ")
    numericValues = []

    for i in dataTextList:
        if str.isdigit(i):
            numericValues.append(int(i))

    return numericValues

# def drawBarChart():

IGACCOUNTNAME = "eye.tattoo.girl"

X_data = ("Followers", "Following", "Posts")
y_data = findDataInIG(IGACCOUNTNAME)
y_pos = np.arange(len(X_data))

plt.bar(y_pos, y_data, align='center', alpha=0.5)
plt.xticks(y_pos, X_data)
plt.ylabel('Count')
plt.title('Your Instagram Account Info')

plt.show()




# objects = ('Followers', 'Following', 'Posts')
# y_pos = np.arange(len(objects))
# performance = [10,8,6,4,2,1]
#
# plt.bar(y_pos, performance, align='center', alpha=0.5)
# plt.xticks(y_pos, objects)
# plt.ylabel('Usage')
# plt.title('Programming language usage')
#
# plt.show()


















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




