def GetTextUser(message):
    text =""
    typeMessage = message["type"]

    if typeMessage == "text":
        text = (message["text"])["body"]
    elif typeMessage == "interactive":
        interactiveObject = message["interactive"]
        typeInteractive = interactiveObject["type"]
        if typeInteractive == "button_reply":
            text = (interactiveObject["button_reply"])["title"]
        elif typeInteractive == "list_reply":
            text = (interactiveObject["list_reply"])["title"]
        else:
            print("sin mensaje interactivo")
    else:
        print("sin mensaje")
    
    return text

def TextMessage(text, number):
    data = {
                "messaging_product": "whatsapp",    
                "recipient_type": "individual",
                "to": number,
                "type": "text",
                "text": {
                    "body": text
                }
            }
    
    return data

def TextFormatMessage(number):
    data = {
                "messaging_product": "whatsapp",    
                "recipient_type": "individual",
                "to": number,
                "type": "text",
                "text": {
                    "body": "Hola *Diego*" # "" _Luque_ - ~Linares~ - ```Hello``` "
                }
            }
    
    return data

def ImageMessage(number):
    data = {
                "messaging_product": "whatsapp",    
                "to": number,
                "type": "image",
                "image": {
                    "link": "https://i.postimg.cc/4xzJdjY2/Personal-Portafolio.jpg"     
                }
            }
    
    return data

def AudioMessage(number):
    data = {
                "messaging_product": "whatsapp",    
                "to": number,
                "type": "audio",
                "audio": {
                    "link": "https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/audio_whatsapp.mp3"     
                }
            }
    
    return data

def VideoMessage(number):
    data = {
                "messaging_product": "whatsapp",    
                "to": number,
                "type": "video",
                "video": {
                    "link": "https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/video_whatsapp.mp4"     
                }
            }
    
    return data

def DocumentMessage(number):
    data = {
                "messaging_product": "whatsapp",    
                "to": number,
                "type": "document",
                "document": {
                    "link": "https://biostoragecloud.blob.core.windows.net/resource-udemy-whatsapp-node/document_whatsapp.pdf",
                    "caption":"Services",
                    "filename":"Services SF"     
                }
            }
    
    return data

def LocationMessage(number):
    data = {
            "messaging_product": "whatsapp",
            "to": number,
            "type":"location",
            "location": {
                "latitude":"-20.288523125969466",
                "longitude":"-70.10427668484094",
                "name":"SantiagoFiltros - Al por mayor",
                "address":"Gabriela mistral con, Venezuela 4237, Alto Hospicio, Tarapacá"
            }
        }
    
    return data

def ButtonsMessage(number):
    data = {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": number,
                "type": "interactive",
                "interactive": {
                    "type": "button",
                    "body": {
                        "text": "¿Acceder😊?"
                    },
                    "action": {
                        "buttons": [
                            {
                                "type": "reply",
                                "reply": {
                                    "id": "001",
                                    "title": "✅ Sign up"
                                }
                            },
                            {
                                "type": "reply",
                                "reply": {
                                    "id": "002",
                                    "title": "❌ Login"
                                }
                            }
                        ]
                    }
                }
            }
    
    return data


def ButtonsParaNavegar(number):
    data = {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": number,
                "type": "interactive",
                "interactive": {
                    "type": "button",
                    "body": {
                        "text": "¿Como deseas Navegar😊?"
                    },
                    "action": {
                        "buttons": [
                            {
                                "type": "reply",
                                "reply": {
                                    "id": "003",
                                    "title": "Buscar Filtro"
                                }
                            },
                            {
                                "type": "reply",
                                "reply": {
                                    "id": "002",
                                    "title": "Informacion"
                                }
                            }
                        ]
                    }
                }
            }
    
    return data


def ButtonsMessageProducts(number):
    data = {
                "messaging_product": "whatsapp",
                "recipient_type": "individual",
                "to": number,
                "type": "interactive",
                "interactive": {
                    "type": "button",
                    "body": {
                        "text": "¿Qué desea saber😊?"
                    },
                    "action": {
                        "buttons": [
                            {
                                "type": "reply",
                                "reply": {
                                    "id": "001",
                                    "title": "✅ Ver Catalogo"
                                }
                            },
                            {
                                "type": "reply",
                                "reply": {
                                    "id": "002",
                                    "title": "🔎 Buscar Filtro"
                                }
                            }
                        ]
                    }
                }
            }
    
    return data

def ListMessage(number):
    data = {
    "messaging_product": "whatsapp",
    "to": number,
    "type": "interactive",
    "interactive": {
        "type": "list",
        "body": {
            "text": "✅ Navegar por este Chat"
        },
        "footer": {
            "text": "Selecciona una opción"
        },
        "action": {
            "button": "Navegar",
            "sections": [
                {
                    "title": "Que Filtro Busca?",
                    "rows": [
                        {
                            "id": "main-aire",
                            "title": "Aire",
                            "description": "Filtros de Aire de diferentes Marcas"
                        },
                        {
                            "id": "main-aceite",
                            "title": "Aceite",
                            "description": "Filtros de Aceite de diferentes Marcas"
                        },
                        {
                            "id": "main-combustible",
                            "title": "Filtro de Combustible",
                            "description": "Filtros de Combustible de diferentes Marcas"
                        }
                    ]
                },
                {
                    "title": "📍Centro de Contacto",
                    "rows": [
                        {
                            "id": "main-agency",
                            "title": "sucursal",
                            "description": "Your can visit our agency"
                        },
                        {
                            "id": "main-contact",
                            "title": "contacto",
                            "description": "One of our agents will assist you"
                        }
                    ]
                }
            ]
        }
    }
}
    
    return data