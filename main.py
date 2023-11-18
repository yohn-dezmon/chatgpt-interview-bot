# 1. Send audio and have it transcribed


# 2. Send transcription to chatgpt and get a response


# 3. Save the chat history to send back and forth for context 
import os
import json

import openai
from openai import OpenAI
from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile
from typing import Dict


load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("OPEN_AI_ORG")
client = OpenAI()
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/talk")
async def post_audio(file: UploadFile):
    user_message = transcribe_audio(file)
    chat_response = get_chat_response(user_message)

# Functions 
def transcribe_audio(file: UploadFile) -> Dict[str, str]:
    """convert audio to text."""
    # UploadFile by default uploads to file.filename
    audio_file = open(file.filename, "rb")
    # each API call is $0.01
    transcript = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
    )
    print(transcript)
    return {"message": "Audio has been transcribed"}

def get_chat_response(user_message: Dict[str, str]):
    messages = load_messages()


def load_messages():
    messages = []
    file = 'database.json'
    empty = os.stat(file).st_size == 0

    # if file is not empty, loop through history and add to messages 
    if not empty:
        with open(file) as db_file:
            data = json.load(db_file)
            for item in data:
                messages.append(item)
    else:
        # if file is empty we need to add context (system role)
        messages.append(
            {"role": "system", "content": "You are inerviewing the user for a frontend React developer position. Ask short questions that are relevant to a junior level developer. Your name is Greg, the user is John. Keep responses under 30 words and be funny sometimes."}
        )
    return messages
