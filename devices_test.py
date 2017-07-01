import httplib as http

conn = http.HTTPConnection('localhost:8000')
conn.request("GET", "/devices", "", {"device-name": "ct"})
if conn.getresponse().read() == "Legacy Legato CT transmitter":
  print "Successful test"
else: 
  print "Failuere"