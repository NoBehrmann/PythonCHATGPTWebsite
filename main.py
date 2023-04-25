import js

import os
import requests

import pyodide_http

# Patch the requests library so it works with Pyscript
pyodide_http.patch_all()

OPENAI_API_KEY = input()

url = "https://api.openai.com/v1/chat/completions"
headers = {"Content-Type": "application/json",
           "Authorization": f"Bearer {OPENAI_API_KEY}"}

messages = []
print("What type of chatbot would you like to create? ")

def send():
    userElement = js.document.getElementById('userInput')
    message = userElement.value
    userElement.value = ""
    
    if len(messages) == 0:
        print("> " + message)
        messages.append({"role": "system", "content": message})
        print("Say hello to your new assistant!")
        return

    print("> " + message)
    messages.append({"role": "user", "content": message})

    data = {"model": "gpt-3.5-turbo", "messages": messages}
    response = requests.post(url, headers=headers, json=data)
    
    reply = response.json()["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")
