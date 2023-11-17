
Whisper API:
- text to speech.

OpenAI API:


FastAPI :D   
- uvicorn is a server.


```
pip install fastapi
pip install uvicorn
pip install openai
```

/docs == swagger UI  

platform.openai.com  
manage account  

got to here before failing to get credits:  
https://youtu.be/4y1a4syMJHM?t=432


```
pip install python-dotenv
pip install python-multipart
```

https://platform.openai.com/docs/libraries/libraries  
https://platform.openai.com/docs/guides/speech-to-text  

Use postman.  
```
POST
localhost:8000/talk
form data: file
KEY: file

```

Stop at:
```
    raise self._make_status_error_from_response(err.response) from None
openai.RateLimitError: Error code: 429 - {'error': {'message': 'You exceeded your current quota, please check your plan and billing details.', 'type': 'insufficient_quota', 'param': None, 'code': 'insufficient_quota'}}
```
