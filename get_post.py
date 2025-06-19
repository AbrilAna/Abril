import requests

def hacer_get(url):
    response = requests.get(url)
    try: 
        return response.json()
    except:
        return response.text

def hacer_post(url, data):  
    response = requests.post(url, json=data)
    return response.json()
