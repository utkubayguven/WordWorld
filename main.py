import requests
import csv
import re
from bs4 import BeautifulSoup

file = open("WordUniverse.csv", "w")
writer = csv.writer(file)


#find pages number
c=1
i=0
j=0
def pagneNumber(c):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]
    URL = "https://www.lexico.com/es/list/"+letters[j]+"/1?locale=en"
    req = requests.get(URL)
    soup = BeautifulSoup(req.text, "html.parser")
    for classes in soup.find_all("span", {"class": "last"}):
        for hrefs in classes.find_all('a'):
            a = str(hrefs).strip()
            num = re.findall(r'\d[0-9]*', a)
            b=num[0]
            c = int(b)
    return c


word1="test"


while word1!="":
    pagneNumber(c)
    page = str(i+1)
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    URL = "https://www.lexico.com/es/list/"+letters[j]+"/" + page+ "?locale=en"
    i = i + 1
    if pagneNumber(c) == i:
        j=j+1
        i=0
    req = requests.get(URL)

    soup = BeautifulSoup(req.text, "html.parser")

    for classes in soup.find_all("div", {"class": "textBlock layout sitemap_row"}):
        for words in classes.find_all('ul'):
            for word in words.find_all('li'):
                word1 = word.text
                print(word1)
                writer.writerow([word1])  # if your ide doesnt support, you can write writer.writerow([word1].encode("utf-8"))

file.close()








