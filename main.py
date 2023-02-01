import requests

URL= "https://dev.socrata.com/foundry/data.cityofchicago.org/ijzp-q8t.json?year=2022"
PAGE= requests.get(URL)
