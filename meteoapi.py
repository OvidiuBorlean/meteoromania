import requests
import json
import pprint


starevreme = requests.get("http://www.meteoromania.ro/wp-json/meteoapi/v2/starea-vremii", params = {"properties" : ""})
output = starevreme.json()
print (output.keys())
keys1 = output["features"]
for item in keys1:
   keys2 = item["properties"]
   if keys2["nume"] == "TIMISOARA":
      print(keys2["nume"])
      print(keys2["tempe"])
   