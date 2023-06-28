import pandas as pd
import requests
from xml.etree import ElementTree

passcode = pd.read_csv('passcode.csv', index_col=0)
passcodey = passcode.iloc[0][0]

URL = "https://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst"

PARAMS = {'serviceKey': passcodey,
          'numOfRows': 10,
          'pageNo': 1,
          'base_date': 20230628,
          'base_time': '0600',
          'nx': 55,
          'ny': 127}

r = requests.get(url = URL, params = PARAMS)


tree = ElementTree.fromstring(r.content)
print(r.content)