# tests/test_model.py

import pytest
from app.model import classify_ticket

def test_billing_ticket():
    result = classify_ticket("I was charged twice this month")
    assert result["category"] == "Billing"
    assert isinstance(result["confidence"], float)
    assert "refund" in result["response"].lower() or "billing" in result["response"].lower()

def test_tech_ticket():
    result = classify_ticket("I can't log in to my account")
    assert result["category"] == "Technical Support"

def test_cancel_ticket():
    result = classify_ticket("Please cancel my subscription")
    assert result["category"] == "Cancellation"
