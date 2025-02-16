
# nms-mission-progress

Work in progress scripts for No Man's Sky (NMS) save JSON, including updating MissionProgress
with simple YAML input.

## Introduction

At time of this writing, none of the major NMS save editors provided a UI to update MissionProgress,
where NMS tracks storyline completion. 

Editing the raw JSON allows completing missions, but can be tedious. For example, see 
"Complete the Artemis Story w/JSON Data By Geldric™" here:

https://steamcommunity.com/sharedfiles/filedetails/?id=3026134039

The original goal was to have an easy NMS Creative "Plus Plus" special save with all missions
completed and all tech and products unlocked.

The scripts and mission details in the YAML files can also be used to understand save JSON details.
Ideally, mission completion will be added to NMS save editors.


## Warnings

__USE AT YOUR OWN RISK__

Editing NMS save files is very risky and may result in a corrupt, unplayable save.
Always keep backups.

For these reasons, test the `update-nms-mission-progress.py` script with a new Creative mode 
NMS save file until the mechanics are fully documented.

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
prior to Worlds Part II as well as several other missions.

### `extract-nms-mission-progress.py`

1. Start a new Creative NMS save
1. Name your save and create a Restore Point with your ship
1. Quit the save
1. Open the NMS save editor, open your save and Export JSON
1. Run the script, which creates the `out.json` file
1. In the NMS save editor, use Import JSON with `out.json`

Example script command 

```bash
./update-nms-mission-progress.py ~/Downloads/mysave.json
```

See [CLI.md](docs/CLI.md) for a longer command line example.


### Extract Missions

This will output YAML:

```bash
./extract-nms-mission-progress.py ~/Downloads/mysave.json | sort
```


## License

This project is licensed under the MIT license - see the [LICENSE](LICENSE)
file for details.

