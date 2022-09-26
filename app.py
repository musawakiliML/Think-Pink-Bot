# Chatbot implementation
from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
import utils


# app initialization
app = Flask("__name__")



@app.route('/')
def index():

    return "Hello World!!"

# Function for building responses
def results():
    
    pass


# The Bot webhook for serving responses

@app.route("/bot", methods=["POST"])
def bot():
    data = request.get_json(force=True)
    action = data.get('queryResult').get('action')
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
                    'text':{
                        'text':["Hello I am a chatbot", "Helllo i am breast cancer chatbot"]
                    }
                },
                {
                    'text':{
                        'text':["I will diagnose you and share tips with you"]
                    }
                },
                {
                    "payload": {
                        "mediaUrl": link,
                        "text": "Breast Cancer Awareness Month"
                        # // custom integration payload here
                    }
                },
                {
                    "payload": {
                        "mediaUrl": 'https://youtu.be/rEV_bc32HaY',
                        "text": "Breast Cancer Awareness Month"
                        # // custom integration payload here
                    }
                }
            ]
        }
        return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
