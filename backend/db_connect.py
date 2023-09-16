import time
import os
import heapq
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


# Initialize Firebase
cred = credentials.Certificate("firebase-sdk-admin.json")
firebase_admin.initialize_app(cred)

# Initialize Firestore Database
db = firestore.client()

# env variables
load_dotenv()

api_key = os.getenv("FIREBASE_API_KEY")

def name_to_id(name: str):
    return name.lower().replace(" ", "-")

def upload_card(name: str, company_name: str, card_type: str, avg_apr: float, min_cashback: float,
        max_cashback: float,
        foreign_fee: float, intro_offer: bool, intro_offer_details: str, description: str,
        annual_fee: float, overcharge_fee: float):
    id_ = name_to_id(name)
    row_data = {
        "id": id_,
        "name": name,
        "company-name": company_name,
        "card-type": card_type,
        "avg-apr": avg_apr,
        "min-cashback": min_cashback,
        "max-cashback": max_cashback,
        "foreign-fee": foreign_fee,
        "intro-offer": intro_offer,
        "intro-offer-details": intro_offer_details,
        "description": description,
        "annual-fee": annual_fee,
        "overcharge-fee": overcharge_fee,
    }

    if get_card(id_):
        raise ValueError("We already have this card")

    db.collection("cards").add(row_data)

def upload_chat(id_: str, question: str, answer: str):
    row_data = {
        "id": id_,
        "question": question,
        "answer": answer,
        "timestamp": time.time(),
    }
    db.collection("questions").add(row_data)

def get_card(id_: str):
    query = db.collection("cards").where(filter=firestore.FieldFilter("id", "==", id_))
    cards = query.stream()

    try:
        if card := next(cards):
            return card.to_dict()
    except StopIteration:
        return None

def get_chats(id_: str):
    query = db.collection("questions").where(filter=firestore.FieldFilter("id", "==", id_)).order_by("timestamp")

    return [chat.dict() for chat in query.stream()]

def calc_metric(metric_1: float, metric_2: float, row_data: dict):
    # TODO: calculate metric
    return 1

def get_optimal(metric_1: float, metric_2: float, n=3):
    id_to_metric = {}

    for card in db.collection("cards").stream():
        id_to_metric.update(card.id, calc_metric(metric_1, metric_2, card))

    return heapq.nlargest(n, id_to_metric.keys(), key=id_to_metric.get)
