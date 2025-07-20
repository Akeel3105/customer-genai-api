# app/main.py

from fastapi import FastAPI
from app.model import classify_ticket
from app.schemas import TicketRequest, TicketResponse

app = FastAPI(title="Customer Ticket Classifier API")

@app.get("/")
def root():
    return {"message": "Welcome to the Customer Ticket Classifier API"}

@app.post("/predict", response_model=TicketResponse)
def predict_ticket(data: TicketRequest):
    result = classify_ticket(data.ticket)
    return result
