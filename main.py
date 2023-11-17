# Send audio and have it transcribed


# Send transcription to chatgpt and get a response


# Save the chat history to send back and forth for context 



from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
