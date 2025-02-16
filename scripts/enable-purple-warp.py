#!/usr/bin/env python3
import io
import sys
import json

if len(sys.argv) < 2:
  print(f'Usage: {sys.argv[0]} EXPORTED-NMS-SAVE-JSON-FILE')
  sys.exit()

with io.open(sys.argv[1],'r',encoding="utf-8") as myfile: mystring = myfile.read()
data = json.loads(mystring)
#data = json.loads(mystring.replace('\\x', '\\u00'), strict=False) 

data['BaseContext']['PlayerStateData']['HasDiscoveredPurpleSystems'] = True

tech = data['BaseContext']['PlayerStateData']['KnownTech']
tech.append('^HDRIVEBOOST4')

with open("out.json", "w") as outfile:
    json.dump(data, outfile, indent=2)
