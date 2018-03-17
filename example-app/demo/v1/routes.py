# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.physio_objects_measure_names import PhysioObjectsMeasureNames
from .api.available_encounters_time_tuple import AvailableEncountersTimeTuple
from .api.patient_mrns_patientIDs import PatientMrnsPatientids


url_prefix = 'v1'

routes = [
    dict(resource=PhysioObjectsMeasureNames, urls=[r"/physio_objects/(?P<measure_names>[^/]+?)"], endpoint='physio_objects_measure_names'),
    dict(resource=AvailableEncountersTimeTuple, urls=[r"/available_encounters/(?P<time_tuple>[^/]+?)"], endpoint='available_encounters_time_tuple'),
    dict(resource=PatientMrnsPatientids, urls=[r"/patient_mrns/(?P<patientIDs>[^/]+?)"], endpoint='patient_mrns_patientIDs'),
]

def load_uris(config):
    try:
        config.update_uri(routes, url_prefix)
    except:
        pass