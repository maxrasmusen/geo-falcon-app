import falcon
import json
import xml_reader as x
import xml.etree.ElementTree as et
import re

class DevicesResource(object): 

    def __init__(self):
      self.xml_reader = x.XMLReader()

    def get_single_device(self, req, res):
      device_name = req.headers['DEVICE-NAME']
        
      notes = self.xml_reader.get_single_device_notes(device_name)
      
      if notes: 
        res.status = falcon.HTTP_200
        res.body = json.dumps({"name": device_name, "notes": notes})
      else: 
        res.status = falcon.HTTP_404
        res.body = "That device cannot be found"

    def get_all_devices(self, req, res):
      minischema = et.parse('mini-schema.xml')
      devices = minischema.getroot().find('devices')
      all_devices = []
      for device in devices.findall('device'):
        name = device.find('name').text
        value = device.find('value').text
        notes = self.xml_reader.strip_whitespace(device.find('notes').text)
        dict = {'name': name, 'value': value, 'notes': notes}
        print(dict)
        all_devices.append(dict)

      res.status = falcon.HTTP_200
      res.body = json.dumps(all_devices)

    def on_get(self, req, res): 

      # Get device name stored in request head. 
      if 'DEVICE-NAME' in req.headers:
        self.get_single_device(req, res)
      else:
        self.get_all_devices(req, res)

# Start falcon server
app = falcon.API()

# Add instance of devices controller to app
devices = DevicesResource()
app.add_route('/devices', devices)