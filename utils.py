# Chatbot Functions

# External libraries
import requests
from googlesearch import search


# Google Search function
def search_google(user_message):
    # results list
    results = []

    # searching and storing the urls
    for i in search(user_message, lang='en', num_results=6):
        results.append(i)
    return results

#query = input("Enter a search query:")

#results = search_google(query)

#print(results)
