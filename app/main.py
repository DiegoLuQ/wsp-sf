
from flask import Flask, request
import util
import whatsappservice
app = Flask(__name__)

@app.route('/welcome', methods=['GET'])
def index():
    return "welcome developer"

@app.route('/whatsapp', methods=['GET'])
def VerifyToken():
    try:
        access_token = "asd7s7s8a5s4d8asd5"
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if token != None and challenge != None and token == access_token:
            return challenge
        else:
            return "", 400
    except:
        return "", 400

@app.route('/whatsapp', methods=['POST'])
def ReceivedMessage():
    try:
        body = request.get_json()
        entry = (body["entry"])[0]
        changes = (entry["changes"])[0]
        value = changes["value"]
        message = (value["messages"])[0]
        idWA=( body['entry'])[0]['changes'][0]['value']['messages'][0]['id']
        number = message["from"]
        dataUser = {
            "id": idWA,
            "body": body,
            "changes": changes,
            "value":value,
            "message":message,
            "number":number
        }
        text = util.GetTextUser(message)

        ProcessMessages(text, number)
        # print(dataUser)
        return "EVENT_RECEIVED"
        
    except Exception as e:
        raise "EVENT_RECEIVED"

def ProcessMessages(text,number):
    text = text.lower()
    listData = []

    if "hola" in text:
        data = util.TextMessage("Hola soy Sanbot, tu asistente virtual. Te dejo opciones", number)
        dataButtons = util.ListMessage(number)
        listData.append(data)
        listData.append(dataButtons)

    elif "sucursal" in text:
        data = util.TextMessage("Aqui te dejo la direccion de nuestra sucursal", number)
        dataLocation = util.LocationMessage(number)
        listData.append(data)
        listData.append(dataLocation)

    elif "contacto" in text:
        data = util.TextMessage("*Centro de Contacto*:\n981732415", number)
        listData.append(data)

    elif "aire" in text:
        data = util.ButtonsMessageProducts(number)
        listData.append(data)

    elif "aceite" in text:
        data = util.ButtonsMessageProducts(number)
        listData.append(data)

    elif "filtro de combustible" in text:
        data = util.ButtonsMessageProducts(number)
        listData.append(data)

    elif "cotizar" in text:
        data = util.ButtonsMessage(number)
        listData.append(data)

    elif "ver catalogo" in text:
        data = util.TextMessage("www.santiagofiltros.cl", number)
        listData.append(data)

    elif "buscar filtro" in text:
        data = util.TextMessage("www.santiagofiltros.cl/buscar", number)
        listData.append(data)

    elif "gracias" in text:
        data = util.TextMessage("gracias por contactarme", number)

        listData.append(data)
    else:
        data = util.TextMessage("lo siento, no puedo entenderte", number)
        listData.append(data)

    for item in listData:
        whatsappservice.SendMessageWhatsapp(item)
    
def GenerateMessage(text, number):
    text = text.lower()

    if "text" in text:
        data = util.TextMessage("text", number)
    if "format" in text:
        data = util.TextFormatMessage(number)
    if "image" in text:
        data = util.ImageMessage(number)
    if "video" in text:
        data = util.VideoMessage(number)
    if "audio" in text:
        data = util.AudioMessage(number)
    if "document" in text:
        data = util.DocumentMessage(number)
    if "location" in text:
        data = util.LocationMessage(number)
    if "button" in text:
        data = util.ButtonsMessage(number)
    if "list" in text:
        data = util.ListMessage(number)
    
    whatsappservice.SendMessageWhatsapp(data)

if(__name__ == "__main__"):
    app.run(host='0.0.0.0', debug=True, port=94)