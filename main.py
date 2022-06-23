from MWParser.MWParser import MWParser
from MWParser.Iterator import Iterator
from MWParser.Rules import RuleList

# path_to_simplewiki = (
#     "./simplewiki-NS0-20220420-ENTERPRISE-HTML.json/simplewiki_0.ndjson"
# )
# for html in Iterator(path_to_simplewiki):
#     print(html.text)

parser = MWParser(cache_folder="./cache")
path_to_html = "./example.html"
with open(path_to_html, "r") as file:
    output = parser.parse_html(file)
    print(output.text)
    print(output.data)
