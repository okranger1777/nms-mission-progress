#!/usr/bin/env python3
import xml.etree.ElementTree as ET
# reads "rewards.xml" from unzipped NMSSaveEditor.jar nomanssave/db folder
# prints expedition rewards for MacOS GcUserSettingsData.mxml 
# see https://gist.github.com/okranger1777/1da6e36e9b28aa9fdff5c2203fdd4802

def read_xml_file(filename):
  try:
    tree = ET.parse(filename)
    root = tree.getroot()
    return root
  except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
    return None
  except ET.ParseError as e:
    print(f"Error parsing XML file '{filename}': {e}")
    return None

mylist = []
if __name__ == "__main__":
  root_element = read_xml_file("rewards.xml")
  if root_element:
    for e in root_element.findall('season'):
      r = e.get('id')
      mylist.append(r[1:])

mylist.sort()
for index, item in enumerate(mylist):
  print(f'\t\t<Property name="UnlockedSeasonRewards" value="{item}" _index="{index}" />')



