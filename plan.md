# Credit Card Comparer

### Features

- Upload a PDF and get credit card info in a standardized format
- Be able to ask more questions about the specific credit card
- Get recommendations for credit cards based on preferences
- Search for credit cards given preferences?
- See random credit card?

## Frontend

## Backend

- Convert PDF to text for processing

### Cohere

- Chat feature with RAG to upload text
- Define set of metrics (questions) to ask and get consistent results
- Store results in a database
- Be able to answer a follow up question about the contract

### Database

- Choose database (firebase, mongodb, cockroach)
- Create schema
- Make method to take NLP results and store in cohere
- Figure out how to calculate and sort entries by a metric (for user preferences)

### Server

- Choose a place to host the server
- Create an API endpoint that gets the data from a given PDF
- Be able to answer a follow-up question about a contract

### Schema Ideas

- id (uuid)
- name (str)
- Company name (eg Air Canada)
- Avg. APR (float)
- Min Cashback (float)
- Max Cashback (float)
- Min Credit Score (int) ?
- Foreign transaction fee (float)
- Has sign on offer (bool)
- Sign on offer (sentence explanation)
- Type of credit card [ie Visa Mastercard Amex Discover] (string)
- 
