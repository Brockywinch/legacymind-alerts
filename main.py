import os
import requests
from flask import Flask

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

@app.route("/send")
def send_message():
    message = "🔔 LegacyMind Test Alert\nYou're now connected. All future milestone alerts will be sent right here."
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    r = requests.post(url, data=payload)
    return "Message sent!" if r.status_code == 200 else f"Error: {r.text}"
