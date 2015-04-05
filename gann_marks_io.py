# -*- coding: utf-8 -*-

__author__ = 'Ilya Shoshin'
__copyright__ = 'Copyright 2015, Ilya Shoshin'


import json


def load_marks(file_name):
    marks = []
    if file_name != '':
        with open(file_name) as data_file:
            marks = json.load(data_file)
            for dict in marks:
                data_path = dict["data_path"]
                with open(data_path) as sub_data_file:
                    data = list(sub_data_file)
                    dict.update({"data": data})
    return marks
