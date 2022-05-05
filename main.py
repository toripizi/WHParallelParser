from html.parser import HTMLParser
from html.entities import name2codepoint
from bs4 import BeautifulSoup, Comment
import codecs


forbidden_tags =[
    {
        "tag": "style",
        "attrs": []
    }, {
        "tag": "script",
        "attrs": []
    }, {
        "tag": "span",
        "attrs": [('class', 'IPA'), ('class', 'unicode haudio'), ('class', 'mw-editsection')]
    }, {
        "tag": "table",
        "attrs": [('class', 'infobox vcard')]
    }, {
        "tag": "sup",
        "attrs": [('class', 'reference')]
    }, {
        "tag": "div",
        "attrs": [('role', 'navigation')]
    },
]
single_tags = [
    "area",
    "base",
    "br",
    "col",
    "command",
    "embed",
    "hr",
    "img",
    "input",
    "keygen",
    "link",
    "meta",
    "param",
    "source",
    "track",
    "wbr"
]
STOS = []


def ShouldParseStartTag(tag,attrs):
    if not tag in single_tags:
        forbidden = False
        for i in forbidden_tags:
            if tag == i["tag"]:
                if not len(i["attrs"]) == 0:
                    inttuple = tuple(set(i["attrs"]) & set(attrs))
                    if not len(inttuple) == 0:
                        forbidden = True
                        break
                else:
                    forbidden = True
                    break
        STOS.append((tag, forbidden))


def ShouldParse():
    shouldparse = True
    for i in STOS:
        if i[1] == True:
            shouldparse = False
            break

    return shouldparse


def ShouldParseEndTag(tag):
    if not tag in single_tags:
        STOS.pop()


class MyHTMLParser(HTMLParser):
    @override
    def handle_starttag(self, tag, attrs):
        ShouldParseStartTag(tag, attrs)
        if ShouldParse():
            print("Start tag:", tag)
            if tag == "p":
                merytoryka.write("\n")
            for attr in attrs:
                print("     attr:", attr)

    def handle_endtag(self, tag):
        ShouldParseEndTag(tag)
        print("End tag  :", tag)

    def handle_data(self, data):
        if ShouldParse():
            if not data.isspace() and not len(data) == 0 and not data == "\n":
                print("Data     :", data)
                merytoryka.write(data)
                #print("Position :",self.getpos())

    def handle_comment(self, data):
        print("Comment  :", data)

    def handle_entityref(self, name):
        c = chr(name2codepoint[name])
        print("Named ent:", c)

    def handle_charref(self, name):
        if name.startswith('x'):
            c = chr(int(name[1:], 16))
        else:
            c = chr(int(name))
        print("Num ent  :", c)

    def handle_decl(self, data):
        print("Decl     :", data)

parser = MyHTMLParser()
file = codecs.open("index1.html", "r", encoding="utf-8")
merytoryka = open("text.txt","w", encoding="utf-8") #plik do zapisywania czystego textu
save = open("test.txt","w", encoding="utf-8") #plik do zapisywania htmla

soup = BeautifulSoup(file, 'html.parser')

soup_string = str(soup)
save.write(soup_string)
#print(soup_string)
parser.feed(soup_string)

print(STOS)

