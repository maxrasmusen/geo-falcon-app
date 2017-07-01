import httplib 

class DevicesRequestWrapper:

  def __init__(self):
    self.conn = httplib.HTTPConnection('localhost:8000')

  def getsingledevice(self, device_name):
    self.conn.request("GET", "/devices", "", {"device_name": device_name})
    return self.conn.getresponse().read()