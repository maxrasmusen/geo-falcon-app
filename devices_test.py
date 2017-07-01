import httplib as http
import unittest

class TestDevicesResponse(unittest.TestCase):

  def test_get_correct_response(self):
    conn = http.HTTPConnection('localhost:8000')
    conn.request("GET", "/devices", "", {"device_name": "ct"})
    self.assertEqual(conn.getresponse().read(), "Legacy Legato CT transmitter")

unittest.main()

