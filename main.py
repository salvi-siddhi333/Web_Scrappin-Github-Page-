# import libraries
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
import numpy as np

#Url of website
url = "https://github.com/trending"

response = requests.get(url)
print(response.status_code)

#Check if website is UP and running well!
if(response.status_code) != 200:
    print("Error!")

#Getting Content
content = response.text
#print(type(content))
soup = bs(content,"html.parser")
#print(soup)

#article_tag = soup.find_all("article", {"class": "Box-row"})
# print(article_tag)

#extracting all <a> from <h1> 
blk_details = soup.find_all("article", {"class": "Box-row"})

#List of different details
author = []
repo = []
lang = []
star = []
fork = []

#iterate each block
for i in range(len(blk_details)):
    #Extract Author and Repo
    title = blk_details[i].find_all("h1", {"class": "h3 lh-condensed"})[0].text
    title = title.strip().replace(" ", "")
    val_list = title.split("/")
    for val in val_list:
        val.replace("\n", "")
    author.append(val_list[0])
    repo.append(val_list[1][2:])


    #Extract Language
    lang_lst = blk_details[i].find_all("span", {"itemprop": "programmingLanguage"})
    if(lang_lst):
        lang.append(lang_lst[0].text)
    else:
        lang.append(np.nan)

    #Extract Star
    star_lst = blk_details[i].find_all("a", {"class": "Link--muted d-inline-block mr-3"})
    #star = star_lst[0].strip().replace(" ", "")
    if(star_lst):
        star.append(star_lst[0].text.strip())
    else:
        star.append(np.nan)


    #Extract Fork
    fork_lst = blk_details[i].find_all("a", {"class": "Link--muted d-inline-block mr-3"})
    if(fork_lst):
        fork.append(fork_lst[1].text.strip())
    else:
        fork.append(np.nan)

trending_dict = {
    "Author": author,
    "Repo" : repo, 
    "Language" : lang,
    "Star" : star,
    "Fork" : fork
}

#Created Data frame 
trending_dict = pd.DataFrame(trending_dict)
#Converted to csv
trending_dict.to_csv("Trending repositories on GitHub.csv")
print(trending_dict.head())

# print("Details of Trending Repositories")
# for i in range(len(author)):
#     print(author[i], "==>", repo[i])
#     print("Language ==>", lang[i])
#     print("Star ==>", star[i])
#     print("Fork ==>", fork[i])
#     print("_"*50)