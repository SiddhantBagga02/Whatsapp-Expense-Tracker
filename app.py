from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from bot import generate_intent_response

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return "Welcome to the Expense Tracker Bot!"

@app.route('/favicon.ico')
def favicon():
    return '', 204

@app.route('/webhook', methods=['POST'])
def webhook():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    
    response_text = generate_intent_response(incoming_msg)
    
    msg.body(response_text)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4040)
