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
                    'text': [f"You Can Start Here: {em(':question:',language='alias')} \n 1. What is Breast Cancer? {em(':person_raising_hand:',language='alias')} \n 2. What Causes Breast Cancer? {em(':thinking_face:',language='alias')} \n 3. What are the symptoms of breast cancer? {em(':thinking_face:',language='alias')} \n 4. Early Detection {em(':medical_symbol:',language='alias')} \n 5. Diagnosis {em(':stethoscope:', language='alias')} \n 6. Stages {em(':twelve_o’clock:', language='alias')}\n 7. Types of Breast Cancer {em(':check_box_with_check:', language='alias')} \n 8. Treatment {em(':hospital:', language='alias')} \n 9. Breast Cancer Myths {em(':warning:', language='alias')} \n 10. FAQS (Frequently Asked Questions) {em(':bookmark_tabs:', language='alias')} \n 11. Breast Cancer Resources {em(':books:', language='alias')} \n 12. Free Educational Guides {em(':light_bulb:', language='alias')} \n 13. Search Google {em(':magnifying_glass_tilted_right:', language='alias')} \n\n {em(':keyboard:', language='alias')}Type any option to get a response..."]
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