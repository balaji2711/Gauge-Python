from getgauge.python import step
from step_impl.actions.websocket_actions import WebsocketActions

@step("When I tests a valid socket connection")
def when_i_tests_a_valid_socket_connection():  
    WebsocketActions.create_connection()  
    WebsocketActions.receive()
    print("Sending 'Hello, World'...")
    WebsocketActions.send("Hello, World")       

@step("Then connection should be established")
def then_connection_should_be_established():
    print("Receiving...")
    result =  WebsocketActions.receive()
    print("Received '%s'" % result)
    WebsocketActions.close()