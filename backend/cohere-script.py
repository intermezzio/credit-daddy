import requests

url = "https://api.cohere.ai/v1/chat"

payload = {
    "message": "What is the APR for purchases?",
    # documents has title of document and snippet of text
    "documents": [
        {"title": "TD Double Up Terms and Conditions", "snippet": "TD Double UpSM Important Credit Card Terms and Conditions Rates, fees, and other important costs of the TD Double Up Credit Card are disclosed below. Additional fees and account terms are described in the TD Double Up Credit Card Agreement that will be enclosed with the card if a card is issued. The terms disclosedbelow and in the TD Double Up Credit Card Agreement (together, the “Agreement”) and the TD Double Up Credit Card rewardprogram may be changed at any time subject to applicable law. Based on our evaluation of your credit report and other factors, ifapproved for a TD Double Up Credit Card, you may receive a credit card account (Account) with a minimum credit line of $500 ormore. If you apply and are approved, you will receive either a Signature Visa card if your approved account credit limit is$5,000 or greater or a Platinum Visa card if your approved account credit limit is less than $5,000. Both Signature andPlatinum cards have the same terms and conditions, however the Signature card comes with added Visa Signature benefitssuch as complimentary 24/7 concierge, access to exclusive events, special shopping perks and more.The information about the costs of the card described below is accurate as of September 6, 2023. This information maychange after that date. To find out what may have changed, please call us at 1-888-561-8861.Interest Rates and Interest ChargesAnnual Percentage Rate(APR) for Purchases: 20.24%, 25.24% or 30.24% based on your creditworthiness.All APRs will vary with the market based on the Prime Rate.APR for Balance"},
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

answer_text = response_data.get('text', 'Key not found')

print(answer_text)
