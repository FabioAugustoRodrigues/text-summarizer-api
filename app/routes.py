from fastapi import APIRouter

router = APIRouter()

@router.post("/summarize/")
def summarize_text():
    return "Hello World"
