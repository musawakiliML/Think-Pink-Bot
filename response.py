# The Module for generating the response for the chatbot
from emoji import emojize as em
# About think pink function


def about_us():
    response_message = {
        "fulfillmentMessages": [
            {
                'text': {
                    'text': [f"{em(':ribbon:',language='alias')} Think Pink is Non-Governmental Organization that aims at raising awareness for breast cancer, supporting the individuals affected by it.\nSaving Lives Through early detection."]
                }
            },
            {
                'text': {
                    'text': ["Early diagnosis of breast cancer is possible through adequate awareness and intervention."]
                }
            },
            {
                'text': {
                    'text': [f" {em(':robot:',language='alias')} Our Chatbot will help learn about breast cancer."]
                }
            },
            {
                "payload": {
                    "mediaUrl": "https://dandelion-robin-1277.twil.io/assets/logo.jpeg",
                    "text": "We are Think Pink Breast Cancer Awareness"
                    # // custom integration payload here
                }
            }
        ]
    }
    return response_message

# Main Functions


def welcome():
    response_message = {
        "fulfillmentMessages": [
            {
                'text': {
                    'text': [f"Hi! {em(':waving_hand:',language='alias')}  Good day", f"Hello! {em('waving_hand',language='alias')} Nice to meet you"]
                }
            },
            {
                'text': {
                    'text': [f"{em(':robot:',language='alias')} I am Chatbot that can educate you on Breast Cancer.\nI will send you verified information with both video, links and pictures."]
                }
            },
            {
                'text': {
                    'text': [f"You can Ask me things Like {em(':question:',language='alias')} \n 1. What is breast cancer? \n 2. "]
                }
            },
            {
                'text': {
                    'text': [f"{em(':handshake:',language='alias')} Let's Fight Breast Cancer Together!!"]
                }
            },
        ]
    }
    return response_message
