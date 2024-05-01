print("hello")
import requests
from bs4 import BeautifulSoup
Url = "https://en.wikipedia.org/wiki/Yu-Gi-Oh%21"
r = requests.get(Url)
print (r.status_code)
print(r.text)