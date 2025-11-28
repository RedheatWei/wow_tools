#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/24 10:23
# @Author  : unknown
import json
import csv
import struct


def parse_string_block(block):
    strings = {}
    current_string = []
    for index, i in enumerate(block):
        if i == 0:
            strings[index - len(current_string)] = bytes(current_string).decode('utf-8')
            current_string = []
        else:
            current_string.append(i)
    return strings


class CSV(object):
    def __init__(self, csv_file, schema_file):
        with open(schema_file, "r") as f:
            schema_list = json.load(f)
            self.schema = {i["name"]: i["type"] for i in schema_list}

        with open(csv_file, "r") as csvfile:
            reader = csv.DictReader(
                csvfile,
                # fieldnames=[i["name"] for i in self.schema],
                delimiter=',',
                quotechar='"',
                quoting=csv.QUOTE_ALL
            )
            self.csv_content = [i for i in reader]

    def _build_string_block(self):
        # 找出所有字符串
        string_list = []
        for row in self.csv_content:
            for k, v in row.items():
                if self.schema[k] == 'string':
                    string_list.append(v)
        string_set = set(string_list)
        # 生成 string block
        bytes_string = bytes()
        string_index_dict = {}
        for string in string_set:
            bytes_string += string.encode('utf-8') + b'\x00'
            string_index_dict[string] = len(bytes_string)
        return {
            "string_index_dict": string_index_dict,
            "bytes_string": bytes_string
        }

    def _build_record_block(self, string_index_dict):
        bytes_record = bytes()
        bytes_record_size = 20
        for row in self.csv_content:
            for k, v in row.items():
                if self.schema[k] != 'byte':
                    bytes_record_size += 4
                else:
                    bytes_record_size += 1

        for row in self.csv_content:
            for k, v in row.items():
                if self.schema[k] == 'int':
                    bytes_record += struct.pack('<i', int(v))
                elif self.schema[k] == 'uint':
                    bytes_record += struct.pack('<I', int(v, 16))
                elif self.schema[k] == 'float':
                    bytes_record += struct.pack('<f', float(v))
                elif self.schema[k] == 'byte':
                    bytes_record += struct.pack('b', int(v))
                elif self.schema[k] == 'string':
                    bytes_record += struct.pack('<i', int(string_index_dict[v] + bytes_record_size))
                else:
                    bytes_record += struct.pack('<i', int(v))
        return bytes_record

    def csv2dbc(self, filename):
        string_info = self._build_string_block()
        bytes_string = string_info["bytes_string"]
        string_index_dict = string_info["string_index_dict"]

        bytes_record = self._build_record_block(string_index_dict)

        bytes_dbc = bytes()
        bytes_dbc += struct.pack('<I', "WDBC".encode('utf-8'))
        bytes_dbc += struct.pack('<I', len(self.csv_content))
        bytes_dbc += struct.pack('<I', len(self.schema.keys()))
        bytes_dbc += struct.pack('<I', len(bytes_record))
        bytes_dbc += struct.pack('<I', len(bytes_string))
        with open(filename, "wb") as f:
            f.write(bytes_dbc)


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
            if point + 4 > len(record):
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
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=list(dbc_list[0].keys()), delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_ALL)
            writer.writeheader()
            writer.writerows(dbc_list)


if __name__ == "__main__":
    # dbc = DBC("./data/dbc/Spell.dbc", "./schemas/azerothcore/spell.json")
    # l = dbc.dbc2list()
    # dbc.dbc2csv("spell.csv")
    csv = CSV("./spell.csv", "./schemas/azerothcore/spell.json")
    csv.csv2dbc("./spell.dbc")
