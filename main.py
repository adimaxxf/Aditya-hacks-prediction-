from flask import Flask, request
import requests
import os

app = Flask(__name__)
BOT_TOKEN = os.environ.get("BOT_TOKEN")
URL = f"https://api.telegram.org/bot{7976941515:AAHHcbK5-w9Os8d7R0g-HTUg4WtIyYDawp4}/sendMessage"

# 10-character rule-based transformation
def transform_input(text):
    if len(text) != 10 or any(c.upper() not in "SB" for c in text):
        return "Please send exactly 10 letters using only S or B."

    text = text.upper()
    positions = [7, 9, 5, 6, 8, 2, 3, 0, 4, 1]
    output = ''.join(text[i] for i in positions)
    return output

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    if 'message' in data and 'text' in data['message']:
        chat_id = data['message']['chat']['id']
        incoming_text = data['message']['text']
        reply = transform_input(incoming_text)
        requests.post(URL, json={'chat_id': chat_id, 'text': reply})
    return 'OK'

@app.route('/')
def home():
    return "Bot is running!"
