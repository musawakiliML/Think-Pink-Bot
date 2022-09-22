# Chatbot implementation
import re
from urllib import response
from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
import utils

app = Flask("__name__")


@app.route('/')
def index():

    return "Hello World!!"


@app.route("/bot", methods=["POST"])
def bot():
    data = request.get_json()
    print(data)
    # if 'quote' in data['queryResult']['queryText']:
    #    today_quote = utils.get_quote()
    #    response = {
    #        "fulfillmentText": today_quote
   #     }
    #if 'image' in data['queryResult']['queryText']:
    link = 'https://sample-videos.com/img/Sample-jpg-image-100kb.jpg'

    response = {
        "fulfillmentMessages":
            {
                "payload": {
                    'mediaUrl': link,
                    'text': "Testing images"
                }
            }

    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
