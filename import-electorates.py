#!/usr/bin/env python

import os
import django
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settlers.settings')

from mashup.models import *

with open('datasrc/electorates.csv', 'r') as f:
  a = csv.reader(f, delimiter=',', quotechar='"')
  c = 0
  for row in a:
    if c != 0:
      e = Electorate.objects.create(code=row[0], name=row[1])
    c = c+1

