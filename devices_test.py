import devices_test_object as dto
import unittest
import colour_runner.runner

class TestDevicesResponse(unittest.TestCase):
  
  def setUp(self):
    self.devices_request = dto.DevicesRequestWrapper()

  def test_response_when_single_line(self):
    self.assertEqual(self.devices_request.get_single_device_body('ct'), 'Legacy Legato CT transmitter')
    
  def test_response_when_multi_line(self):
    self.assertEqual(self.devices_request.get_single_device_body('hub_ethernet_cosy_generic'), "Generic hub to connect to Cosy servers and perform fast firmware download. Used to deploy hub firmware at the point of installation.")

  def test_response_when_does_not_exist(self):
    self.assertEqual(self.devices_request.get_single_device_status('i don\'t exist'), 404)

  def test_create_single_device(self):
    response = self.devices_request.create_single_device_body('test_device', 'a cool description')
    self.assertEqual(response["name"], "test_device")
    self.assertEqual(response["notes"], "a cool description")

  def test_create_bad_request(self):
    self.assertEqual(self.devices_request.create_single_device_status_bad(), 400)

  def test_get_all_devices_length(self):
    self.assertEqual(len(self.devices_request.get_all_devices()), 31)

  # Just check the first device to see if it contains the right information
  def test_get_all_devices_content(self):
    hub_ethernet_cosy = self.devices_request.get_all_devices()[0]
    self.assertEqual(hub_ethernet_cosy["name"], "hub_ethernet_cosy")
    self.assertEqual(hub_ethernet_cosy["value"], "0")
    self.assertEqual(hub_ethernet_cosy["notes"], "Cosy hub, Ethernet microcontroller")



suite = unittest.TestLoader().loadTestsFromTestCase(TestDevicesResponse)
colour_runner.runner.ColourTextTestRunner().run(suite)

