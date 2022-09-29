# Chatbot implementation
from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse
import utils
from response import about_us, breast_cancer, welcome


# app initialization
app = Flask("__name__")


@app.route('/')
def index():

    return "Hello World!!"

# Function for building responses

# The Bot webhook for serving responses


@app.route("/bot", methods=["POST"])
def bot():
    data = request.get_json(force=True)
    action = data.get('queryResult').get('action')

    if "about_us" == action:
        response = about_us()

        return jsonify(response)
    if "input.welcome" == action:
        response = welcome()

        return jsonify(response)

    if "what.breast_cancer" == action:
        response = breast_cancer()

        return jsonify(response)

    # if 'quote' in data['queryResult']['queryText']:
        #today_quote = utils.get_quote()
      #  response = {
      #      "fulfillmentText": today_quote
      #  }
      #  return jsonify(response)

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
                    'text': {
                        'text': ["Hello I am a chatbot", "Helllo i am breast cancer chatbot"]
                    }
                },
                {
                    'text': {
                        'text': ["I will diagnose you and share tips with you"]
                    }
                },
                {
                    'text': {
                        'text': ['https://youtu.be/rEV_bc32HaY']
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
                        "mediaUrl": 'https://dandelion-robin-1277.twil.io/assets/WhatsApp%20Image%202022-09-22%20at%207.17.40%20PM.jpeg',
                        "text": "Breast Cancer Awareness Month"
                        # // custom integration payload here
                    }
                },
                {
                    "payload": {
                        "mediaUrl": 'https://dandelion-robin-1277.twil.io/assets/Beyond%20The%20Shock%20-%20Chapter%204%20-%20Diagnosis%20-%20Diagnostic%20Method.mp4',
                        "text": "Breast Cancer Awareness Month"
                        # // custom integration payload here
                    }
                }
            ]
        }
        return jsonify(response)
    if action == 'contact_us':
        response = {
            "fulfillmentMessages": [
                {
                    'text': {
                        'text': ["We are Think Pink"]
                    }
                },
                {
                    "payload": {
                        "mediaUrl": 'https://dandelion-robin-1277.twil.io/assets/WhatsApp%20Image%202022-09-22%20at%207.17.40%20PM.jpeg',
                        "text": "Breast Cancer Awareness Month"
                        # // custom integration payload here
                    }
                }
            ]
        }
        return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
