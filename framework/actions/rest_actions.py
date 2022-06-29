import os
import requests


apiBaseUrl = os.getenv('apiBaseURL')

class RestActions:  
    asajiUri = None  
    request = None
    global response, statusCode

    def open_rest_client():
        global request
        request = requests

    def get(url, headers): 
        return request.get(apiBaseUrl + url, headers = headers)  

    def post(url, data, headers):        
        return request.post(apiBaseUrl + url, json = data, headers = headers)  

    def put(url, data, headers):        
        return request.put(apiBaseUrl + url, json = data, headers = headers)

    def patch(url, data, headers):        
        return request.patch(apiBaseUrl + url, json = data, headers = headers)
    
    def delete(url, headers):        
        return request.delete(apiBaseUrl + url, headers = headers)