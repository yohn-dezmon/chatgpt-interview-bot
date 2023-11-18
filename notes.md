
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
https://youtu.be/4y1a4syMJHM?t=806


Documentation > Capabilities > Chat Completions  
(different than video)  

Everytime you submit text to ChatGPT, if you have previous text in your chat, you resend the entire chat history. Otherwise ChatGPT doesn't have memory.  

Within our app, we need to create a kind of "database" to store chat history.  

if "database"/history is empty, we always provide an initial context for the ChatGPT session!  

Stop here:  
https://youtu.be/4y1a4syMJHM?t=1593  
Stop at removing hard coded data.



