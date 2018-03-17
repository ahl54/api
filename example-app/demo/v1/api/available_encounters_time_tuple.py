# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas

import data_handler

class AvailableEncountersTimeTuple(ApiHandler):

    def get(self, time_tuples):
        '''
        Gets a list of patientIDs available from encounters
        Available is defined as overlapping time between start_time, stop_time and admitDate, dischargeDate
        Args:
            time_tuples: list of tuples of format (start_time, stop_time) 
        Returns:
            res: list of patientIDs available from encounters
            code: http status code, 200 OK, 404 not found
            header: dict
        '''
        res = []
        code = 200
        header = {}

        encounters = data_handler.load_file('encounters.csv')

        # T(O^2) optimize this
        for time_tuple in time_tuples:
            start_time = time_tuple[0]
            end_time = time_tuple[1]
            for encounter in encounters:
                # TODO: overlap = tupleTimes in range of tupleDates
                if (encounter['admitDate'] > end_time) or (encounter['dischargeDate'] < start_time):
                    res.append(encounter[patientID])

        # TODO: implement the nested forloop above to bisect with time overlap
        # try:
        #     res = list(set(a).intersection(b))
        # except Exception as e:
        #     print(str(e))
            
        if not res:
            code = 404
        return res, code, header
