# The Module for generating the response for the chatbot

# About think pink function
def about_us():
    response_message = {
            "fulfillmentMessages": [
                {
                    'text':{
                        'text':["Think Pink is Non-Governmental Organization that aims at raising awareness for breast cancer, supporting the individuals affected by it."]
                    }
                },
                {
                    'text':{
                        'text':["Saving Lives Through early detection. Early diagnosis of breast cancer is possible through adequate awareness and intervention."]
                    }
                },
                {
                    'text':{
                        'text':["Our Chatbot will help learn about breast cancer."]
                    }
                },
                {
                    "payload": {
                        "mediaUrl":"https://dandelion-robin-1277.twil.io/assets/logo.jpeg",
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
                    'text':{
                        'text':["Hi! Good day", "Hello! Nice to meet you"]
                    }
                },
                {
                    'text':{
                        'text':["I am Chatbot that can educate you on Breast Cancer. I will send you verified information with both video, links and pictures."]
                    }
                },
                {
                    'text':{
                        'text':["Let's Fight Breast Cancer Together!!"]
                    }
                },
                {
                    'text':{
                        'text':["You can Ask me things Like: 1. What is breast cancer "]
                    }
                },
                {
                    "payload": {
                        "mediaUrl":"https://dandelion-robin-1277.twil.io/assets/logo.jpeg",
                        "text": "We are Think Pink Breast Cancer Awareness"
                        # // custom integration payload here
                    }
                }
            ]
        }
    

