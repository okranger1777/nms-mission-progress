#!/usr/bin/env python3
import io
import sys
import json

if len(sys.argv) < 2:
  print(f'Usage: {sys.argv[0]} EXPORTED-NMS-SAVE-JSON-FILE')
  sys.exit()
with io.open(sys.argv[1],'r',encoding="utf-8") as myfile: mystring = myfile.read()
data = json.loads(mystring)
# line numbers: 10-19 for Player Hotkeys 0-9, lines 20-29 for Ship, 30-39 for Exocraft
player = [ { "Action": {"QuickMenuActions": "None"}, "Id": "^", "Number": 0, "InventoryIndex": {"X": -1, "Y": -1} },
        { "Action": {"QuickMenuActions": "VehicleAIToggle"}, "Id": "^", "Number": 0, "InventoryIndex": {"X": -1, "Y": -1} }, 
        { "Action": {"QuickMenuActions": "None"}, "Id": "^", "Number": 0, "InventoryIndex": {"X": -1, "Y": -1} }, 
        { "Action": {"QuickMenuActions": "None"}, "Id": "^", "Number": 0, "InventoryIndex": {"X": -1, "Y": -1} }, 
        { "Action": {"QuickMenuActions": "SwapMultitool"}, "Id": "^", "Number": 0, "InventoryIndex": {"X": -1, "Y": -1} }, 
        { "Action": {"QuickMenuActions": "SwapMultitool"}, "Id": "^", "Number": 1, "InventoryIndex": {"X": -1, "Y": -1} }, 
        { "Action": {"QuickMenuActions": "ThirdPersonCharacter"}, "Id": "^", "Number": 0, "InventoryIndex": {"X": -1, "Y": -1} }, 
        { "Action": {"QuickMenuActions": "CallFreighter"}, "Id": "^", "Number": 0, "InventoryIndex": {"X": -1, "Y": -1} }, 
        { "Action": {"QuickMenuActions": "Emote"}, "Id": "^EMOTE_WAVE", "Number": 0, "InventoryIndex": {"X": -1, "Y": -1} }, 
        { "Action": {"QuickMenuActions": "PhotoMode"}, "Id": "^", "Number": 0, "InventoryIndex": {"X": -1, "Y": -1} } ]
ship = [ { "Action": {"QuickMenuActions": "None"}, "Id": "^", "Number": 0, "InventoryIndex": {"X": -1, "Y": -1} },
        { "Action": {"QuickMenuActions": "None"}, "Id": "^", "Number": 0, "InventoryIndex": {"X": -1, "Y": -1} }, 
        { "Action": {"QuickMenuActions": "None"}, "Id": "^", "Number": 0, "InventoryIndex": {"X": -1, "Y": -1} }, 
        { "Action": {"QuickMenuActions": "None"}, "Id": "^", "Number": 0, "InventoryIndex": {"X": -1, "Y": -1} }, 
        { "Action": {"QuickMenuActions": "CargoShield"}, "Id": "^", "Number": 0, "InventoryIndex": {"X": -1, "Y": -1} }, 
        { "Action": {"QuickMenuActions": "EconomyScan"}, "Id": "^", "Number": 1, "InventoryIndex": {"X": -1, "Y": -1} }, 
        { "Action": {"QuickMenuActions": "ThirdPersonShip"}, "Id": "^", "Number": 0, "InventoryIndex": {"X": -1, "Y": -1} }, 
        { "Action": {"QuickMenuActions": "CallFreighter"}, "Id": "^", "Number": 0, "InventoryIndex": {"X": -1, "Y": -1} }, 
        { "Action": {"QuickMenuActions": "None"}, "Id": "^", "Number": 0, "InventoryIndex": {"X": -1, "Y": -1} }, 
        { "Action": {"QuickMenuActions": "PhotoMode"}, "Id": "^", "Number": 0, "InventoryIndex": {"X": -1, "Y": -1} } ]
exocraft = [ { "Action": {"QuickMenuActions": "None"}, "Id": "^", "Number": 0, "InventoryIndex": {"X": -1, "Y": -1} },
        { "Action": {"QuickMenuActions": "None"}, "Id": "^", "Number": 0, "InventoryIndex": {"X": -1, "Y": -1} }, 
        { "Action": {"QuickMenuActions": "None"}, "Id": "^", "Number": 0, "InventoryIndex": {"X": -1, "Y": -1} }, 
        { "Action": {"QuickMenuActions": "None"}, "Id": "^", "Number": 0, "InventoryIndex": {"X": -1, "Y": -1} }, 
        { "Action": {"QuickMenuActions": "None"}, "Id": "^", "Number": 0, "InventoryIndex": {"X": -1, "Y": -1} }, 
        { "Action": {"QuickMenuActions": "None"}, "Id": "^", "Number": 0, "InventoryIndex": {"X": -1, "Y": -1} }, 
        { "Action": {"QuickMenuActions": "ThirdPersonVehicle"}, "Id": "^", "Number": 0, "InventoryIndex": {"X": -1, "Y": -1} }, 
        { "Action": {"QuickMenuActions": "VehicleScanSelect"}, "Id": "^", "Number": 0, "InventoryIndex": {"X": -1, "Y": -1} }, 
        { "Action": {"QuickMenuActions": "None"}, "Id": "^", "Number": 0, "InventoryIndex": {"X": -1, "Y": -1} }, 
        { "Action": {"QuickMenuActions": "PhotoMode"}, "Id": "^", "Number": 0, "InventoryIndex": {"X": -1, "Y": -1} } ]

data['BaseContext']['PlayerStateData']['HotActions'][0]['KeyActions'] = player
data['BaseContext']['PlayerStateData']['HotActions'][1]['KeyActions'] = ship
data['BaseContext']['PlayerStateData']['HotActions'][2]['KeyActions'] = exocraft

with open("out.json", "w") as outfile:
    json.dump(data, outfile, indent=2)

