import pandas as pd
import requests
import xml.etree.ElementTree as ET
import json
import csv

passcode = pd.read_csv('passcode.csv', index_col=0)
passcodey = passcode.iloc[0][0]

URL = "https://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst"

PARAMS = {'serviceKey': passcodey,
          'numOfRows': 10,
          'pageNo': 1,
          'base_date': 20230628,
          'base_time': '0600',
          'dataType': 'JSON',
          'nx': 55,
          'ny': 127}

r = requests.get(url = URL, params = PARAMS)



jsondata = json.loads(r.content)
data_file = open('Gjsonoutput.csv', 'w', newline='')
csv_writer = csv.writer(data_file)



count = 0
for data in jsondata['response']['body']['items']['item']:
    if count == 0:
        header = data.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(data.values())

data_file.close()

"""
root = ET.fromstring(r.content)

cols = ["baseDate", "baseTime", "category", "nx", "ny", "obsrValue"]
rows = []

rooty = root.get('items')

print(type(root))

baseDate = ''
baseTime = ''
category = ''
nx = ''
ny = ''
obsrValue = ''

for i in root.iter():
    if i.tag == 'baseDate':
        baseDate = i.text
    elif i.tag == 'baseTime':
        baseTime = i.text
    elif i.tag == 'category':
        category = i.text
    elif i.tag == 'nx':
        nx = i.text
    elif i.tag == 'ny':
        ny = i.text
    elif i.tag == 'obsrValue':
        obsrValue = i.text

        rows.append({"baseDate": baseDate,
                 "baseTime": baseTime,
                 "category": category,
                 "nx": nx,
                 "ny": ny,
                 'obsrValue': obsrValue})

df = pd.DataFrame(rows, columns=cols)

# Writing dataframe to csv
df.to_csv('output.csv')
"""

