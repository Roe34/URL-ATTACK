import requests  
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import os 

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet SPİDERURL")

def find_urls(url):
    visited_urls = set()
    urls = []

    def crawl(url):
        if url in visited_urls:
            return

        visited_urls.add(url)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                absolute_url = urljoin(url, href)
                parsed_url = urlparse(absolute_url)
                if parsed_url.scheme in ('http', 'https') and parsed_url.netloc == urlparse(url).netloc:
                    formatted_url = "URL:" + absolute_url
                    urls.append(formatted_url)
                    crawl(absolute_url)

    crawl(url)
    return urls
print("BU TOOL RoE TARAFINDAN YAPILMIŞTIR")
site_url = input("Lütfen URL'yi girin: ")
found_urls = find_urls(site_url)

print("Bulunan URL'ler:")
for url in found_urls:
    print(url)
print("VİXYUM VE DESTROYER SİZİ SEVİYORUM ~RoE")