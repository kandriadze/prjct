import requests
import json


URL = "https://data.cityofchicago.org/resource/ijzp-q8t2.json?year=2022"
page= requests.get(URL)
print(page.json())

j_string = json.dumps(page.json())
j_file = open("data.json" , "w")
j_file.write(j_string)
j_file.close()

