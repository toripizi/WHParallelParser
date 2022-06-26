import requests
import hashlib
from os.path import exists


class MWApi:
    def __init__(self, URL, cache_folder):
        self.URL = URL
        self.cache_folder = cache_folder

    def parse(self, text):
        cached = self.get_cached(text)
        if cached:
            return cached
        response = requests.get(
            url=self.URL,
            params={
                "action": "parse",
                "contentmodel": "wikitext",
                "text": text,
                "format": "json",
            },
        )
        parsed = response.json()["parse"]["text"]["*"]
        self.save_to_cache(text, parsed)
        return parsed

    def get_cached(self, text):
        name = hashlib.sha256(text.encode("utf-8")).hexdigest()
        path = f"{self.cache_folder}/{name}"
        if exists(path):
            with open(path, "r", encoding="utf-8") as file:
                parsed = file.read()
                return parsed

    def save_to_cache(self, text, parsed):
        name = hashlib.sha256(text.encode("utf-8")).hexdigest()
        path = f"{self.cache_folder}/{name}"
        with open(path, "w", encoding="utf-8") as file:
            file.write(parsed)
