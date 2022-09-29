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
                'text': {
                    'text': [f"{em(':handshake:',language='alias')} Let's Fight Breast Cancer Together!!"]
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
                    'text': [f"{em(':robot:',language='alias')} I am Chatbot that can educate you on Breast Cancer with verified information like video, links and pictures."]
                }
            },
            {
                'text': {
                    'text': [f"You Can Start Here: {em(':question:',language='alias')} \n 1. What is Breast Cancer? \n 2. What Causes Breast Cancer? \n 3. What are the symptoms of breast cancer? \n 4. Early Detection \n 5. Diagnosis \n 6. Stages \n 7. Types of Breast Cancer \n 8. Treatment \n 9. Breast Cancer Myths \n 10. FAQS(Frequently Asked Questions) \n 11. Breast Cancer Resources \n 12. Free Educational Guides \n 13. Search Google."]
                }
            },
        ]
    }
    return response_message


def causes():
    # breast cancer causes
    pass

def symptoms():
    # breast cancer symptoms
    pass


def resources():
    # website links
    # pdf and others
    # resources of breast cancer
    pass