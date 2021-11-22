questions = {
    "Hello there": "greeting",
    "Track my order 3231": "order_tracking",
    "I want to set an appointment with Manoj": "appointment_book",
    "I forgot my password": "forgot_password",
    "best selling product": "highest_grossing",
    "I want software update on my device": "version_update",
    "How are you doing today?": "about",
    "What do you share with your supplier?": "supplier_info",
    "What is the profit for this year": "predict_performance",
    "are customers happy": "customer_satisfaction",
    "what is customer response?": "customer_satisfaction",
    "very helpful": "thanks",
    "what do you do": "options",
    "shreyaans@gmail.com": "email_id",
    "who is your manufacturer": "manufacturing_problems",
    "what does this product do": "solve_problems",
    "what might impact sales?": "factors_impacting_sale",
    "profits from last year?": "predict_performance",
    "how are you doing today?": "about",
    "configure laptop steps": "configuration",
    "what time do you guys close?": "opening_time",
    "what is affecting sales?": "factors_impacting_sale",
    "I cannot understand what your product does": "solve_problems",
    "I don't remember my password": "forgot_password",
    "please tell my list of appointments": "appointment_status",
    "can I have an appointment with your manager?": "appointment_book",
    "THANK YOU SO MUCH": "thanks",
    "what information do your supplier know?": "supplier_info",
    "who is your manufacturer": "manufacturing_problems",
    "what do your customers say?": "customer_satisfaction",
    "what do you have in stock?": "gadgets",
    "where is your shop located?": "store_location",
    "tell me what ratings your customers give you": "customer_satisfaction",
}

from chat import get_response
from prettytable import PrettyTable

t = PrettyTable(["Question", "Actual Tag", "Predicted Tag", "Match Tag"])

for question in questions:
    _, tag = get_response(question)
    t.add_row([question, questions[question], tag, tag == questions[question]])

print(t)
