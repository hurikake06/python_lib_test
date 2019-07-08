import urllib.request, urllib.error
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import re

url_base = "https://www.aeonpet-memorial.com/"
url_sitemap = url_base + "sitemap.xml"
url = "https://www.aeonpet-memorial.com/reien/satu-petyasuragi-sapporo/"

urls = []

with urllib.request.urlopen(url=url_sitemap) as xml_string:
    sitemap = ET.fromstring(xml_string.read())

urls = [child[0].text for child in sitemap.findall('./atom:url', {'atom': 'http://www.sitemaps.org/schemas/sitemap/0.9'}) if re.match('https://www.aeonpet-memorial.com/reien/.+', child[0].text)]

pages = [BeautifulSoup(urllib.request.urlopen(url=url), "html.parser") for url in urls]

for index, page in enumerate(pages):
    print('{0}:{1}'.format(index, page.find("div", class_="dethead").find("h1").string))
