# import libraries
import requests
from bs4 import BeautifulSoup as bs

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

author = []
repo = []
for i in range(len(blk_details)):
    title = blk_details[i].find_all("h1", {"class": "h3 lh-condensed"})[0].text
    title = title.strip().replace(" ", "")
    val_list = title.split("/")
    for val in val_list:
        val.replace("\n", "")
    author.append(val_list[0])
    repo.append(val_list[1][2:])

for i in range(len(author)):
    print(author[i], "==>", repo[i])
    print("_"*50)