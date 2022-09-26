# Chatbot implementation
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
    if 'quote' in data['queryResult']['queryText']:
        today_quote = utils.get_quote()
        response = {
            "fulfillmentText": today_quote
        }
        return jsonify(response)

    if 'musa' in data['queryResult']['queryText']:
        link = 'https://sample-videos.com/img/Sample-jpg-image-100kb.jpg'

        response = {
            "fulfillmentMessages": [
                {
                    "payload": {
                        "mediaUrl": link,
                        "text": "Example logo"

                        # // custom integration payload here
                    }
                }
            ]
        }
        return jsonify(response)
    if 'image' in data['queryResult']['queryText']:
        link = "https://pbs.twimg.com/ext_tw_video_thumb/1450389344418734080/pu/img/zX1Acbm-qMbl1PfK.jpg"
        
        response = {
            "fulfillmentMessages": [
                {
                    "payload": {
                        "mediaUrl": link,
                        "text": "Breast Cancer Awareness Month"

                        # // custom integration payload here
                    }
                }
            ]
        }


if __name__ == '__main__':
    app.run(debug=True)
