import xml.etree.ElementTree as et
import re

class XMLReader():

  def __init__(self):
    minischema = et.parse('mini-schema.xml')
    self.devices = minischema.getroot().find('devices')

  def get_single_device_notes(self, device_name):
      
      # Iterate through all devices. Return the notes if names match
      for device in self.devices.findall('device'):
        d = device.find('name').text
        if d == device_name:
          notes = device.find('notes').text
          # Remove tabs, CRs and newlines from notes, replacing newlines with spaces. Remove extra whitespace around edge.
          notes = self.strip_whitespace(notes)
          return notes

      # If we get here none have matched. 
      return False

  def get_all_devices(self):
    all_devices = []
    for device in self.devices.findall('device'):
      name = device.find('name').text
      value = device.find('value').text
      notes = self.strip_whitespace(device.find('notes').text)
      dict = {'name': name, 'value': value, 'notes': notes}
      all_devices.append(dict)
    return all_devices

  def strip_whitespace(self, notes):
    
    notes = re.sub(r'[\t\r]', r'', notes)
    notes = re.sub(r'\n', r' ', notes)
    notes = notes.strip()
          
    return notes