#!python3

import csv
import urllib.request

downloaded_data = urllib.request.urlopen('https://www.cnbc.com/quotes/?symbol=@BTC.1')
csv_data = csv.reader(downloaded_data)

for row in csv_data:
    print(row)
