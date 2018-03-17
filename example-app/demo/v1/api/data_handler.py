# -*- coding: utf-8 -*-

import os
import csv
import json

def load_file(fname):

    data = None
    data_path = os.path.join(os.getcwd(), fname)
    print(data_path)

    try:
        if fname.endswith('.txt'):
            data = json.dumps(data_path)

        if fname.endswith('patients.csv'):
            with open(data_path, 'r') as f:
                #reader = csv.DictReader(f)
                data = json.dumps(f)
    except IOError:
        print('Could not open file at:', data_path)
        return

    if not data:
        print('No data was loaded from file:', data_path)
        return

    print(data)
    return data
