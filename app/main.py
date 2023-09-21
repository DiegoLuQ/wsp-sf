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
        
        text = text.lower()
        listData = []
        if "hola" in text:
            data = util.TextMessage("Hola soy Sanbot, tu asistente virtual.", number)
            dataButtons = util.ButtonsParaNavegar(number)
            listData.append(data)
            listData.append(dataButtons)
        elif "informacion" in text:
            
            dataInicio = util.TextMessage("Porsupuesto, te puedo enviar informacion sobre SF", number)
            dataOpciones = util.ListMessage(number)
            listData.append(dataInicio)
            listData.append(dataOpciones)
            if "sucursal" in text:
                data = util.TextMessage("Aqui te dejo la direccion de nuestra sucursal", number)
                dataLocation = util.LocationMessage(number)
                listData.append(data)
                listData.append(dataLocation)
            elif "contacto" in text:
                data = util.TextMessage("*Centro de Contacto*:\n981732415", number)
                listData.append(data)

            
        elif "buscar filtro" in text:
            handle_search_product(number, text)


        else:
            data = util.TextMessage("No entiendo. Por favor, envía 'hola' para comenzar.", number)
            listData.append(data)

        for item in listData:
            whatsappservice.SendMessageWhatsapp(item)

        # ProcessMessages(text, number)
        # print(dataUser)
        print(f"Texto recibido: {text}")
        return "EVENT_RECEIVED"
        
    except Exception as e:
        return "EVENT_RECEIVED"

def handle_information(number, text):
    print(f"En handle_information con texto: {text}")
    listData = []
    text = text.lower()
    if "informacion" in text:
        dataInicio = util.TextMessage("Porsupuesto, te puedo enviar informacion sobre SF", number)
        dataOpciones = util.ListMessage(number)
        listData.append(dataInicio)
        listData.append(dataOpciones)
    elif "sucursal" in text:
        data = util.TextMessage("Aqui te dejo la direccion de nuestra sucursal", number)
        dataLocation = util.LocationMessage(number)
        listData.append(data)
        listData.append(dataLocation)

    elif "contacto" in text:
        data = util.TextMessage("*Centro de Contacto*:\n981732415", number)
        listData.append(data)

    for item in listData:
        whatsappservice.SendMessageWhatsapp(item)

    


def handle_search_product(number, text):
    print(f"En handle_search_product con texto: {text}")
    listData = []
    text = text.lower()
    if "buscar filtro" in text:
        dataInicio = util.TextMessage("Porsupuesto, aqui tienes opciones para buscar sobre nuestros productos", number)
        dataButtons = util.ButtonsMessageProducts(number)
        listData.append(dataInicio)
        listData.append(dataButtons)

    elif "cotizar" in text:
        data = util.ButtonsMessage(number)
        listData.append(data)

    elif "ver catalogo" in text:
        data = util.TextMessage("www.santiagofiltros.cl", number)
        listData.append(data)

    for item in listData:
        whatsappservice.SendMessageWhatsapp(item)
    
    
if(__name__ == "__main__"):
    app.run(host='0.0.0.0', debug=True, port=94)