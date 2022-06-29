from getgauge.python import step
from framework.actions.rest_actions import RestActions
from getgauge.python import Messages

request = RestActions.open_rest_client()
title = None

@step("When I run the user request API")
def when_i_run_the_user_request_api():
    global title        
    headers =  {"Content-Type":"application/json"}
    response = RestActions.get("todos/1",headers)
    RestActions.statusCode = response.status_code    
    message = "Status code is - {0}"
    Messages.write_message(message.format(RestActions.statusCode))   
    print(response.json())
    json_data = response.json()
    title = json_data['title']
    message = "Response is - {0}"
    Messages.write_message(message.format(json_data))    

@step("Then verify the success response from user API")
def then_verify_the_success_response_from_user_api():
    assert RestActions.statusCode == 200, "Status code is not 200"
    assert title =='delectus aut autem', "Title is not matching" 

@step("When I run the post request API")
def when_i_run_the_post_request_api():
    headers =  {"Content-Type":"application/json"}
    data = {"userId": 1, "title": "Buy milk", "completed": False}
    response = RestActions.post("todos", data, headers)
    RestActions.statusCode = response.status_code      
    message = "Status code is - {0}"
    Messages.write_message(message.format(RestActions.statusCode))  
    message = "Response is - {0}"
    Messages.write_message(message.format(response.json()))     

@step("Then verify the success response from post API")
def then_verify_the_success_response_from_post_api():
    assert RestActions.statusCode == 201, "Status code is not 201"