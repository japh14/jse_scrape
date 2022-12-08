import requests
from typing import List

def create_content_pages(pages: List) -> List:
    return (requests.get(page).content for page in pages)
