#!/usr/bin/env python3
import io
import os
import sys
import json
import yaml
import logging
logging.basicConfig(level=logging.INFO) 

if len(sys.argv) > 1:
  sfname=sys.argv[1]
else:
  print(f'Usage: {sys.argv[0]} NMS-SAVE-JSON')
  sys.exit(1)

if os.path.exists(sfname):
  with io.open(sys.argv[1],'r',encoding="utf-8") as myfile: mystring = myfile.read()
  data = json.loads(mystring)
  #data = json.loads(mystring.replace('\\x', '\\u00'), strict=False) 

yname = "steps.yaml"
step_ref = {}
with open(yname, 'r') as stream:
    try:
      step_ref = yaml.safe_load(stream)
    except yaml.YAMLError as e:
      print(e)


def complete_step(data, mission_name, mission_index):
  mission_data = data['BaseContext']['PlayerStateData']['MissionProgress'][mission_index]
  if mission_data['Progress'] != step_ref[mission_name]:
    mission_data['Progress'] = step_ref[mission_name]
    logging.info(f'Set mission {m} to {step_ref[mission_name]}')


missions = data['BaseContext']['PlayerStateData']['MissionProgress']
for idx, i in enumerate(missions):
  m = i['Mission']
  progress = i['Progress']
  if m in step_ref:
    logging.debug(f'Found mission {m}')
    complete_step(data, m, idx)

# set by first Anomaly conversations
data['BaseContext']['PlayerStateData']['RevealBlackHoles'] = True
data['BaseContext']['PlayerStateData']['FirstAtlasStationDiscovered'] = True

# required and convenience
products = data['BaseContext']['PlayerStateData']['KnownProducts']
products.append('^U_ADAPTOR')
products.append('^U_ADAPTORCUBE')
products.append('^PURPM_PACKET')
products.append('^PURPM_LUSH_KEY')
products.append('^PURPM_MIRROR')

tech = data['BaseContext']['PlayerStateData']['KnownTech']
tech.append('^FRE_ROOM_TELEPO')
tech.append('^FRE_ROOM_SCAN')
tech.append('^FRE_ROOM_TECH')
tech.append('^FRE_ROOM_SHOP')
tech.append('^FRE_ROOM_PLANT0')
tech.append('^FRE_ROOM_PLANT1')
tech.append('^ATLAS_SEED_1')
tech.append('^ATLAS_SEED_2')
tech.append('^ATLAS_SEED_3')
tech.append('^ATLAS_SEED_4')
tech.append('^ATLAS_SEED_5')
tech.append('^ATLAS_SEED_6')
tech.append('^ATLAS_SEED_7')
tech.append('^ATLAS_SEED_8')
tech.append('^ATLAS_SEED_9')
tech.append('^ATLAS_SEED_10')
tech.append('^STAFF_PART_A')
tech.append('^STAFF_PART_B')
tech.append('^STAFF_PART_C')
tech.append('^UT_BUI_SCAN')
tech.append('^UT_BUI_SCAN2')
tech.append('^HDRIVEBOOST4')

with open("out.json", "w") as outfile:
    json.dump(data, outfile, indent=2)
