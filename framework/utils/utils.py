from datetime import datetime
import gzip
import base64
from getgauge.python import custom_screenshot_writer
import os
from uuid import uuid1
import json
import xmltodict
import pyodbc

class Utils:
    def get_zoned_date_time():
        today = datetime.now()
        zonedDateTime = today.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]+'Z'
        return zonedDateTime

    def compress(request):
         return gzip.compress(bytes(request))
    
    def decompress(request):
        return gzip.decompress(request)
    
    def base64_encode(message):
        return base64.b64encode(message)
    
    def base64_decode(message):
        return base64.b64decode(message)  

    def decode(message):
        return message.decode("utf-8")

    def parse_xml(result):
        parseXml = xmltodict.parse(result)
        parseXml = json.dumps(parseXml)  
        parseXml = json.loads(parseXml)
        return parseXml

    @custom_screenshot_writer
    def take_screenshot(driver, path):
        image = driver.get_screenshot_as_png()
        file_name = os.path.join(os.getenv("gauge_reports_dir") + path, "screenshot-{0}.png".format(uuid1().int))
        file = open(file_name, "wb")
        file.write(image)
        return os.path.basename(file_name)    

    def read_data_from_database(servername, database, username, password, query):
        conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                      'Server='+servername+';'
                      'Database='+database+';'
                      'uid='+username+';pwd='+password)
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor