# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas

import data_handler

class PhysioObjectsMeasureNames(ApiHandler):

    def get(self, measure_names):
        '''
        Gets a list of start, stop time tuples from physio_data objects
        filtered by measure_names
        Args:
            measure_names: list of string measure_names 
        Returns:
            res: list of tuples of format (start_time, stop_time)
            code: http status code, 200 OK, 404 not found
            header: dict
        '''
        res = []
        code = 200
        header = {}

        physio_data = data_handler.load_file('physio_data.txt')

        try:
            res_idx = list(set(measure_names).intersection(physio_data['measure_names']))
            # get all the indices of matching measure names
            # then index on physio and key start stop, format as list
            res = (physio_data[res_idx]['start_time'], physio_data[res_idx]['stop_time'])
        except Exception as e:
            print(str(e))
        return res, code, header