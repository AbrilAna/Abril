import requests
from base_datos import obtener_contexto

def pregunta_ia(prompt, model="llama3.2:latest"):
    url = "http://186.182.14.98:11434/api/generate"
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=data)
    return response.json()["response"]

def pregunta_ia_con_datos(pregunta, model="llama3.2:latest"):
    conocimiento = obtener_contexto()
    prompt = (
        f"Usá esta información para responder de forma clara:\n"
        f"{conocimiento}\n\n"
        f"Pregunta del usuario: {pregunta}"
    )
    return pregunta_ia(prompt, model=model)
