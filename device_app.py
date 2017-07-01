import falcon
import xml.etree.ElementTree as et
import re
import json

def get_notes(device_name):
    # Parse xml from file and find 'devices tag'
    minischema = et.parse('mini-schema.xml')
    devices = minischema.getroot().find('devices')

    # Iterate through all devices. Return the notes if names match
    for device in devices.findall('device'):
      d = device.find('name').text
      if d == device_name:
        notes = device.find('notes').text
        # Remove tabs, CRs and newlines from notes, replacing newlines with spaces. Remove extra whitespace around edge.
        notes = strip_whitespace(notes)
        return notes

    # If we get here none have matched. 
    return False

def strip_whitespace(notes):
  
  notes = re.sub(r'[\t\r]', r'', notes)
  notes = re.sub(r'\n', r' ', notes)
  notes = notes.strip()
        
  return notes

class DevicesResource(object): 

    def get_single_device(self, req, res):
      device_name = req.headers['DEVICE-NAME']
        
      notes = get_notes(device_name)
      
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
        notes = strip_whitespace(device.find('notes').text)
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