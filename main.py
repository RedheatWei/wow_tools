#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/24 10:23
# @Author  : unknown
def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()
