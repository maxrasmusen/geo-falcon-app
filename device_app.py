import falcon
import xml.etree.ElementTree as et

class DevicesResource(object): 

  def on_get(self, req, res): 

    # Get device name stored in request head. 
    device_name = req.headers['DEVICE-NAME']
    
    # Parse xml from file and find 'devices tag'
    devices = et.parse('mini-schema.xml')
    devices = devices.getroot().find('devices')

    # Iterate through all devices
    for device in devices.findall('device'):
      print(device.find('name').text)

    res.status = falcon.HTTP_200
    res.body = ("HELLO")

# Start falcon server
app = falcon.API()

# Add instance of devices controller to app
devices = DevicesResource()
app.add_route('/devices', devices)