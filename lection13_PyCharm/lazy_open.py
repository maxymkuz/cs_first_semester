import requests
import os
from settings import MAPPER

def lazy_open(path):
    if not os.path.exists(path):
        url = MAPPER[path]
        r = requests.get(url)
