from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai
import datetime
import os

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model = genai.GenerativeModel("gemini-1.5-flash")

class ChatRequest(BaseModel):
    message: str
@app.get("/")
def home():
    return {"status": "ALTRON API ONLINE!", "version": "2.0"}

@app.get("/time")
def get_time():
    now = datetime.datetime.now()
    return {"time": now.strftime("%I:%M %p"), "date": now.strftime("%d %B %Y")}

@app.post("/chat")
def chat(req: ChatRequest):
    response = model.generate_content(
        f"Tu ALTRON hai - ek powerful Hindi AI assistant. Pyaar se jawab de. {req.message}"
    )
    return {"reply": response.text}
