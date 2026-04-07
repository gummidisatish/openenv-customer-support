from pydantic import BaseModel
from typing import Optional, Dict


class Observation(BaseModel):
    email_id: str
    sender: str
    subject: str
    body: str


class Action(BaseModel):
    action_type: str
    category: Optional[str] = None
    response: Optional[str] = None
    extracted_fields: Optional[Dict[str, str]] = None


class Reward(BaseModel):
    score: float
    feedback: str