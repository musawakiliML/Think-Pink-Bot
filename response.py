# The Module for generating the response for the chatbot


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
                        "mediaUrl":"#",
                        "text": "We are Think Pink Breast Cancer Awareness"

                        # // custom integration payload here
                    }
                }
            ]
        }