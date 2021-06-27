import json
import os
import string

import requests
from bs4 import BeautifulSoup

page_num = int(input())
article_type = input()
for n in range(1, page_num + 1):
    url_ = "https://www.nature.com/nature/articles?page={}".format(str(n))
    os.mkdir("Page_" + str(n))
    os.chdir("Page_" + str(n))
    response = requests.get(url_)
    if response.status_code != 200:
        print("The URL returned {}!".format(response.status_code))
        exit(0)
    source = response.content
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = {}
    tags_ = soup.select('article')
    for tag in tags_:
        tag_ = tag.select_one("article [data-test] span[class='c-meta__type']")
        # if tag_.text == 'News':
        if tag_.text == article_type:
            name = tag.select_one("[data-track-action='view article']").text
            name = name.strip()
            source = tag.select_one("[itemprop='url']").get('href')
            source = 'https://www.nature.com' + source
            for ch in string.punctuation:
                name = name.replace(ch, "")
            name = name.replace(" ", "_")
            response = requests.get(source)
            soup_ = BeautifulSoup(response.content, 'html.parser')
            source = soup_.select_one(".article-item__body").text
            with open(name + '.txt', 'w', encoding='utf-8') as file:
                file.write(source)
    os.chdir("..")
