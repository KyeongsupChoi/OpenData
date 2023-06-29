import pandas as pd
import requests
import xml.etree.ElementTree as ET
import json
import csv

# Load password from fil in gitignore
passcode = pd.read_csv('passcode.csv', index_col=0)
passcodey = passcode.iloc[0][0]

# Ultra short Korea now cast API address
URL = "https://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst"

# Parameters for api call
PARAMS = {'serviceKey': passcodey,
          'numOfRows': 10,
          'pageNo': 1,
          'base_date': 20230629,
          'base_time': '0600',
          'dataType': 'JSON',
          'nx': 55,
          'ny': 127}

# Get request to api address with parameters
r = requests.get(url=URL, params=PARAMS)

# Load json content
jsondata = json.loads(r.content)

# Select body content
jsondata = jsondata['response']['body']['items']['item']

# Open csv file
data_file = open('Gjsonoutput.csv', 'w', newline='')

# Initialize csv writer
csv_writer = csv.writer(data_file)

# Write to csv
count = 0
for data in jsondata:
    if count == 0:
        header = data.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(data.values())

data_file.close()

