from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from .summarizer import summarize

router = APIRouter()

class TextInput(BaseModel):
    text: str
    num_sentences: int = 3

@router.post("/summarize/")
def summarize_text(input: TextInput):
    if len(input.text) < 50:
        raise HTTPException(status_code=400, detail="Text is too short")
    
    summary = summarize(input.text, input.num_sentences)
    return {"summary": summary}
