# Send audio and have it transcribed


# Send transcription to chatgpt and get a response


# Save the chat history to send back and forth for context 
import os

import openai
from openai import OpenAI
from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile


load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("OPEN_AI_ORG")

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/talk")
async def post_audio(file: UploadFile):
    # convert audio to text
    
    client = OpenAI()
    # UploadFile by default uploads to file.filename
    audio_file = open(file.filename, "rb")
    # client.audio.transcriptions.create
    transcript = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
    )
    print(transcript)

