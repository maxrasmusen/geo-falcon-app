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


suite = unittest.TestLoader().loadTestsFromTestCase(TestDevicesResponse)
colour_runner.runner.ColourTextTestRunner().run(suite)

