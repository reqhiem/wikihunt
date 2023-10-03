# Crawler Wikipedia
1. **Ubícate en el directorio de este archivo**

2. **Crea y activa un entorno virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   
4. **Instala las dependencias desde el archivo requirements.txt:**
   ```bash
   pip install -r requirements.txt
  
3. **Ejecuta la spider pages:**
   ```bash
   cd crawler
   scrapy crawl pages -o test_urls.csv
