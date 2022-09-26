# Chatbot Functions
import requests
from newsapi import NewsApiClient

# Init news api class
newsapi = NewsApiClient(api_key='bdab0a5542d548b089fd8ab63022cf55')

# get top headlines


def top_headlines():
    top_headlines = newsapi.get_top_headlines(q='breastcancer',
                                              category='general',
                                              language='en',
                                              country='us')
    return top_headlines


'''
def get_quote():
    response = requests.get("https://zenquotes.io/api/today")

    if response.status_code == 200:
        values = response.json()
        quote = values[0]['q']
        author = values[0]['a']

        result = f"{author.upper()} Said: '{quote}'."

        # print(quote)
        # print(author)
        # print(values)

        return result
'''

top_headlines = top_headlines()
print(top_headlines)


def ngnews():
    newsapi = NewsApiClient(api_key='bdab0a5542d548b089fd8ab63022cf55')
    top_headlines = newsapi.get_top_headlines(q='coronavirus',
                                              category='general',
                                              language='en',
                                              country='ng')
    articles = top_headlines["articles"]
    results = [arr["title"] for arr in articles]
    result_url = [arr["url"] for arr in articles]
    news_head = ["Headliness Now: \n "]
    news_headurl = ["lINKS: \n"]

    for index, item in enumerate(results):
        news_head.append(str(index + 1) + ": " + item + "\n \n")
        head_news = " ".join(news_head)

    for index1, item1 in enumerate(result_url):
        news_headurl.append(str(index1 + 1) + ": " + item1 + "\n\n")
        head_newsurl = " ".join(news_headurl)

    finalnews = head_news + head_newsurl

    return finalnews
