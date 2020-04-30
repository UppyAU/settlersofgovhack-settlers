#!/usr/bin/env python

import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settlers.settings')

from mashup.models import *

with open('datasrc/aus-postcodes.json', 'r') as f:
  a = json.loads(f.read())

for p in a:
  np = Postcode.objects.get_or_create(code=p["Postcode"])
  np[0].save()
  ns = Suburb.objects.get_or_create(postcode=np[0], name=p["Suburb"])
  ns[0].save()

