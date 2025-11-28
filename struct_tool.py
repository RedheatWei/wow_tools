#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/28 17:55
# @Author  : unknown
import json
import sys


def spell():
    with open("./schemas/azerothcore/spell.json", "r") as f:
        json_data = json.load(f)
        for i in json_data:
            if i["type"] == "int":
                s = f'''('{i["name"]}', c_int32),'''
                print(s)
            elif i["type"] == "float":
                s = f'''('{i["name"]}', c_float),'''
                print(s)
            elif i["type"] == "uint":
                s = f'''('{i["name"]}', c_uint32),'''
                print(s)
            elif i["type"] == "string":
                s = f'''('{i["name"]}', c_int32),'''
                print(s)
            else:
                print(i["type"])
                sys.exit("unknown type")


if __name__ == '__main__':
    spell()
