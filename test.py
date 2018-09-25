
url = "https://www.smyk.com/catalog/product/view/id/293679/s/columbia-spodnie-narciarskie-dziewczece-starchaser-peak-ii-pant/"

import re
import urllib.request
with urllib.request.urlopen(url) as response:
    html = response.read()
    print( re.findall("finalPrice\"\:\"([\d\.]+)\"", html.decode())[0])
