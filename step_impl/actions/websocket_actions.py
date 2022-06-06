import websocket
import os, ssl

webSocketUrl = os.getenv('webSocketUrl')

class WebsocketActions(): 
    ws = None
    websocket.enableTrace(True)

    def create_connection():
        global ws
        websocket.enableTrace(True)
        ws = websocket.create_connection(webSocketUrl)
        return ws

    def add_sub_protocol():
        global ws
        websocket.enableTrace(True)
        ws = websocket.create_connection("",subprotocols=[""])
        return ws
    
    def send(message):
        return ws.send(message)        

    def receive():
        return ws.recv()  

    def close():
        ws.close()

    def create_ssl_certificate():
        if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
            ssl._create_default_https_context = ssl._create_unverified_context