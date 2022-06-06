import os
import requests

class RestActions():    
    apiBaseUrl = os.getenv('apiBaseURL')
    request = None
    global response, statusCode 

    def open_rest_client():
        global request
        request = requests
        return request

    def get(url, headers):        
        return request.get(url, headers = headers)  

    def post(url, data, headers):        
        return request.post(url, json = data, headers = headers)  

    def put(url, data, headers):        
        return request.put(url, json = data, headers = headers)

    def patch(url, data, headers):        
        return request.patch(url, json = data, headers = headers)
    
    def delete(url, headers):        
        return request.delete(url, headers = headers)