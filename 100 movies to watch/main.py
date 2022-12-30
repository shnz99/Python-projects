from importlib.resources import contents
from urllib import response
import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
contents = response.text
soup = BeautifulSoup(contents, "html.parser")

titles = soup.findAll(name="h3", class_="title")
title_texts = []

for title_tag in titles:
    title_text = title_tag.getText()
    title_texts.append(title_text)

title_texts.reverse()
# print(title_texts)

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for title in title_texts:
        file.write(f"{title}\n")
