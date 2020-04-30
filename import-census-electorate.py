#!/usr/bin/env python

import os
import django
import json
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settlers.settings')
from django.core.exceptions import *
from mashup.models import *

lesszero = IncomeBand.objects.get(name="Zero or Less than Zero")
i199 = IncomeBand.objects.get(name="1 to 199")
i299 = IncomeBand.objects.get(name="200 to 299")
i399 = IncomeBand.objects.get(name="300 to 399")
i499 = IncomeBand.objects.get(name="400 to 599")
i699 = IncomeBand.objects.get(name="600 to 799")
i899 = IncomeBand.objects.get(name="800 to 999")
i1000 = IncomeBand.objects.get(name="1000 to 1249")
i1250 = IncomeBand.objects.get(name="1250 to 1499")
i1500 = IncomeBand.objects.get(name="1500 to 1999")
i2000 = IncomeBand.objects.get(name="Over 2000")
na = IncomeBand.objects.get(name="NA")

with open('datasrc/2011Census_P17B_AUST_CED_long_WORKING.csv', 'r') as f:
  a = csv.reader(f, delimiter=',', quotechar='"')
  cnt = 0
  for row in a:
    if cnt != 0:
      try:
        e = Electorate.objects.get(code=row[0])
        nr = CensusElectorateIncome.objects.create(electorate=e, band=lesszero, value=row[2])
        nr = CensusElectorateIncome.objects.create(electorate=e, band=i199, value=row[3])
        nr = CensusElectorateIncome.objects.create(electorate=e, band=i299, value=row[4])
        nr = CensusElectorateIncome.objects.create(electorate=e, band=i399, value=row[5])
        nr = CensusElectorateIncome.objects.create(electorate=e, band=i499, value=row[6])
        nr = CensusElectorateIncome.objects.create(electorate=e, band=i699, value=row[7])
        nr = CensusElectorateIncome.objects.create(electorate=e, band=i899, value=row[8])
        nr = CensusElectorateIncome.objects.create(electorate=e, band=i1000, value=row[9])
        nr = CensusElectorateIncome.objects.create(electorate=e, band=i1250, value=row[10])
        nr = CensusElectorateIncome.objects.create(electorate=e, band=i1500, value=row[11])
        nr = CensusElectorateIncome.objects.create(electorate=e, band=i2000, value=row[12])
        nr = CensusElectorateIncome.objects.create(electorate=e, band=na, value=row[13])
      except Electorate.DoesNotExist, e:
        print "NOT FOUND: " + '|'.join(row)
    cnt = cnt + 1
