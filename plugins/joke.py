#!/bin/python

import json

hanzojokes = {
        "0": {
            "joke": {
                "part1": "There are no good hanzojokes...",
                "part2": "... just like there are no good hanzo mains"
                },
        },
        "1": {
            "joke": {
                "part1": ""
                }
            }
        }

with open("libs/jokes", "a") as f:
    json.dump(f)
