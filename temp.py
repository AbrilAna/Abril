

from tran_audio import transcribe
from tpmy import pjson

from tpmy import encode64


url = 'http://186.182.14.98:3001/transcribe'

audio_url = 'https://drive.conversana.com/files/conversations/35/2025/6/13/PIp1j5LT.ogg'

audio_path = r'c:\tpmy\audio.ogg'

with open(audio_path, "rb") as f:
    audio = f.read()

audio_b64 = encode64(audio)


respuesta = transcribe(audio_url)

pjson(respuesta)


