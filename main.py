from src.MWParser import MWParser


parser = MWParser("https://en.wikipedia.org/w/api.php", "./cached")
output = parser.parse_wikicode("'''asd'''")
print(output.text)
print(output.data)

with open("./example.html", "r") as file:
    output = parser.parse_html(file)
    print(output.text)
    print(output.data)
