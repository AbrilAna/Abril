import requests
import base64
import os

url_transcrip = "http://186.182.14.98:3000/transcribe"
url = "http://186.182.14.98:11434/api/generate"

def transcribir_audio():

    texto = transcribir_audio
    
    datos = extraer_datos(texto)

    if not all(datos.values()):
        return "No se pudo extraer toda la información necesaria. Por favor, revise el audio."

    if datos["informe"] not in ["C-ECC", "P-ECC", "P-CSCC", "C-CSCC"]:
        return "Tipo de informe inválido."
    
    informe_generado = generar_informe(datos)
    
    link = guardar_y_obtener_link(informe_generado)
    
    return f"Informe generado correctamente. Podés descargarlo aquí: {link}"



def enviar(mensaje):

    payload = {
        "model" : "llama3.2"
        "messages" [
            {
            "role" : "user", 
            "content" : mensaje
            }
        ]
    }

def procesar_audio_con_chat(audio_path):
    with open(audio_path, "rb") as f:
        audio_bytes = f.read()
