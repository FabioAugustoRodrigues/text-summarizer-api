from fastapi import FastAPI
from app.routes import router

import nltk

nltk.download('punkt_tab')

app = FastAPI(
    title="Text Summarizer API",
    description="",
    version="0.1.0"
)

app.include_router(router)