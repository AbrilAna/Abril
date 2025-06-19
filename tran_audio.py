import requests

# Ruta al archivo (¡usá doble barra \\ si hay espacios!)
ruta_audio = r"C:\Users\PC 1\Desktop\IAs\aparte\audio.ogg"

# Endpoint del servidor Whisper
url = "http://186.182.14.98:3000/transcribe"

# Abrimos el archivo en modo binario
with open(ruta_audio, 'rb') as f:
    files = {'audio': f}
    response = requests.post(url, files=files)

# Mostramos el resultado
print("Código de respuesta:", response.status_code)

try:
    print("Texto:")
    print(response.json()['text'])
except Exception as e:
    print("No se pudo decodificar JSON:", e)
    print(response.text)
