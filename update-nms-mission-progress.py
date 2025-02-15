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


def add_product(data, product):
  products = data['BaseContext']['PlayerStateData']['KnownProducts']
  if product not in products:
    products.append(product)


def add_tech(data, tech):
  tech_known = data['BaseContext']['PlayerStateData']['KnownTech']
  if tech not in tech_known:
    tech_known.append(tech)


missions = data['BaseContext']['PlayerStateData']['MissionProgress']
for idx, i in enumerate(missions):
  m = i['Mission']
  progress = i['Progress']
  if m in step_ref:
    logging.debug(f'Found mission {m}')
    complete_step(data, m, idx)

# set by first Anomaly conversations
data['BaseContext']['PlayerStateData']['HasAccessToNexus'] = True
data['BaseContext']['PlayerStateData']['RevealBlackHoles'] = True
data['BaseContext']['PlayerStateData']['FirstAtlasStationDiscovered'] = True
# after In Stellar Multitudes
data['BaseContext']['PlayerStateData']['HasDiscoveredPurpleSystems'] = True

# required for completing Artemis Path, Atlas Path, and Stellar Multitudes
add_product(data, '^BUILDSIGNAL')
add_product(data, '^ATLAS_SEED_2')
add_product(data, '^ATLAS_SEED_3')
add_product(data, '^ATLAS_SEED_4')
add_product(data, '^ATLAS_SEED_5')
add_product(data, '^ATLAS_SEED_6')
add_product(data, '^ATLAS_SEED_7')
add_product(data, '^ATLAS_SEED_8')
add_product(data, '^ATLAS_SEED_9')
add_product(data, '^ATLAS_SEED_10')
add_product(data, '^ATLAS_SEED_1')
add_product(data, '^U_ADAPTOR')
add_product(data, '^U_ADAPTORCUBE')
add_product(data, '^PURPM_PACKET')
add_product(data, '^PURPM_LUSH_KEY')
add_product(data, '^PURPM_MIRROR')

add_tech(data, '^STRONGLASER')
add_tech(data, '^STARSUIT')
add_tech(data, '^STAFF_PART_A')
add_tech(data, '^STAFF_PART_B')
add_tech(data, '^STAFF_PART_C')
add_tech(data, '^HDRIVEBOOST4')

with open("out.json", "w") as outfile:
    json.dump(data, outfile, indent=2)
