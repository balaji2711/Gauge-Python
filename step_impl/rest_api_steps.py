from getgauge.python import step
from requests import request
from step_impl.actions.rest_actions import RestActions

request = RestActions.open_rest_client()
title = None

@step("I run the user request API")
def i_run_the_user_request_api():
    global title
    api_url = RestActions.apiBaseUrl + "todos/1"
    headers =  {"Content-Type":"application/json"}
    response = RestActions.get(api_url,headers)
    RestActions.statusCode = response.status_code          
    print(response.json())
    json_data = response.json()
    title = json_data['title']
    print(title)

@step("verify the success response from user API")
def verify_the_success_response_from_user_api():
    assert RestActions.statusCode == 200
    assert title =='delectus aut autem'

@step("I run the post request API")
def i_run_the_post_request_api():
    api_url = RestActions.apiBaseUrl + "todos"
    headers =  {"Content-Type":"application/json"}
    data = {"userId": 1, "title": "Buy milk", "completed": False}
    response = RestActions.post(api_url, data, headers)
    RestActions.statusCode = response.status_code        
    print(response.json())

@step("verify the success response from post API")
def verify_the_success_response_from_post_api():
    assert RestActions.statusCode == 201   