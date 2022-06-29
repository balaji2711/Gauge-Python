from math import fabs
import websocket
import os
from framework.actions.rest_actions import RestActions
import ssl


webSocketUrl = os.getenv('webSocketUrl')

class WebsocketActions: 
    ws = None
    websocket.enableTrace(True)

    def create_connection():
        global ws
        websocket.enableTrace(True)
        ws = websocket.create_connection(webSocketUrl)
        return ws
    
    def send(message):
        return ws.send(message)        

    def receive():
        return ws.recv()

    def close():
        ws.close()

    def is_open():
        try:
            return ws.connected
        except:
            return False