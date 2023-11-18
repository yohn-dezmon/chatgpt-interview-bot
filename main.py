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
    # transcript = {"role": "user", "content": "Who won the world series in 2020?"}
    print(transcript)
    return transcript

def get_chat_response(user_message: Dict[str, str]):
    messages = load_messages()
    messages.append({"role": "user", "content": user_message.text})

    # Send to ChatGPT/OpenAI
    # gpt_response = {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."}
    gpt_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    # not sure if it should be index[0] or just choices[0]
    parsed_gpt_response = gpt_response.choices[0].message.content
    print(gpt_response)
    # Save messages
    save_messages(user_message.text, parsed_gpt_response)



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

def save_messages(user_message, gpt_response):
    file = 'database.json'
    messages = load_messages()
    # save prompt + response 
    messages.append(user_message)
    messages.append(gpt_response)
    with open(file, 'w') as f:
        json.dump(messages, f)
    
    
