from tpmy import encode64
from tran_audio import transcribe
import re

url_transcrip = "http://186.182.14.98:3001/transcribe"
url = "http://186.182.14.98:11434/api/chat"
audio_path = r"C:\Users\PC 1\Desktop\mi_libreria\audio.ogg"

'''
def extraer(texto):
    cuit_match = re.search(r"\b(\d{2})-?(\d{8})-?(\d)\b", texto)
    clave_match = re.search(r"clave\s+(\w+)", texto, re.IGNORECASE) 

    tipo = None
    if "estado de cuenta corriente" in texto and "cliente" in texto:
        tipo = "C-ECC"
    elif "estado de cuenta corriente" in texto and "proveedor" in texto:
        tipo = "P-ECC"s
        tipo = "C-CSCC"
    elif "composición de saldos" in texto and "proveedor" in texto:
        tipo = "P-CSCC"

    return {
        "CUIT": "".join(cuit_match.groups()) if cuit_match else None,
        "clave": clave_match.group(1) if clave_match else None,
        "informe": tipo
    }
'''
def proceso_completo(audio_path):
    
    audio_b64 = encode64(audio_path)
    texto = transcribe(audio_b64)
    #datos = extraer(texto)
    return texto

if __name__ == "__main__":
    resultado = proceso_completo (audio_path)
    print ("Resultado final:\n", resultado)
