#import important libraries
import requests
from bs4 import BeautifulSoup as bs
import numpy as np
import pandas as pd

def topics():
    #URL of the scrapping website
    url = "https://github.com/topics"

    #GETTING url
    response = requests.get(url)
    # print(response.status_code)

    #Checking if URL is perfectly running
    if(response.status_code != 200):
        print("Error")

    #GETTING content
    content = response.text

    soup = bs(content,"html.parser")

    blk = soup.find_all("div", {"class" : "py-4 border-bottom"})

    #Details
    title = []
    content = []

    #iterating block
    for i in range(len(blk)):
        #Extract title
        title_lst = blk[i].find_all("p", {"class": "f3 lh-condensed mb-0 mt-1 Link--primary"})
        if(title_lst):
            title.append(title_lst[0].text)
        else:
            title.append(np.nan)

        content_lst = blk[i].find_all("p", {"class": "f5 color-text-secondary mb-0 mt-1"})
        # content_lst = content_lst.replace
        if(content_lst):
            for val in content_lst[0]: 
                val = val.replace("\n", "").strip()
            # print(content_lst[0])
            # content_lst[0] = content_lst[0].replace("\n", "")
                content.append(val)
        else:
            content.append(np.nan)

    df = {"Title" : title, "Content" : content}
    #converting into DataFrame
    df = pd.DataFrame(df)
    # df.to_csv("topics.csv")
    return df

    # print("Title ==> ", title)
    # print("Content ==>", content)