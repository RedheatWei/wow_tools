#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/24 10:23
# @Author  : unknown
import json
import struct


def parse_string_block(block):
    strings = {}
    current_string = ""
    for index, i in enumerate(block):
        if i == 0:
            strings[index - len(current_string)] = current_string
            current_string = ""
        else:
            current_string += chr(i)
    return strings


class DBC(object):
    def __init__(self, dbc_file, schema_file):
        with open(dbc_file, "rb") as f:
            self.buffer = f.read()
        with open(schema_file, "r") as f:
            self.schema = json.load(f)

    def _dbc2struct(self):
        if self.buffer[:4].decode("utf-8") != "WDBC":
            raise TypeError
        if struct.unpack('<I', self.buffer[:4])[0] != 1128416343:
            raise TypeError
        record_count = struct.unpack('<I', self.buffer[4:8])[0]
        field_count = struct.unpack('<I', self.buffer[8:12])[0]
        record_size = struct.unpack('<I', self.buffer[12:16])[0]
        # string block
        string_block_size = struct.unpack('<I', self.buffer[16:20])[0]
        string_block_start_index = len(self.buffer) - string_block_size
        string_block = self.buffer[string_block_start_index:]
        string_list = parse_string_block(string_block)
        # record block
        record_block = self.buffer[20:string_block_start_index]
        record_list = [record_block[i * record_size:(i + 1) * record_size] for i in range(record_count)]
        return {
            "record_count": record_count,
            "field_count": field_count,
            "record_size": record_size,
            "string_list": string_list,
            "record_list": record_list
        }

    def _record2dict(self, record, string_list):
        point = 0
        row = {}
        for index, key in enumerate(self.schema):
            col_type = key.get("type", 'int')
            col_name = key.get("name", f'field_{index + 1}')
            if point+4 > len(record):
                break

            if col_type == 'int':
                value = struct.unpack('<i', record[point:point + 4])[0]
            elif col_type == 'uint':
                value = struct.unpack('<I', record[point:point + 4])[0]
                value = hex(value)
            elif col_type == 'float':
                value = struct.unpack('<f', record[point:point + 4])[0]
            elif col_type == 'byte':
                value = struct.unpack('b', record[point:point + 1])[0]
            elif col_type == 'string':
                string_index = struct.unpack('<i', record[point:point + 4])[0]
                value = string_list[string_index]
            else:
                value = struct.unpack('<i', record[point:point + 4])[0]
            if col_type not in ['byte', 'null', 'localization']:
                point += 4
            row[col_name] = str(value)
        return row

    def dbc2list(self):
        dbc_struct = self._dbc2struct()
        return [self._record2dict(r, dbc_struct["string_list"]) for r in dbc_struct["record_list"]]

    def dbc2json(self):
        dbc_struct = self._dbc2struct()
        return json.dumps([self._record2dict(r, dbc_struct["string_list"]) for r in dbc_struct["record_list"]])

    def dbc2csv(self, filename):
        dbc_list = self.dbc2list()
        header = ",".join(list(dbc_list[0].keys())) + "\n"
        content = "\n".join([",".join(i.values()) for i in dbc_list])
        with open(filename, "w") as f:
            f.write(header)
            f.write(content)



if __name__ == "__main__":
    dbc = DBC("./data/dbc/Spell.dbc", "./schemas/azerothcore/spell.json")
    l = dbc.dbc2list()
    dbc.dbc2csv("spell.csv")
