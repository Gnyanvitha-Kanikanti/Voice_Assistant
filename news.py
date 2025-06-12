from newsapi import NewsApiClient
import requests
api_key = "6618fd0b60d44ba5bd492d8bb2ef7242"
newsapi = NewsApiClient(api_key=api_key)
title_list=[]
def news(max_titles=3):
    count = 1
    top_headlines = newsapi.get_top_headlines(language="en")
    for i in top_headlines['articles']:
        if len(title_list)<max_titles:
            title_list.append("Number"+str(count)+" "+i['title'])
            count = count+1
        else:
            break
    return title_list