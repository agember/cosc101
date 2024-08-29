#!/usr/bin/env python3

import json
import os

last_category = None

with open('index.md', 'w') as index:
    index.write("# COSC 101A, Fall 2021\n\n")
    for filename in sorted(os.listdir(".")):
        if filename.endswith('.ipynb'):
            with open(filename, 'r') as notebook:
                contents = json.load(notebook)
            title = contents["cells"][0]["source"][0].strip("# \n")
            title_parts = title.split(": ")
            if len(title_parts) == 2:
                category = title_parts[0]
                title = title_parts[1]
            else:
                category = None
            date = contents["cells"][0]["source"][1].split(",")[2].strip(" _")
            print("{} ({})".format(title, date))
#            if (category != last_category):
#                index.write("\n## {}\n".format(category))
            index.write("* {} ({}) [[Notes]]({}) [[Worksheet]]({}) [[Slides]]({})\n".format(
                    title, date, filename.replace('.ipynb', '.notes.html'),
                    filename.replace('.ipynb', '.worksheet.html'),
                    filename.replace('.ipynb', '.slides.html')))
            last_category = category

