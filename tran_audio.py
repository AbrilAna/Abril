import requests
import base64
import os

def transcribe(audio):
    url = "http://186.182.14.98:3001/transcribe"

    if audio.startswith("http://") or audio.startswith("https://"):
        data = {"audio": audio}
    else:
        if not os.path.exists(audio):
            return {"error": "Archivo no encontrado"}

        with open(audio, "rb") as f:
            audio_b64 = base64.b64encode(f.read()).decode("utf-8")
        data = {"audio": audio_b64}

    try:
        respuesta = requests.post(url, json=data)
        return respuesta.json()
    except Exception as e:
        return {"error": str(e)}
