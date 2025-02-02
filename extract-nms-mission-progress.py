#!/usr/bin/env python3
import io
import os
import sys
import json

if len(sys.argv) > 1:
  sfname=sys.argv[1]

if os.path.exists(sfname):
  with io.open(sys.argv[1],'r',encoding="utf-8") as myfile: mystring = myfile.read()
  #data = json.loads(mystring)
  data = json.loads(mystring.replace('\\x', '\\u00'), strict=False) 

missions = data['BaseContext']['PlayerStateData']['MissionProgress']

for idx, i in enumerate(missions):
  m = i['Mission']
  progress = i['Progress']
  # example to show only one mission
  # if m.startswith('^WATERSTORY'):
  print(f'{m}: {progress}')

