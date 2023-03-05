import os
import requests
from flask import Flask

app = Flask(__name__)

@app.before_request
def handle():
    link = os.environ["LINK"]
    response_data = requests.post(link)
    print(response_data.text)
    if response_data.content:
        print("Got it")

    return ""

app.run(host="0.0.0.0", port=int(os.getenv("PORT")))


