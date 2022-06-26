# WHParallelParser
**WHParallelParser** *(the WikiCode&Html Parallel Parser)* is a Python package that provides a parser for Wikipedia Html and WikiCode.

The WHParallelParser parser uses the parallel markup approach, the raw text data and the formatting information are kept separately. Each tag contains information about its position and length in the document. This format has many advantages over traditional embedded markup, and can be use in machine learning.

File input types for the parser:
- HyperText Markup Language (HTML) 
- WikiCode

# Installation
The WHParallelParser is avaliable through Pip Installs Packages.
You can install the latest release with command line
```
pip install WHParallelParser
```

# Usage
Parser initialization, we should specify **cache_folder**
```python
from WHParallelParser import WHParallelParser
from WHParallelParser import Iterator
from WHParallelParser import Rule

cache_folder = "./cached"


parser = WHParallelParser(cache_folder=cache_folder)
```
# Parsing HTML
After parser initialization, we can use function **parse_html**
```python
output = parser.parse_html("<div>test<h1>test</div>")
print(output.text)
print(output.data)
```
Example **output.text** output
```
['test', 'test']
```
Example **output.data** output
```
[
  {
    "tag": "h1",
    "attrs": {},
    "start": [
      1,
      0
    ],
    "end": [
      1,
      3
    ]
  },
  {
    "tag": "div",
    "attrs": {},
    "start": [
      0,
      0
    ],
    "end": [
      2,
      -1
    ]
  }
]
```
# Parsing WikiCode
After parser initialization, we can use function **parse_wikicode**
```python
output = parser.parse_wikicode("[[link]]")
print(output.text)
print(output.data)
```
Example **output.text** output
```
['link']
```
Example **output.data** output
```
[
  {
    "tag": "a",
    "attrs": {
      "href": "/wiki/Link",
      "class": [
        "mw-disambig"
      ],
      "title": "Link"
    },
    "start": [
      0,
      0
    ],
    "end": [
      0,
      3
    ]
  },
  {
    "tag": "p",
    "attrs": {},
    "start": [
      0,
      0
    ],
    "end": [
      0,
      3
    ]
  },
  {
    "tag": "div",
    "attrs": {
      "class": [
        "mw-parser-output"
      ]
    },
    "start": [
      0,
      0
    ],
    "end": [
      1,
      -1
    ]
  }
]
```

# Simplewiki json
We can iterate over simplewiki json file
```python
path_to_simplewiki = "example_simplewiki.json/simplewiki.ndjson"
for html in Iterator(path_to_simplewiki):
    print(html.text)
```
# Add Rule
We can add some rules
```python
parser.rules.add_rule(Rule({"name": "a", "class": "mw-disambig"}))

output = parser.parse_wikicode("[[link]] '''test'''")
print(output.text)
print(output.data)
```
Example **output.text** output
```
['test']
```
Example **output.data** output
```
[
  {
    "tag": "b",
    "attrs": {},
    "start": [
      0,
      1
    ],
    "end": [
      0,
      4
    ]
  },
  {
    "tag": "p",
    "attrs": {},
    "start": [
      0,
      0
    ],
    "end": [
      0,
      4
    ]
  },
  {
    "tag": "div",
    "attrs": {
      "class": [
        "mw-parser-output"
      ]
    },
    "start": [
      0,
      0
    ],
    "end": [
      1,
      -1
    ]
  }
]
```
# Remove Rule
We can remove some rules
```python
parser.rules.remove_rule(Rule({"name": "a", "class": "mw-disambig"}))

output = parser.parse_wikicode("[[link]] '''test'''")
print(output.text)
print(output.data)
```

Example **output.text** output
```
['link test']
```
Example **output.data** output
```
[
  {
    "tag": "a",
    "attrs": {
      "href": "/wiki/Link",
      "class": [
        "mw-disambig"
      ],
      "title": "Link"
    },
    "start": [
      0,
      0
    ],
    "end": [
      0,
      3
    ]
  },
  {
    "tag": "b",
    "attrs": {},
    "start": [
      0,
      5
    ],
    "end": [
      0,
      8
    ]
  },
  {
    "tag": "p",
    "attrs": {},
    "start": [
      0,
      0
    ],
    "end": [
      0,
      8
    ]
  },
  {
    "tag": "div",
    "attrs": {
      "class": [
        "mw-parser-output"
      ]
    },
    "start": [
      0,
      0
    ],
    "end": [
      1,
      -1
    ]
  }
]
```

# Supported tags
Each wiki link is defined by the tag with the following structure:
```
{
    'tag': 'link',
    'attrs': {
        'href': string,
        'class': [string],
        ...
    },
    'start': [int, int],
    'end': [int, int]
}
```
# Development
The project contains unit tests that checks if the parser works as expected. To execute all the tests run the following command in the project root dictionary:
```console
pytest ./tests
```
To execute a specific test suite:
```console
pytest ./tests/test_wikilink.py
```
# Authors
The Three Musketeers | MMK_team
- Maciek
- Miłosz
- Kajetan

We are students from Gdańsk University of Technology
