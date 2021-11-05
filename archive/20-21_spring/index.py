#!/usr/bin/env python3

import json
import os

with open('index.md', 'w') as index:
    for filename in sorted(os.listdir(".")):
        if filename.endswith('.ipynb'):
            with open(filename, 'r') as notebook:
                contents = json.load(notebook)
            title = contents["cells"][0]["source"][0].strip("# ")
            print(title)
            index.write("* %s [[Notes]](%s) [[Worksheet]](%s) [[Slides]](%s)\n" 
                    % (title, filename.replace('.ipynb', '.notes.html'),
                    filename.replace('.ipynb', '.worksheet.html'),
                    filename.replace('.ipynb', '.slides.html')))

