#!/usr/bin/python3

import json
import requests
from lib.parsenv import load

envs = load()
BASE_URL = 'https://api.nasa.gov'

def test(endpoint, param_str=""):
  URL = f'{BASE_URL}{endpoint}?{param_str}&API_KEY={envs["NASA_API_KEY"]}'

  response = requests.get(URL)

  if response.status_code == 200:
    return response.text
  else: 
    return 'Error'


if __name__ == "__main__":
  print(test('/neo/rest/v1/feed', 'start_date=2021-01-01'))