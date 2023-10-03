import scrapy
import re
import os
import urllib.parse
from bs4 import BeautifulSoup


class PageSpider(scrapy.Spider):
    name = "pages"
    start_urls = ["https://es.wikipedia.org/wiki/Nube_privada_virtual"]
    save_dir = "/home/kate/Desktop/UNSA-2023B/Cloud/crawler/crawler/spiders/files"  # Reemplaza con tu ruta

    def parse(self, response):

        soup = BeautifulSoup(response.text, 'html.parser')
        current_page_url = response.url
        links = soup.find_all('a')

        file_name = self.obtener_nombre_archivo(current_page_url)
        file_path = os.path.join(self.save_dir, file_name)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(response.text)

        for link in links:
            href = link.get('href')
            if href:
                url_valida = self.es_url_valida(href)
                if url_valida:
                    yield {
                        "from_": current_page_url,
                        "to_": url_valida,
                    }
                    yield scrapy.Request(url_valida, callback=self.parse)

    def es_url_valida(self, url):
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

    def obtener_nombre_archivo(self, url):
        clean_title = re.sub(r'[\/:*?"<>|]', '_', urllib.parse.unquote(url))
        clean_title = clean_title.split('wiki_')[-1]
        return f"{clean_title}.html"
