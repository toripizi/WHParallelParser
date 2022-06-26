from MWParser import MWParser
from MWParser import Iterator
from MWParser import MWApi
from MWParser import RuleList

# path_to_simplewiki = "./simplewiki-NS0-20220420-ENTERPRISE-HTML.json/simplewiki_0.ndjson"
# for html in Iterator(path_to_simplewiki):
#     print(html.text)

parser = MWParser(cache_folder="./cached")
path_to_html = "./example.html"
with open(path_to_html, "r") as file:
    output = parser.parse_html("<i>asd</i>")
    print(output.text)
    print(output.data)
