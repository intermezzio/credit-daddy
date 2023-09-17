import requests
import os
import firebase_admin
import json
import cohere
from icecream import ic
from PDFReader import pdf_to_text 



# Cohere initialization
co = cohere.Client(os.environ.get("COHERE_API_KEY"))

url = "https://api.cohere.ai/v1/chat"

def extract_card_details(input_contract: str):

    message_1 = "Please list out the Company Name (TD, Royal Bank of Canada, etc), Card Type (card_type) [ie Visa, Mastercard] (str), Avg APR (avg_apr) (float) - use first APR seen, " \
            "Minimum Cashback (float percentage), Foreign Transaction Fee (float percentage), Sign up Offer (float percentage), Annual Fee (float percentage), and finally Overcharge fee (float percentage)." \
            "Only describe one card list in a single level JSON format. If you don't have data just put N/A for strings and a '-1' for floats. " \
            "The output should look like EXAMPLE: { Bank Name: , Card Type: , Avg Apr: , Min Cashback: , Max Cashback: , Foreign Transaction Fee: , Sign Up Offer: , Annual Fee: , Overcharge Fee: } in valid JSON."
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

    # convert to json
    bot_answer_json_1 = ic(json.loads(bot_answer_text_1))

    # add text to json
    # bot_answer_json_1["text"] = input_contract
    bot_answer_json_1["text"] = "input_contract"

    print(bot_answer_json_1)

    if True:
        return bot_answer_json_1

def ask_more_card_details(input_contract: str, question: str):
    response = co.chat(
        message=question,
        # documents has title of document and snippet of text
        documents=[
            {"title": "Card Terms and Conditions", "snippet": input_contract},
        ],
        prompt_truncation="AUTO",
    )
    return response.summary



if __name__ == "__main__":
    result_text = pdf_to_text("../data/CIBC-Premium.pdf")

    print("Sanitized PDF:")
    print(result_text)

    extract_card_details(result_text)
