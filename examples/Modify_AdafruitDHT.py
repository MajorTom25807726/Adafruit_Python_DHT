#/usr/bin/python3
import time
import sys
import http.client as http
Import urllib
import json
deviceId = "DzuLn9tM"
deviceKey = "z3o9tOcB0I3Dgy0h" 
def post_to_mcs(payload): 
	headers = {"Content-type": "application/json", "deviceKey": deviceKey} 
	not_connected = 1 
	while (not_connected):
		try:
			conn = http.HTTPConnection("api.mediatek.com:80")
			conn.connect() 
			not_connected = 0 
		except (http.HTTPException, socket.error) as ex: 
			print ("Error: %s" % ex)
 			time.sleep(10)
			 # sleep 10 seconds 
	conn.request("POST", "/mcs/v2/devices/" + deviceId + "/datapoints", json.dumps(payload), headers) 
	response = conn.getresponse() 
	print( response.status, response.reason, json.dumps(payload), time.strftime("%c")) 
	data = response.read() 
	conn.close() 

	while true:
		h0, t0= Adafruit_DHT.read_retry(sensor, pin)
		if h0 is not None and t0 is not None:
			print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(t0, h0))

			payload = {"datapoints":[{"dataChnId":"Humidity","values":{"value":h0}},{"dataChnId":"Temperature","values":{"value":t0}}]} 
			post_to_mcs(payload)
			time.sleep(10) 

		else:
			print('Failed to get reading. Try again!')
			sys.exit(1)


