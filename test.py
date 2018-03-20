from blocks.models import *
from functions.models import *
from django.db import models

#p1 = Sample(name = 'AGJL00', Sample_type_id=2, date_created='2015-12-03',date_removed_optional='2015-01-01', Class_id=2, location_id=2, provider_name_id=2)
#p1.save()

p1 = Author.objects.all()
for row in p1:
    print(row, row.id)

p2 = dewar_tray.objects.all()
for row in p2:
    print(row, row.id)

p3 = Sample_Class.objects.all()
for row in p3:
    print(row, row.id)

p4 = sample_type.objects.all()
for row in p4:
    print(row, row.id)

p5 = Sample.objects.get(name='undefined')
print(p5.id)

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
