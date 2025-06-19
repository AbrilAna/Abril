import requests

def pregunta_ia (prompt, model="llama3.2:latest"): 
    url = "http://186.182.14.98:11434/api/generate"
    data = {
        "model": model,
        "prompt" : prompt,
        "stream" : False
    }
    response = requests.post(url, json=data)
    return response.json()["response"]


if __name__ == '__main__':
    while True :
        prompt = input ("Hola! Cual es tu pregunta?"  )
        respuesta = pregunta_ia (prompt)
        print(f"IA: {respuesta}") 