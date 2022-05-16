from src.MWParser import MWParser
import json

parser = MWParser("./cached")
output = parser.parse_wikicode("""== Header ==\nContent""")
print(output.text)
print(json.dumps(output.data))

with open("./example.html", "r") as file:
    output = parser.parse_html(file)
    print(output.text)
    print(output.data)
