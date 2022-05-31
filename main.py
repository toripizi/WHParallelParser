from bs4 import BeautifulSoup
from src.api import MWApi
from src.MWParser import MWParser
import json

URL = "https://en.wikipedia.org/w/api.php"
api = MWApi(URL, "cached")
soup = BeautifulSoup(
    api.parse(
        "<ref>{{cytuj stronę |url = https://www.cia.gov/library/publications/resources/the-world-factbook/rankorder/2147rank.html#pl |tytuł = Country comparison: Area |praca = The World Factbook |opublikowany = [[Centralna Agencja Wywiadowcza|Central Intelligence Agency]] |język = en |data dostępu = 2017-11-29}}</ref>"
    ),
    "html.parser",
)
root = soup.find("div", {"class": "mw-parser-output"})


print(root)

# print(json.dumps(output.data))
#
# with open("./example.html", "r") as file:
#     output = parser.parse_html(file)
#     print(output.text)
#     print(output.data)
