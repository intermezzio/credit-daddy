import requests
import os
import firebase_admin
import json
import cohere
from icecream import ic
from PDFReader import read_pdf_content 



# Cohere initialization
co = cohere.Client(os.environ.get("COHERE_API_KEY"))

url = "https://api.cohere.ai/v1/chat"

def extract_card_details(input_contract: str):

    message_1 = "Please list out the Company Name (str), Card Type [ie Visa, Mastercard] (str), Avg APR (float), " \
            "Lowest Cashback Percentage (float), Highest Cashback Percentage (float), Foreign Transaction Fee (float), Sign on Offer (bool), " \
            "Offer details (str), Annual Fee (float), and Overcharge fee (float). " \
            "Only describe one card list in a single level JSON format. If you don't have data just put an empty string '' for strings and a '0' for floats."
    response_1 = co.chat(
        message=message_1,
        # documents has title of document and snippet of text
        documents=[
            {"title": "Card Terms and Conditions", "snippet": input_contract},
        ],
        prompt_truncation="AUTO",
    )

    # Get response from Cohere API and print the answer text

    response_data = response_1.text

    user_question = {
        "user_name": "User",
        "text": message_1,
    }


    # remove delimiters
    bot_answer_text_1 = (
        response_data
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    globals().update(locals())

    print(bot_answer_text_1)

    if True:
        return

    bot_answer_text_1 = json.loads(bot_answer_text_1)
    bot_answer = {"user_name": "Bot", "text": bot_answer_text_1}

    print("First answer: \n")
    print(json.dumps(bot_answer_text_1, indent=2))

    # ---------------------------------------------#

    payload = {
        "message": "What is the company name? Don't use JSON. Answer like a normal human.",
        # documents has title of document and snippet of text
        "documents": [
            {"title": "Card Terms and Conditions", "snippet": input_contract},
        ],
        "prompt_truncation": "AUTO",
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer rhs2oirDH8IMSqHI2P4oCIVqXoU6IzxbsYsBEcI3",
    }

    # Get response from Cohere API and print the answer text

    response = requests.post(url, json=payload, headers=headers)
    response_data = response.json()
    bot_answer_text_2 = response_data.get("text", "Key not found")

    print("Second answer: \n")
    print(bot_answer_text_2)

    full_summary = {
        "company-name": bot_answer_text_1.pop("Company Name"),
        "card-type": bot_answer_text_1.pop("Card Type"),
        "avg-apr": float(bot_answer_text_1.pop("Avg APR").strip("%")),
    }

    # add to firebase firestore
    # doc_ref = db.collection("cards").add(bot_answer_json)


def ask_more_card_details(input_contract: str, question: str):
    pass


if __name__ == "__main__":
    result_text = read_pdf_content("../data/Capital.pdf")

    extract_card_details(result_text)
