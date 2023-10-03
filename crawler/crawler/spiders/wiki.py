import scrapy
import re
from bs4 import BeautifulSoup
from crawler.items import CrawlerItem
from scrapy.http import HtmlResponse, Response
from urllib.parse import urlparse


def es_url_valida(url):
    patrones_invalidos = [
        r'^/wiki/Portal',
        r'^/wiki/Wikipedia',
        r'^/wiki/Ayuda',
        r'^/wiki/Especial',
        r'^/wiki/Archivo',
        r'^/wiki/Categor',
    ]

    for patron in patrones_invalidos:
        if re.match(patron, url):
            return None

    patron = r'^/wiki/[^\s]+$'
    if re.match(patron, url):
        return f"https://es.wikipedia.org{url}"


class WikiSpider(scrapy.Spider):
    name = "wiki"
    start_urls = ["https://es.wikipedia.org/wiki/Nube_privada_virtual"]

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        current_page_url = response.url
        links = soup.find_all('a')

        for link in links:
            href = link.get('href')
            if href:
                url_valida = es_url_valida(href)
                if url_valida:
                    yield {
                        "from_": current_page_url,
                        "to_": url_valida,
                    }
                    yield scrapy.Request(url_valida, callback=self.parse)
