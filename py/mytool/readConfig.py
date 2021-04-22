#!/usr/bin/env python
# -*- coding: utf-8 -*-

def readconfig(path):
    config_file = open(path)
    dict_temp = {}
    try:
        for line in config_file:
            if  line == "\n":
                continue
            line = line.split("=")
            k = line[0]
            v = line[1].split("\n")[0]
            dict_temp[k] = v
    finally:
        config_file.close()
    return dict_temp