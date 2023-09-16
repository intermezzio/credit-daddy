import requests

url = "https://api.cohere.ai/v1/chat"

snippet_data = "9/16/23, 1:16 AMApply for a Capital One Cardhttps://applynow.capitalone.ca/?external_id=WWW_C0493_EGB_AAZ_ER_CADSX_GENA_BC_T_SEM&ad_id=154626887883&dev_id=c&mtch=b&k…1/2Capital One® Important DisclosuresSummary of key terms as of June 1, 2023.Annual Interest RatesThese interest rates are in effect upon approval.Standard rate for purchases: 21.9%.Standard rate for balance transfers1: 21.9%.Standard rate for cash advances2: 21.9%.Default rate: Your minimum payment for any given billing period is due by the payment due datespecified on the monthly statement for that period. If we do not receive your minimum paymentby the payment due date 2 times in any 12-month period, your rates will increase to the defaultrate of 25.9% at the beginning of the next billing period.Then, if we receive at least the minimum payment by the payment due date for 12 consecutivebilling periods, your rates will change to the standard rates that apply to your account at that time,starting from the beginning of the next billing period.Interest-Free GracePeriodYou will benefit from an interest-free grace period of at least 25 days on new purchases andstandard balance transfers if you pay off your new balance in full by the payment due date. Thereis no interest-free grace period on cash advances, special balance transfers3 and interest charges.Minimum PaymentIf you reside anywhere other than the province of Quebec, your required minimum payment willbe the greatest of:The sum of the following, rounded down to the nearest dollar:a) 1% of your new balance,b) any interest charges you may have, andc) 1/12th of your annual fee;plus any past due required minimum payment amountor$10 plus any past due required minimum payment amount.If you reside in Quebec, your required minimum payment will be the greatest of:5% of your new balance plus any past due required minimum payment amountor$15 plus any past due required minimum payment amount.If your required minimum payment exceeds your total balance, we’ll only require the totalbalance. If you are over limit by more than your required minimum payment, we’ll request thefull over limit amount.Foreign CurrencyConversionWe bill you in Canadian dollars when you use your card to make a transaction in a foreigncurrency. The transaction amount will be converted to Canadian dollars using the Mastercard rateof exchange applicable at the time the transaction is processed. When the converted transactionposts to your account, we will add a foreign currency conversion charge equal to 2.5% of theconverted transaction amount.9/16/23, 1:16 AMApply for a Capital One Cardhttps://applynow.capitalone.ca/?external_id=WWW_C0493_EGB_AAZmount of $75 or $300, which actas collateral and help show us you’re committed to using your card responsibly. By providing us with security funds, you agree that ifyou’re in default on your account, you authorize Capital One to set off (and effect compensation, if you’re a resident of the province ofQuebec) and apply those funds against your obligations to us, without notice or demand for payment. Your funds will be held in anaccount at a depository institution we select, but don’t constitute a deposit with Capital One. Any interest earned on the security fundswill become our sole property, and you’ll have no right to access or withdraw the funds until your account is paid in full and closed.You can increase your credit limit, up to a maximum of $2,500, by providing additional security funds – we’ll increase your limit by$1 for every $1 in additional funds you send in. You’ll receive more information about the amount of security funds required, andterms that apply, if you’re approved.BenefitsThere are benefits included with this card. You’ll receive more information about the benefits available to you, and the terms,conditions, limitations and exclusions that apply, in the documentation provided with your card if you’re approved."

payload = {
    "message": "What is the foreign conversion rate?",
    # documents has title of document and snippet of text
    "documents": [
        {"title": "TD Double Up Terms and Conditions", "snippet": snippet_data},
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
