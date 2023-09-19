import requests
import json

def SendMessageWhatsapp(data):
    try:
        token = "EAAJnnqzxiNoBO1pgyHiDLa5Kts2IkZAd15OEooEemwqhJ4OxpZAtZBerxU6VDAbTaX1302lbugkvFYwQPZAgW5Vvj0X8dIIfnZBKflFYVpVHjYWgUDKCZAo9tmHzALHTB8cVcAhpWzvNCvOp4hxB55reXjnUYA2OPUac0b8NTwqKGg4peev2VAhwKW8G9nx25k"
        api_url = "https://graph.facebook.com/v17.0/133381839854669/messages"
        headers = {"Content-Type":"application/json", "Authorization":"Bearer " + token}
        response = requests.post(api_url, data = json.dumps(data), headers = headers)

        if response.status_code == 200:

            return True
        
        return False
    except Exception as e:
        raise e