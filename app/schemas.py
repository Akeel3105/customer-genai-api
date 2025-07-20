# app/schemas.py

from pydantic import BaseModel


class TicketRequest(BaseModel):
    ticket: str


class TicketResponse(BaseModel):
    sentiment: str
    confidence: float
    category: str
    response: str
