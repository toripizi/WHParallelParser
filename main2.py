from bs4 import BeautifulSoup
import json

# from bs4.formatter import HTMLFormatter


# class UnsortedAttributes(HTMLFormatter):
#     def attributes(self, tag):
#         for k, v in tag.attrs.items():
#             yield k, v


class MyParser:
    def __init__(self):
        self.id = 0
        self.parsed_obj = None
        self.html = None
        self.reborn_html = None

    def parse(self, html):
        self.html = html
        self.parsed_obj = self.get_obj()

    def get_obj(self, html=None):
        html = html if html else BeautifulSoup(self.html, 'html.parser').body
        return {
            "tag": html.name,
            "attr": html.attrs,
            "content": self.get_content(html)
        }

    def get_content(self, html):
        content_list = []
        for content in html.contents:
            if not isinstance(content, str):
                content_list.append(self.get_obj(content))
            else:
                content_list.append(content)
        return content_list

    def save_json(self, file_name):
        with open(f'output_files/{file_name}.json', 'w') as out_file:
            json.dump(self.parsed_obj, out_file)

    def save_html(self, file_name):
        with open(f'output_files/{file_name}.html', 'w') as out_file:
            out_file.write(self.html)

    def get_plain_text(self, parsed_obj=None):
        plane_text = ""
        for content in parsed_obj["content"] if parsed_obj else self.parsed_obj["content"]:
            if not isinstance(content, str):
                plane_text += self.get_plain_text(content)
            else:
                plane_text += content
        return plane_text.replace("\\n", "\n")

    def parse_obj_to_html(self, parsed_obj=None):
        parsed_obj = parsed_obj if parsed_obj else self.parsed_obj
        soup = BeautifulSoup("", 'html.parser')
        soup.append(self.create_tag(parsed_obj, soup))
        self.reborn_html = soup
        return soup

    def create_tag(self, parsed_obj, soup):
        new_tag = soup.new_tag(parsed_obj["tag"])
        new_tag.attrs = parsed_obj["attr"]
        for content in parsed_obj["content"]:
            if not isinstance(content, str):
                new_tag.append(self.create_tag(content, soup))
            else:
                new_tag.contents.append(content)
        return new_tag


# import unittest


# class TestStringMethods(unittest.TestCase):
#     # test function to test equality of two value
#     def test_negative(self):
#         with open("index1.html", "r", encoding="utf-8") as html_to_parse:
#             soup_html = BeautifulSoup(html_to_parse, 'html.parser')
#             parser = MyParser()
#             parser.parsed_obj = parser.get_obj(soup_html)
#             # parser.save("json_data")
#
#             text = parser.get_plain_text()
#             text = text.replace("\\n", "\n")
#
#             print(soup_html.contents)
#             expected_text = soup_html.get_text()
#
#             self.assertEqual(text, expected_text)
#
# TestStringMethods().test_negative()


with open("input_files/index.html", "r", encoding="utf-8") as html_to_parse:
    # soup_html = BeautifulSoup(html_to_parse, 'html.parser')
    parser = MyParser()
    parser.parse(html_to_parse)
    parser.save_json("json_data")
    # print(parser.parsed_obj)

    # text = parser.get_plain_text()
    # print(text)

    with open(f'output_files/asd.html', 'w') as out_file:
        out_file.write(str(parser.parse_obj_to_html()))

    # print(parser.parse_obj_to_html())
    # parser.save_html("reborn_html")

# Przydatne info
# parsed_html.div.contents
# [' CentralNotice ']
# parsed_html.div.contents[0].__class__
# <class 'bs4.element.Comment'>
