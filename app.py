# Chatbot implementation

from flask import Flask
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/bot', methods=["POST"])
def bot():
    return "Hello World!!"



if __name__ == '__main__':
    app.run(debug=True)
    
