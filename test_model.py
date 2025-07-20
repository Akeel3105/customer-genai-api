# test_model.py

from app.model import classify_ticket

ticket_text = "I want to cancel my plan and get a refund for this month."

result = classify_ticket(ticket_text)

print("Classification Result:")
print(result)

