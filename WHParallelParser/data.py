forbidden_tags = [
    {"name": "style"},
    {"name": "script"},
    {"name": "span", "class": "IPA"},
    {"name": "span", "class": "unicode haudio"},
    {"name": "span", "class": "mw-editsection"},
    {"name": "table", "class": "infobox vcard"},
    {"name": "div", "$and": [{"class": "infobox"}, {"class": "sisterproject"}]},
    {"name": "sup", "class": "reference"},
    {"name": "div", "role": "navigation"},
    {"name": "table"},
    {"name": "span", "$and": [{"class": "error"}, {"class": "mw-ext-cite-error"}]},
    {"name": "sup", "class": "reference"},
    {"name": "div", "$and": [{"class": "boilerplate"}, {"class": "metadata"}, {"class": "plainlinks"}]}
]

new_line_tags = [
    "p",
    "br",
    "hr",
    "li",
    "ol",
    "dl",
    "dt",
    "dd",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
]
