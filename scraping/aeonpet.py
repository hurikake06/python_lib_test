import urllib.request, urllib.error
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import re

from MyScraping import MyScraping


url_base = "https://www.aeonpet-memorial.com/"
url_sitemap = url_base + "sitemap.xml"
url = "https://www.aeonpet-memorial.com/reien/satu-petyasuragi-sapporo/"

url_array = []

with urllib.request.urlopen(url=url_sitemap) as xml_string:
    sitemap = ET.fromstring(xml_string.read())

for child in sitemap.findall('./atom:url', {'atom': 'http://www.sitemaps.org/schemas/sitemap/0.9'}):
    url = child[0].text
    if re.match('https://www.aeonpet-memorial.com/reien/.+', url):
        url_array.append(url)

myScraping = MyScraping(url_array)

for index, page in enumerate(myScraping.pages):
    print('{0}:{1}'.format(index, page.find("div", class_="dethead").find("h1").string))







