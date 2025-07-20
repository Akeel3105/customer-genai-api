from transformers import pipeline

def classify_ticket(ticket_text: str) -> dict:
    print("⏳ Starting model load...")
    classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")
    print("✅ Model loaded.")

    print(f"📨 Classifying ticket: {ticket_text}")
    sentiment = classifier(ticket_text)[0]
    label = sentiment['label']
    score = round(sentiment['score'], 2)

    if "refund" in ticket_text.lower() or "charge" in ticket_text.lower():
        category = "Billing"
        response = "Please check your billing history. We'll process any necessary refunds."
    elif "login" in ticket_text.lower() or "error" in ticket_text.lower() or "issue" in ticket_text.lower():
        category = "Technical Support"
        response = "Our tech team is on it. Can you provide more details about the issue?"
    elif "cancel" in ticket_text.lower() or "unsubscribe" in ticket_text.lower():
        category = "Cancellation"
        response = "We're sorry to see you go. Your subscription will be canceled as requested."
    else:
        category = "General Inquiry"
        response = "Thank you for your message. We'll get back to you shortly."

    return {
        "sentiment": label,
        "confidence": score,
        "category": category,
        "response": response
    }
