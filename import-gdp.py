#!/usr/bin/env python

import os
import django
import json
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settlers.settings')
from django.core.exceptions import *
from mashup.models import *

taxagg = {'NT': { 'ind': 0, 'taxinc': 0, 'gross': 0, 'net': 0},
        'NSW': { 'ind': 0, 'taxinc': 0, 'gross': 0, 'net': 0},
        'QLD': { 'ind': 0, 'taxinc': 0, 'gross': 0, 'net': 0},
        'WA': { 'ind': 0, 'taxinc': 0, 'gross': 0, 'net': 0},
        'VIC': { 'ind': 0, 'taxinc': 0, 'gross': 0, 'net': 0},
        'ACT': { 'ind': 0, 'taxinc': 0, 'gross': 0, 'net': 0},
        'TAS': { 'ind': 0, 'taxinc': 0, 'gross': 0, 'net': 0},
        'SA': { 'ind': 0, 'taxinc': 0, 'gross': 0, 'net': 0},
        'AUST': { 'ind': 0, 'taxinc': 0, 'gross': 0, 'net': 0}
        }

with open('datasrc/ATO-Postcode.csv', 'r') as f:
  a = csv.reader(f, delimiter=',', quotechar='"')
  cnt = 0
  for row in a:
    if cnt != 0 and row[0] != 'OTHER':
      try:
        pcode = str(row[0])
        if len(pcode) <4:
          pcode = '0' + pcode
        p = Postcode.objects.get_or_create(code=pcode)
        p[0].save()
        taxagg[row[1]]['ind'] = taxagg[row[1]]['ind'] + int(row[2])
        taxagg[row[1]]['taxinc'] = taxagg[row[1]]['taxinc'] + int(row[3])
        taxagg[row[1]]['gross'] = taxagg[row[1]]['gross'] + int(row[4])
        taxagg[row[1]]['net'] = taxagg[row[1]]['net'] + int(row[5])
        
        taxagg['AUST']['ind'] = taxagg['AUST']['ind'] + int(row[2])
        taxagg['AUST']['taxinc'] = taxagg['AUST']['taxinc'] + int(row[3])
        taxagg['AUST']['gross'] = taxagg['AUST']['gross'] + int(row[4])
        taxagg['AUST']['net'] = taxagg['AUST']['net'] + int(row[5])
        
        t = TaxIncomePostcode.objects.create(postcode=p[0], individuals=int(row[2]), taxable_income=int(row[3]), gross_tax=int(row[4]), net_tax=int(row[5]))
      except Postcode.DoesNotExist, e:
        print "NOT FOUND: " + '|'.join(row)
    cnt = cnt + 1

for x in taxagg.keys():
  r = Region.objects.get(short=x)
  t = TaxIncomeRegion.objects.create(region=r, individuals=taxagg[x]['ind'], taxable_income=taxagg[x]['taxinc'], gross_tax=taxagg[x]['gross'], net_tax=taxagg[x]['net'])
  