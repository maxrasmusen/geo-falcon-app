import httplib 
import json

class DevicesRequestWrapper:

  def __init__(self):
    self.conn = httplib.HTTPConnection('localhost:8000')

  def get_single_device_body(self, device_name):
    self.conn.request("GET", "/devices", "", {"device_name": device_name})
    body = self.conn.getresponse().read()
    return self.load_json(body)

  def get_single_device_status(self, device_name):
    self.conn.request("GET", "/devices", "", {"device_name": device_name})
    return self.conn.getresponse().status

  def create_single_device_body(self, name, notes):
    body = json.dumps({
      "name": name,
      "notes": notes
      })

    self.conn.request("POST", "/devices", body)
    return self.load_json(self.conn.getresponse().read())

  def create_single_device_status_bad(self):
    body = json.dumps({
      "naame": "testname",
      "nos": "some notes"
      })

    self.conn.request("POST", "/devices", body)
    return self.conn.getresponse().status

  def get_all_devices(self):
    self.conn.request("GET", "/devices")
    body = self.conn.getresponse().read()
    return self.load_json(body)

  def load_json(self, js):
    try:
      return json.loads(js)
    except ValueError, e:
      return {}