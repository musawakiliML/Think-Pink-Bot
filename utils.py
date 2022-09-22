# Chatbot Functions
import requests

def get_quote():
    response = requests.get("https://zenquotes.io/api/today")

    if response.status_code == 200:
        values = response.json()
        quote = values[0]['q']
        author = values[0]['a']
        
        result = f"{author.upper()} Said: '{quote}'."
        
        #print(quote)
        #print(author)
        #print(values)
        
        return result
