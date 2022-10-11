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
                    'text': [f"You Can Start Here: {em(':question:',language='alias')} \n 1. What is Breast Cancer? {em(':person_raising_hand:',language='alias')} \n 2. What Causes Breast Cancer? {em(':thinking_face:',language='alias')} \n 3. What are the symptoms of breast cancer? {em(':thinking_face:',language='alias')} \n 4. Early Detection {em(':medical_symbol:',language='alias')} \n 5. Diagnosis {em(':stethoscope:', language='alias')} \n 6. Stages {em(':twelve_o’clock:', language='alias')}\n 7. Types of Breast Cancer {em(':check_box_with_check:', language='alias')} \n 8. Treatment {em(':hospital:', language='alias')} \n 9. How to do Breast Self Examination \n 10. Breast Cancer Myths {em(':warning:', language='alias')} \n 11. FAQS (Frequently Asked Questions) {em(':bookmark_tabs:', language='alias')} \n 12. Breast Cancer Resources {em(':books:', language='alias')} \n 13. Free Educational Guides {em(':light_bulb:', language='alias')} \n 14. Search Google {em(':magnifying_glass_tilted_right:', language='alias')} \n\n {em(':keyboard:', language='alias')}Type any option to get a response..."]
                }
            },
        ]
    }
    return response_message


def breast_cancer():
    # Explain breast cancer
    response_message = {
        "fulfillmentMessages": [
            {
                'text': {
                    'text': ["Breast cancer is a disease in which malignant (cancer) cells form in the tissues of the breast. ", "Breast cancer is a common term for a cancerous (malignant) tumor that starts in the cells that line the ducts and/or lobes of the breast. Breast cancer is not one disease; rather it is several diseases that behave differently."]
                }
            },
            {
                'text': {
                    'text': ["More Facts on Breast Cancer:\n 1. How does breast cancer start? \n - Breast cancer starts when cells in the breast begin to divide and grow in an unusual and uncontrolled way. \n 2.Where does breast cancer start? \n - Breast cancer can start in different parts of the breast.The most common type of breast cancer starts in the ducts. The ducts are tubes in the breast that carry breast milk to the nipple. Sometimes cancer can start in the lobules. The lobules are glands that produce milk for breastfeeding. \n 3. Who does breast cancer affect? \n - Breast cancer mainly affects older women. Most breast cancers (80%) occur in women over the age of 50. And the older you are, the higher your risk. Men can also get breast cancer, but this is rare. Most men who get breast cancer are over 60. Breast cancer is caused by a combination of our genes, environment and lifestyles.\n 4. Being breast aware: \n The earlier breast cancer is diagnosed, the better the chance of successful treatment. So it's important to check your breasts regularly and see your GP if you notice a change."]
                }
            },
            {
                "text": {
                    "text": ["Click the Link to Learn More..\n 1. https://breastcancernow.org/information-support/have-i-got-breast-cancer/what-breast-cancer \n 2. https://www.nationalbreastcancer.org/what-is-breast-cancer/"]
                }
            },
            {
                "payload": {
                    "text": "What is Cancer",
                    "mediaUrl":'https://dandelion-robin-1277.twil.io/assets/what%20is%20cancer.mp4'
                }
            },
            {
                "payload":{
                    "text":"Breast Cancer",
                    "mediaUrl": 'https://dandelion-robin-1277.twil.io/assets/breast%20cancer.jpg'
                }
                
            }
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
