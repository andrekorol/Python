#! python3

import urllib.request

downloaded_data = urllib.request.urlopen('https://www.cnbc.com/quotes/?symbol=@BTC.1')

for line in downloaded_data.readlines():
    print(line)
