from flask import Flask, request, Response
import requests


app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def respond():
    print(request.json)
    received_payload = request.json 
    if received_payload["sender"]["login"] == "npraveenk1":
        print("Sender is {}".format(received_payload["sender"]["login"]))
    return Response(status=200)
