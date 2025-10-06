
# nms-mission-progress

Work in progress scripts and reference files for No Man's Sky (NMS) save JSON, including updating MissionProgress with simple YAML input.

## Introduction

At time of this writing, none of the major NMS save editors provided a UI to update MissionProgress, where NMS tracks storyline completion. 

Editing the raw JSON allows completing missions, but can be tedious. For a clear example, see 
"Complete the Artemis Story w/JSON Data By Geldric™" here:

https://steamcommunity.com/sharedfiles/filedetails/?id=3026134039

You can complete additional missions using the same method, see the YAML files in [missions](missions/). For example, to complete Dreams of the Deep, update the raw JSON and set Progress for the following missions:

```
^WATERSTORY1: 11
^WATERSTORY2: 12
^WATERSTORY3: 12
^WATERSTORY4: 8
^WATERSTORY5: 38
^WATERSTORY_LORE: 10
```

Ideally, mission completion will be added to NMS save editors.


## Warnings

__USE AT YOUR OWN RISK__

Editing NMS save files is very risky and may result in a corrupt, unplayable save.
Keep backups and test them before proceeding.

For these reasons, create a new Creative mode NMS save file to test the `update-nms-mission-progress.py` script until the mechanics are fully documented.

## Requirements

* A new Creative NMS save file
* NMS save editor to export as JSON, tested with https://github.com/goatfungus/NMSSaveEditor
* (Optional) To query and format JSON, `jq` and `gron` and the Python library `compact-json`
* Python and the library `PyYAML`

To install PyYAML:
```bash
pip3 install PyYAML
```

## Usage

Example YAML extracts from other save files are in the `references` directory.

### `update-nms-mission-progress.py`

This script reads `steps.yaml` and outputs the `out.json` file, which you 
can import using an NMS save editor. 

The example `steps.yaml` completes all MissionProgress in the main storyline
prior to Worlds Part II as well as several other side missions.

1. Start a new Creative NMS save
1. Name your save and create a Restore Point with your ship
1. Quit the save
1. Open the NMS save editor, choose your save and Export JSON
1. Run the script, which creates the `out.json` file
1. In the NMS save editor, use Import JSON with `out.json`

Example script command 

```bash
./update-nms-mission-progress.py ~/Downloads/exported/save123.hg.json
```

See [CLI.md](docs/CLI.md) for a longer command line example.

Congratulations! You now have a No Man's Sky Creative "Plus Plus" save with the main storyline completed and all special tech and products unlocked.


## Other Scripts

The [scripts](scripts/) can be used to understand save JSON details, see [Methodology.md](docs/Methodology.md).

### `extract-nms-mission-progress.py`

This will output YAML:

```bash
./extract-nms-mission-progress.py ~/Downloads/exported/save123.hg.json | sort
```

### `nomanssave-rewards.py`

MacOS specific, see https://gist.github.com/okranger1777/1da6e36e9b28aa9fdff5c2203fdd4802

Run this script in unzipped NMSSaveEditor.jar nomanssave/db folder to read "rewards.xml"
and print expedition rewards for MacOS `GcUserSettingsData.mxml` file.


## License

This project is licensed under the MIT license - see the [LICENSE](LICENSE)
file for details.


