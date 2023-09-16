# from http.server import HTTPServer, BaseHTTPRequestHandler
# from urllib.parse import parse_qs
import json

from flask import Flask, redirect, url_for, request
import db_connect


app = Flask(__name__)

@app.route('/card/<id_>')
def get_card(id_, methods=['GET']):
    # get card info
    card_info = db_connect.get_card(id_)
    return card_info

@app.route('/chats/<id_>')
def get_chats(id_, methods=['GET']):
    # get chats
    chats = db_connect.get_chats(id_)
    return chats

@app.route('/upload-card', methods=['POST'])
def analyze_contract():
    name = request.form['name']
    # get card 
    return id_

if __name__ == '__main__':
   app.run(debug=True, port=3000)
