
# nms-mission-progress

Work in progress scripts to extract and update MissionProgress in No Man's Sky (NMS) save JSON.

## Introduction

At time of this writing, none of the major NMS save editors provided a way to update MissionProgress,
where NMS tracks storyline completion.

This project has demonstration scripts to extract MissionProgress from a save JSON and update 
using values in the `steps.yaml` file.

Example YAML extracts from other save files are in the `references` directory.


## Warnings

__USE AT YOUR OWN RISK__

Editing NMS save files is very risky and may result in a corrupt, unplayable save.

Additionally, NMS mission progress is not always simple. For example, you may need a specific 
technology or item in inventory for a step to work properly. This is particularly true of the
"Expanding the Base" missions.

For these reasons, test the `update-nms-mission-progress.py` script with a new Creative mode 
NMS save file until the mechanics are fully documented.

That said, some of the side missions are very straightforward. 
For example, this YAML clears the "Dreams of the Deep" mission:

```
^WATERSTORY1: 11
^WATERSTORY2: 12
^WATERSTORY3: 12
^WATERSTORY4: 8
^WATERSTORY5: 38
^WATERSTORY_LORE: 10
```

Also, the Purple systems introduced in Worlds Part II require only one setting and one 
known technology; the `enable-purple-warp.py` script will update a JSON without requiring
the mission.


## Requirements

* A new Creative NMS save
* NMS save editor to export the save file as JSON, tested with https://github.com/goatfungus/NMSSaveEditor
* (Optional) `jq` to format and query JSON
* Python with the PyYAML library installed

To install PyYAML:
```bash
pip3 install PyYAML
```

## Usage

### `enable-purple-warp.py`

1. Open the NMS save editor, open your new save and Export JSON
1. Run `./enable-purple-warp.py your-export.json`
1. In the NMS save editor, import the `out.json` file created by the script


### `extract-nms-mission-progress.py`

1. Start a new Creative NMS save
1. Save a Restore Point with your ship
1. Quit the save
1. Open the NMS save editor, open your new save and Export JSON

Simple extract usage:
```bash
./extract-nms-mission-progress.py ~/Downloads/mysave.json | sort
```

### `update-nms-mission-progress.py`

This script reads `steps.yaml` and outputs the `out.json` file, which you 
can import using an NMS save editor. 

The example `steps.yaml` completes all MissionProgress in the main storyline
prior to Worlds Part II as well as several other missions.


```bash
./update-nms-mission-progress.py ~/Downloads/mysave.json
```


### libNOM CLI

Here is example update usage on a Mac with the libNOM CLI installed and on your PATH: https://github.com/zencq/libNOM.io

Change the first two lines to match your system. If not using Steam, use `libNOM.io.cli -H` to 
determine the correct format option to use.

```bash

SAVEDIR="$HOME/Library/Application Support/HelloGames/NMS/st_1234..."
SAVEFILE="save10.hg"

mkdir backups/$(date +%s)
cp "$SAVEDIR/$SAVEFILE" backups/$(date +%s)
cp "$SAVEDIR/mf_$SAVEFILE" backups/$(date +%s)

FNAME=creative.json

# convert save to JSON
libNOM.io.cli Read -Input "$SAVEDIR/$SAVEFILE" -J True > "$HOME/Downloads/$FNAME"

# update script writes to out.json
./update-nms-mission-progress.py "$HOME/Downloads/$FNAME"

# write JSON to save
cat out.json | libNOM.io.cli Write -O st -F Steam -I 1
mv st/*data "$SAVEDIR/$SAVEFILE"
mv st/*meta "$SAVEDIR/mf_$SAVEFILE"
```


## License

This project is licensed under the MIT license - see the [LICENSE](LICENSE)
file for details.

