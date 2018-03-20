import csv
import time
from blocks.models import *
from functions.models import *
from extra.models import *

name = []
spec_type = []
sample_id =[]
date = []
condition = []

with open('spec_tab.csv',newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',',quotechar='|')
     for row in spamreader:
         dt = time.strptime(row[3],'%m/%d/%Y')
         dt_convert = str(dt.tm_year)+'-'+str(dt.tm_mon)+'-'+str(dt.tm_mday)
         p1 = spectrum(spectrum_name=row[0],spectrum_type=row[1], Date_measured=dt_convert,Measure_condition=row[4:],sample_id=591)
         p1.save()

#        name.append(row[0])
#        spec_type.append(row[1])
#        sample_id.append(row[2])
#        date.append(row[3])
#        condition.append(row[4])
        
        

#print(name)
#print(spec_type)
#print(sample_id)
#print(date)
#print(condition)




