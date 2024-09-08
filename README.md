WhatsApp Expense Tracker Bot

Objective
Create a WhatsApp bot that allows users to track their expenses using natural language input. The bot should be able to understand and process expense entries and queries in natural language, categorize expenses automatically, and provide insightful responses to user queries.

Example Expenses
"Spent ₹150 on a masala dosa at Udupi Restaurant yesterday"
"Bought groceries for ₹2000 at Big Bazaar"
"Paid ₹250 for lunch at Burger King"
"₹80 for a cutting chai this morning"
"₹3500 for a new pair of shoes from Bata"
"Ola ride to work cost ₹200"
"₹1000 for monthly mobile recharge"
"Watched a movie, tickets cost ₹300 each for 2 people"
"₹5000 for quarterly bike servicing"
"Ordered biryani on Swiggy for ₹400"
"Uber ride home cost ₹180"
"Bought vegetables from Zepto for ₹300"
"Late night ice cream from Blinkit ₹120"
"Ola auto to the metro station ₹60"
"Ordered pizza from Blinkit, cost ₹500"
Example Queries

Query: "What's my total food expenditure this month?"
 Response: "Your total food expenditure this month is ₹4120. This includes all restaurant meals, groceries, and food deliveries."
Query: "List all my travel expenses"
 Response: "Here's a list of all your travel expenses:
Ola ride to work: ₹200
Quarterly bike servicing: ₹5000
Uber ride home: ₹180
Ola auto to the metro station: ₹60 Total travel expenses: ₹5440" 
Query: "How much have I spent on shopping?"
 Response: "Your total shopping expenses are ₹5800. This includes both online and offline purchases of goods.
Query: "List all my online orders"
 Response: "Here's a list of all your online orders:
Biryani from Swiggy: ₹400
Vegetables from Zepto: ₹300
Ice cream from Blinkit: ₹120
Pizza from Blinkit: ₹500
Groceries from Big Bazaar (if ordered online): ₹2000 Total online orders: ₹3320 (or ₹1320 if Big Bazaar was an in-store purchase)"

## Installation

Prerequisites
Before you begin, ensure you have the following installed:

Python 3.8+: Download Python
pip: Python package installer (usually included with Python installation)
Flask: Web framework for Python (installed via pip)
Twilio: For WhatsApp integration 


```bash
git clone https://github.com/SiddhantBagga02/Whatsapp-Expense-Tracker.git
cd whatsapp-expense-tracker

```
    
## Appendix

What's Working  :-
. Generating Response for 'Spent' 'paid' 'Cost' Queries

. Allow User to Add expenses using Natural Language

. categorization 


What's Not Working :-
. not replying message in whatsapp due to ngrol connection issue

. sometimes it is not replying for 'paid' and 'cost' queries.

. cannot generate reports using data visualization.

## Issues I faced
. tried different gpt's models
- gptJ- Takes too much system resources which in turn taking hours to generate response
- gpt2- Generating random query based responses
eg query- spent 150 on burger 

responses  - Here is information about your pc
- gpt4- Premium Account Required for complex bot design 