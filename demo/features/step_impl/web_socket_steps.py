from getgauge.python import step
from framework.actions.websocket_actions import WebsocketActions
from getgauge.python import Messages


@step("When I connect to websocket")
def when_i_connect_to_websocket():
    WebsocketActions.create_connection()  
    WebsocketActions.receive()
    print("Sending 'Hello, World'...")
    WebsocketActions.send("Hello, World")   
    Messages.write_message("Sent Hello World")         

@step("Then verify the websocket response")
def then_verify_the_websocket_response():
    print("Receiving...")
    result =  WebsocketActions.receive()
    print("Received '%s'" % result)
    message = "Received - {0}"
    Messages.write_message(message.format(result))   
    WebsocketActions.close()
    