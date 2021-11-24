#!/usr/bin/env python3

import json
with open('./keywords.md', 'r') as f:
    data = [line.split('|') for line in f.readlines()]

def get_keywords(data):
    return {line[1]: line[2] for line in data}

keywords = get_keywords(data)

with open('./keywords.json', 'w') as f:
    json.dump(keywords, f, indent=4, ensure_ascii=False)
