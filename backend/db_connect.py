import time
import heapq
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

def upload_card(name: str, **properties):
    id_ = name_to_id(name)
    row_data = properties | {
        "id": id_,
        "name": name,
    }
    db.collection("cards").add(row_data)

def upload_chat(id_: str, question: str, answer: str):
    row_data = {
        "id": id_,
        "question": question,
        "answer": answer,
        "timestamp": time.time(),
    }
    db.collection("questions").add(row_data)

def get_chats(id_: str):
    return db.collection("questions").where(filter=FieldFilter("id", "==", id_)).order_by("timestamp")

def calc_metric(metric_1: float, metric_2: float, row_data: dict):
    # TODO: calculate metric
    return 1

def get_optimal(metric_1: float, metric_2: float, n=3):
    id_to_metric = {}

    for card in db.collection("cards").stream():
        id_to_metric.update(card.id, calc_metric(metric_1, metric_2, card))

    return heapq.nlargest(n, id_to_metric.keys(), key=id_to_metric.get)
