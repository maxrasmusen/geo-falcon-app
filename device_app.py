import falcon
import xml.etree.ElementTree as et

def get_notes(device_name):
    # Parse xml from file and find 'devices tag'
    devices = et.parse('mini-schema.xml')
    devices = devices.getroot().find('devices')

    # Iterate through all devices. Return the notes if names match
    for device in devices.findall('device'):
      d = device.find('name').text
      if d == device_name:
        return device.find('notes').text

    # If we get here none have matched. 
    return False

class DevicesResource(object): 

    def on_get(self, req, res): 

      # Get device name stored in request head. 
      device_name = req.headers['DEVICE-NAME']
      print device_name
      
      notes = get_notes(device_name)
      
      if notes: 
        res.status = falcon.HTTP_200
        res.body = (notes)
      else: 
        res.status = falcon.HTTP_404
        res.body = "That device cannot be found"

# Start falcon server
app = falcon.API()

# Add instance of devices controller to app
devices = DevicesResource()
app.add_route('/devices', devices)