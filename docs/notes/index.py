#!/usr/bin/env python3

import dateutil.parser
import datetime
import json
import os

last_category = None

with open('index.md', 'w') as index:
    index.write("# COSC 101A, Introduction to Computing I, Fall 2024\n\n")
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
            solution_filename = filename.replace('.ipynb', '.solution.html')
            worksheet_filename = filename.replace('.ipynb', '.worksheet.html')
        else:
            continue
            
        if (dateutil.parser.parse(date).date() > dateutil.parser.parse("2024-08-01").date()):
            print(f"{title} ({date})")
            if (category != last_category):
                index.write(f"\n## {category}\n")
            index.write(f"* {title}")
            index.write(f" [[Worksheet]]({worksheet_filename})")
            if (datetime.date.today() > dateutil.parser.parse(date).date()
                or (datetime.date.today() == dateutil.parser.parse(date).date() and datetime.datetime.now().hour >= 11)):
                index.write(f"[[Solution]]({solution_filename})")
            index.write("\n")
            last_category = category

