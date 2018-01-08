import json
import urllib.parse,urllib.request,urllib.error

serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"

while True:
	address = input("Enter location: ")
	if len(address)<1:
		break

	url = serviceurl + urllib.parse.urlencode({"address":address})

	print("Retrieving:",url)
	jsn = urllib.request.urlopen(url)
	data = jsn.read().decode()
	print("Retrieved",len(data),"characters")

	try:
		js = json.loads(data)
	except:
		js = None

	if not js or 'status' not in js or js['status'] != 'OK':
		print("Failure To Retrieve".center(50,"="))
		print(data)
		continue

	print(json.dumps(js, indent=4)) #this line pretty prints the list of dictionaries with indents
	#json.dumps is the opposite of json.loads

	lat = js["results"][0]["geometry"]["location"]["lat"]
	lng = js["results"][0]["geometry"]["location"]["lng"]
	print("Latitude:",lat,"Longitude",lng)
	location = js["results"][0]["formatted_address"]
	print("Location:",location)
