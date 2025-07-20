from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import numpy as np

# Example training data for basic classification
train_data = [
    "I want to cancel my subscription",
    "I was charged twice for the same service",
    "How can I reset my password?",
    "Refund my money",
    "I can't log in to my account",
    "Unsubscribe me",
    "Help me with a technical issue",
    "The website shows an error",
    "Billing issue with my invoice",
    "Close my account"
]

train_labels = [
    "Cancellation",
    "Billing",
    "Technical Support",
    "Billing",
    "Technical Support",
    "Cancellation",
    "Technical Support",
    "Technical Support",
    "Billing",
    "Cancellation"
]

# Train a simple model
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(train_data)

classifier = MultinomialNB()
classifier.fit(X_train, train_labels)

def classify_ticket(ticket_text: str) -> dict:
    print("📨 Classifying with scikit-learn model")
    X_test = vectorizer.transform([ticket_text])
    category = classifier.predict(X_test)[0]
    proba = np.max(classifier.predict_proba(X_test))

    # Basic response logic
    if category == "Billing":
        response = "Please check your billing history. We'll process any necessary refunds."
    elif category == "Technical Support":
        response = "Our tech team is on it. Can you provide more details about the issue?"
    elif category == "Cancellation":
        response = "We're sorry to see you go. Your subscription will be canceled as requested."
    else:
        category = "General Inquiry"
        response = "Thank you for your message. We'll get back to you shortly."

    return {
	"sentiment": "Neutral", # Dummy Value
        "category": category,
        "confidence": round(float(proba), 2),
        "response": response
    }
