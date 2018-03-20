import csv
import time
from collections import defaultdict
from blocks.models import *

'''
name = []
date_c = []
date_r = []
class_type = []
prep_by = []
location = []
description = []
log = []
sample_type = []
'''

def fun3(x):
    fun3_dict ={
        'AsqJ': 5,
        'MitoNEET': 9,
        'FtmOx1': 11,
        'Stc2': 19,
        'BDPP':18,
        'Fe-Azurin': 21,
        'CmlI': 7,
        'TPA': 14,
        'TQA': 16,
        'TMC': 13,
        'NifBCo': 19,
        'ME2EBC':15,
        'LAM': 10,
        'LmbB2': 8,
        'HydA1': 20,
    }
    fun3_dict = defaultdict(lambda: 22, fun3_dict)
    return fun3_dict[x]

def fun4(x):
    fun4_dict={
        'AK': 2,
        'JL': 3,
        'KD': 4,
        'EC': 5,
        'AL': 6,
        'ES': 7,
        'HS': 8,
        'RF': 9,
        'AZ':10,
        'CA':11,
        'JK':12,
        'JP':13,
        'MP':14,
        'SK':15,
        'CE':16,
        'DM':17,
        'JL':18,
        'ST':19,
    }
    fun4_dict=defaultdict(lambda: 20, fun4_dict)
    return fun4_dict[x]

def fun5(x):
    fun5_dict={
        'G5': 2,
        'G6': 3,
        'D3': 6,
        'GONE': 7,
        'Transferred': 8,
    }
    fun5_dict=defaultdict(lambda: 13, fun5_dict)
    return fun5_dict[x]

def fun8(x):
    fun8_dict={
        '1': 2,
        '2': 3,
        '3': 4,
        '4': 5,
    }
    fun8_dict=defaultdict(lambda: 5, fun8_dict)
    return fun8_dict[x]

i=0


with open('sam_data.txt',newline='') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter='\t')
    for row in csv_reader:
        #name.append(row[0])
        sample_name=row[0]
        dt_c = time.strptime(row[1],'%m/%d/%Y')
        dt_c_convert = str(dt_c.tm_year)+'-'+str(dt_c.tm_mon)+'-'+str(dt_c.tm_mday)
        #date_c.append(dt_c_convert)
        if row[2]!='':
            dt_r = time.strptime(row[2],'%m/%d/%Y')
            dt_r_convert = str(dt_r.tm_year)+'-'+str(dt_r.tm_mon)+'-'+str(dt_r.tm_mday)
        else:
            dt_r_convert=' '
        # sample system
        sample_system = fun3(row[3])
        # provider
        provider = fun4(row[0][2:4])
        # location of the sample
        location_slot = fun5(row[5])
        #description and log part
        description = row[6]
        log = row[7]
        #sample_type part: EPR, MB OR OTHER
        sampleType = fun8(row[8])
        #Create a new sample object
        p1 = Sample(name=sample_name, 
                    Sample_type_id=sampleType, 
                    date_created=dt_c_convert,
                    date_removed_optional=dt_r_convert,
                    Class_id=sample_system,
                    provider_name_id=provider,
                   location_id=location_slot,
                   sample_description_optional=description,
                   change_log_optional=log,)
        p1.save()

'''
print(name,
      date_c,
      date_r,
      class_type,
      prep_by,
      location,
      description,
      log,
      sample_type,
      )
''' and None



