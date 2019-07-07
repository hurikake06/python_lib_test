import urllib.request, urllib.error
from bs4 import BeautifulSoup

class MyScraping:
    urls = []
    pages = []

    def __init__(self, urls):
        self.urls = urls
        self.set_pages()

    def set_pages(self):
        for url in self.urls:
            html = urllib.request.urlopen(url=url)
            self.pages.append(BeautifulSoup(html, "html.parser"))







