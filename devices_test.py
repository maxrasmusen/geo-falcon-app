import devices_test_object as dto
import unittest

class TestDevicesResponse(unittest.TestCase):
 
  def test_get_correct_response(self):
    devices_request = dto.DevicesRequestWrapper()
    self.assertEqual(devices_request.getsingledevice('ct'), 'Legacy Legato CT transmitter')
    
    

unittest.main()

