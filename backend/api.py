# from http.server import HTTPServer, BaseHTTPRequestHandler
# from urllib.parse import parse_qs
import json
import sys

from flask import Flask, redirect, url_for, request
from flask_cors import CORS, cross_origin
from icecream import ic

from werkzeug.utils import secure_filename

import cohere_script
import db_connect
from PDFReader import pdf_to_text


UPLOAD_FOLDER = "../cache"
ALLOWED_EXTENSIONS = {"pdf", "txt"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
# CORS(app)

@app.route("/card/<id_>", methods=["GET"])
def get_card(id_):
    # get card info
    card_info = db_connect.get_card(id_)
    return card_info


@app.route("/chats/<id_>", methods=["GET"])
def get_chats(id_):
    # get chats
    chats = db_connect.get_chats(id_)
    return chats


@app.route("/ask/<id_>/<question>", methods=["GET"])
def get_answer(id_, question):
    contract = db_connect.get_contract(id_)
    answer = cohere_script.ask_more_card_details(id_, question)

    db_connect.upload_chat(id_, question, answer)
    return answer


@app.route("/upload-card", methods=["POST"])
def analyze_contract():
    name = request.form["name"]
    if "file" not in request.files or request.filename == "":
        pass

    if request.filename.rsplit(".", 1)[1].lower() not in ALLOWED_EXTENSIONS:
        pass

    # see if we already have it
    id_ = db_connect.name_to_id(name)
    if db_connect.get_card(id_):
        pass

    filename = secure_filename(file.filename)
    abs_filename = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(abs_filename)

    # upload pdf and convert to text
    if abs_filename.endswith(".pdf"):
        contract_text = pdf_to_text(abs_filename)
    elif abs_filename.endswith(".txt"):
        with open(abs_filename) as infile:
            contract_text = infile.read().strip()

    # text to results
    card_details = cohere_script.extract_card_details(contract_text)

    # store results in firebase
    db_connect.upload_card(name=name, contract=contract_text, **card_details)

    # return new id
    return id_


@app.route("/recommend", methods=["GET"])
def recommend_cards(
    foreign_overcharge: float = 0,
    apr_intro_offer: float = 0,
    annual_fee_cashback: float = 0,
    n: int = 3,
):
    ids = db_connect.get_optimal(foreign_overcharge, apr_intro_offer, annual_fee_cashback)

    return ids

if __name__ == "__main__":
    app.run(debug=True, port=3000)
