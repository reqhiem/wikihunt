import scrapy
import re
import os
from bs4 import BeautifulSoup
import hashlib
from .utils.postgres_connection import insert_hash_url, get_postgresql_connection
from .utils.content_parser import clean_content


class PageSpider(scrapy.Spider):
    name = "pages"
    start_urls = ["https://es.wikipedia.org/wiki/Nube_privada_virtual"]
    current_dir = os.getcwd()
    save_dir = os.path.join(current_dir, "files")  # Reemplaza con tu ruta
    connection = get_postgresql_connection()

    def parse(self, response):
        soup = BeautifulSoup(response.text, "html.parser")
        current_page_url = response.url
        links = soup.find_all("a")
        soup_title = soup.find("title")
        doc_title = soup_title.get_text() if soup_title else "Sin título"

        hash = hashlib.sha256(current_page_url.encode("UTF-8")).hexdigest()
        file_path = os.path.join(self.save_dir, hash)
        insert_hash_url(hash, current_page_url, doc_title, self.connection)
        content_file = clean_content(soup, hash)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content_file)

        for link in links:
            href = link.get("href")
            if href:
                url_valida = self.es_url_valida(href)
                if url_valida and url_valida != current_page_url:
                    yield {
                        "from_": current_page_url,
                        "to_": url_valida,
                        "hash_from_": hash,
                        "hash_to_": hashlib.sha256(
                            url_valida.encode("UTF-8")
                        ).hexdigest(),
                    }
                    yield scrapy.Request(url_valida, callback=self.parse)

    def es_url_valida(self, url):
        patrones_invalidos = [
            r"^/wiki/Portal",
            r"^/wiki/Wikipedia",
            r"^/wiki/Ayuda",
            r"^/wiki/Especial",
            r"^/wiki/Archivo",
            r"^/wiki/Categor",
        ]

        for patron in patrones_invalidos:
            if re.match(patron, url):
                return None

        patron = r"^/wiki/[^\s]+$"
        if re.match(patron, url):
            return f"https://es.wikipedia.org{url}"
