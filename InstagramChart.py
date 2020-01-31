#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Instragram Data to Chart
    Draw a bar chart of a given public Instagram account

    **Note: Only works for public accounts
"""

from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

# Find followers,  following and posts of a given public Instagram account
def findDataInIg(igAccountName):

    # Get the script of the given account URL
    IGURL = "https://www.instagram.com/{}/"
    fullUrl = IGURL.format(igAccountName)
    urlRead = urllib.request.urlopen(fullUrl).read()
    soup = BeautifulSoup(urlRead, 'html.parser')

    # Fetch followers,  following and posts data from the script
    metaTag = soup.find('meta', attrs={'name': 'description'})
    rawText = metaTag.attrs['content']
    dataTextList = (rawText.split("-")[0]).split(" ")

    fetched = []

    # Get only the numeric data fields of followers,  following and posts data
    followers = dataTextList[0]
    following = dataTextList[2]
    posts = dataTextList[4]

    fetched.append(followers)
    fetched.append(following)
    fetched.append(posts)

    return fetched


# If the numeric values contain m, k or ',', convert them to int values
def cleanNumbers(numericValue):

    if ',' in numericValue:
        numericValue = numericValue.replace(',', '')

    if "m" in numericValue:
        numericValue = numericValue.replace('m', '')

        numericValue = float(numericValue)*1000000
    elif 'k' in numericValue:
        numericValue = numericValue.replace('k', '')
        numericValue = float(numericValue) * 1000

    return int(numericValue)


# Draw the bar chart
def drawBarChart(y_data, fetchedData, igAccount):
    X_data = ("Followers", "Following", "Posts")
    y_pos = np.arange(len(X_data))

    plt.bar(y_pos, y_data, align='center', alpha=1)
    plt.ylim(min(y_data)-10, max(y_data)*1.1)

    # Add bar labels
    for i in range(len(fetchedData)):
        plt.text(x=i, y=((max(y_data) - min(y_data)) / 2) + min(y_data), s=fetchedData[i], horizontalalignment='center',
                 verticalalignment='center')

    plt.xticks(y_pos, X_data)
    plt.ylabel('Count')
    plt.title(igAccount + "'s Instagram Account Info")

    return plt


# Main funtion
if __name__ == '__main__':

    IGACCOUNTNAME = "eye.tattoo.girl"  # Public Instagram account name
    numericValues = []

    fetchedData = findDataInIg(IGACCOUNTNAME)

    for number in fetchedData:
        numericValues.append(cleanNumbers(number))

    plt = drawBarChart(numericValues, fetchedData, IGACCOUNTNAME)
    plt.show()