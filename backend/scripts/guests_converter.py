#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convert txt file of names to json
"""
import re
import json

structure = {
    "parties": [
    ]
}

with open("guests.txt", "r") as fh:
    non_json_data = fh.read()

pattern = r"\"(\w[\w\s-]+)\""
all_parties = re.sub(pattern,r"\1,", non_json_data)
all_parties = [party.lstrip("\n") for party in all_parties[:-1].split(",")]

for party in all_parties:
    dict_party = {
        "email": "INSERT EMAIL",
        "guests": [{"name": guest.strip()} for guest in party.split("\n")]
    }
    structure["parties"].append(dict_party)

json.dump(structure, open("guests.json", "w"), indent=4, ensure_ascii=False)
