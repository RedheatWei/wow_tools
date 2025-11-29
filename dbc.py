#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/24 10:23
# @Author  : unknown
import json
import csv
import struct


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
        for string in sorted(string_set):
            string_index_dict[string] = len(bytes_string)
            bytes_string += string.encode('utf-8') + b'\x00'
        return {
            "string_index_dict": string_index_dict,
            "bytes_string": bytes_string
        }

    def _build_record_block(self, string_index_dict):
        bytes_record_size = 20 + (len(self.csv_content) * len(self.csv_content[0].keys()) * 4)
        bytes_record = bytearray(bytes_record_size - 20)

        def pack_uint(value):
            return struct.pack('<I', int(value))

        def pack_float(value):
            return struct.pack('<f', float(value))

        def pack_string(value):
            return struct.pack('<i', int(string_index_dict[value]))

        # def pack_default(value):
        #     return struct.pack('<i', int(value))

        type_encoders = {
            'uint': pack_uint,
            'int': pack_uint,
            'float': pack_float,
            'string': pack_string,
            # 'default': pack_default
        }

        index = 0
        for row in self.csv_content:
            for k, v in row.items():
                bytes_record[index:index + 4] = type_encoders[self.schema[k]](v)
                index += 4

        return bytes_record

    def csv2dbc(self, filename):
        string_info = self._build_string_block()
        bytes_string = string_info["bytes_string"]
        string_index_dict = string_info["string_index_dict"]

        bytes_record = self._build_record_block(string_index_dict)
        bytes_dbc = bytearray(20 + len(bytes_record) + len(bytes_string))
        bytes_dbc[:4] = struct.pack('<I', int(1128416343))
        bytes_dbc[4:8] = struct.pack('<I', len(self.csv_content))
        bytes_dbc[8:12] = struct.pack('<I', len(self.schema.keys()))
        bytes_dbc[12:16] = struct.pack('<I', int(len(bytes_record) / len(self.csv_content)))
        bytes_dbc[16:20] = struct.pack('<I', len(bytes_string))
        bytes_dbc[20:20 + len(bytes_record)] = bytes_record
        bytes_dbc[20 + len(bytes_record):] = bytes_string
        with open(filename, "wb") as f:
            f.write(bytes_dbc)


class DBC(object):
    def __init__(self, dbc_file, schema_file):
        with open(dbc_file, "rb") as f:
            self.buffer = f.read()
        with open(schema_file, "r") as f:
            self.schema = json.load(f)

    @staticmethod
    def _parse_string_block(block):
        strings = {}
        current_string = bytearray()
        point = 0
        for i in block:
            if i == 0:
                strings[point-len(current_string)] = current_string.decode('utf-8')
                current_string = bytearray()
            else:
                current_string.append(i)
            point += 1
        return strings

    def _dbc2struct(self):
        if struct.unpack('<I', self.buffer[:4])[0] != 1128416343:
            raise TypeError
        record_count = struct.unpack('<I', self.buffer[4:8])[0]
        field_count = struct.unpack('<I', self.buffer[8:12])[0]
        record_size = struct.unpack('<I', self.buffer[12:16])[0]
        # string block
        string_block_size = struct.unpack('<I', self.buffer[16:20])[0]
        string_block_start_index = len(self.buffer) - string_block_size
        string_block = self.buffer[string_block_start_index:]
        string_list = self._parse_string_block(string_block)
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
        row = {}

        def upack_uint(data):
            return struct.unpack('<I', data)[0]

        def upack_float(data):
            return struct.unpack('<f', data)[0]

        def unpack_string(data):
            return string_list[struct.unpack('<i', data)[0]]

        type_handlers = {
            'uint': upack_uint,
            'int': upack_uint,
            'float': upack_float,
            'string': unpack_string,
            # 'default': lambda data: struct.unpack('<i', data)[0]
        }
        point = 0
        for index, key in enumerate(self.schema):
            col_type = key.get("type")
            col_name = key.get("name", f'field_{index + 1}')
            value = type_handlers[col_type](record[point:point + 4])
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
        with open(filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=list(dbc_list[0].keys()), delimiter=',')
            writer.writeheader()
            writer.writerows(dbc_list)


def dbc2csv():
    # dbc = DBC("./data/dbc/Spell.dbc", "./schemas/azerothcore/spell.json")
    dbc = DBC("./ftp/Spell.dbc", "./schemas/azerothcore/spell.json")
    # l = dbc.dbc2list()
    dbc.dbc2csv("./ftp/spell.csv")


def csv2dbc():
    csv = CSV("./ftp/spell.csv", "./schemas/azerothcore/spell.json")
    csv.csv2dbc("./ftp/Spell.dbc")


if __name__ == "__main__":
    # dbc2csv()
    csv2dbc()
