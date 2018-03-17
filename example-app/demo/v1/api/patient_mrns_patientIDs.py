# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas

import data_handler

class PatientMrnsPatientids(ApiHandler):

    def get(self, patientIDs):
        '''
        Gets a list of Medical Record Numbers (MRNs) from patientIDs
        Args:
            patientIDs: list of int patientIDs
        Returns:
            res: list of int MRNs
            code: http status code, 200 OK, 404 not found
            header: dict
        '''
        res = []
        code = 200
        header = {}

        try:
            patients = data_handler.load_file('patients.csv')        
            if patients:
                res = list(set(patientIDs).intersection(patients['patientID']))
        except Exception as e:
            print(str(e))

        if not res:
            code = 404
        return res, code, header