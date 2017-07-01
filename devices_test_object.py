import httplib 
import json

class DevicesRequestWrapper:

  def __init__(self):
    self.conn = httplib.HTTPConnection('localhost:8000')

  def get_single_device_body(self, device_name):
    self.conn.request("GET", "/devices", "", {"device_name": device_name})
    body = self.conn.getresponse().read()
    return json.loads(body)["notes"]

  def get_single_device_status(self, device_name):
    self.conn.request("GET", "/devices", "", {"device_name": device_name})
    return self.conn.getresponse().status