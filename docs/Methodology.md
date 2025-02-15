
# Methodology

Comparing changes between two saves may reveal important details.
Here is how I do it.

If at all possible, use one save at different time points, rather than two completely different 
saves. This reduces the amount of extra information when comparing the two versions.

## General Steps

1. Create a restore point and copy the save file
2. Take an action within the game
3. Wait for the game to update the current mission progress, which can take 30 seconds or more
4. Create a new restore point
5. Create JSON and `gron` text outputs of the before and after restore points
6. Compare the differences in the text outputs

## Example 

Here are some of the changes in a save at the end of the Atlas Path.

Both restore points were created within the Atlas Station, before and after the final "Birth a New Star" Atlas encounter.

See [CLI.md](CLI.md) for details on the scripts used.

The following `diff` output shows:
* CurrentMissionID updated
* Player Energy level changed
* Inventory slot is emptied because "Heart of the Sun" was consumed
* Tech for "Star Seed" was learned
* MissionProgress was set for 3 existing missions: HAS_STARSEED, ATLAS11, and ATLAS_LOOP_STAR (IDs found in the full output)

The full comparison shows over 200 lines were changed! 
Many of the changes are timestamps or other small differences.

```diff
5493c5493
< json.BaseContext.PlayerStateData.CurrentMissionID = "^ATLAS11";
---
> json.BaseContext.PlayerStateData.CurrentMissionID = "^ATLAS_LOOP_STAR";
6433c6433
< json.BaseContext.PlayerStateData.Energy = 90;
---
> json.BaseContext.PlayerStateData.Energy = 83;
8484,8494d8483
< json.BaseContext.PlayerStateData.Inventory.Slots[33] = {};
< json.BaseContext.PlayerStateData.Inventory.Slots[33].Amount = 1;
< json.BaseContext.PlayerStateData.Inventory.Slots[33].DamageFactor = 0.0;
< json.BaseContext.PlayerStateData.Inventory.Slots[33].FullyInstalled = true;
< json.BaseContext.PlayerStateData.Inventory.Slots[33].Id = "^ATLAS_SEED_10";
< json.BaseContext.PlayerStateData.Inventory.Slots[33].Index = {};
< json.BaseContext.PlayerStateData.Inventory.Slots[33].Index.X = 3;
< json.BaseContext.PlayerStateData.Inventory.Slots[33].Index.Y = 3;
< json.BaseContext.PlayerStateData.Inventory.Slots[33].MaxAmount = 1;
< json.BaseContext.PlayerStateData.Inventory.Slots[33].Type = {};
< json.BaseContext.PlayerStateData.Inventory.Slots[33].Type.InventoryType = "Product";
8665c8654
< json.BaseContext.PlayerStateData.Inventory_TechOnly.Slots[0].Amount = 90;
---
> json.BaseContext.PlayerStateData.Inventory_TechOnly.Slots[0].Amount = 83;
9264a9254
> json.BaseContext.PlayerStateData.KnownTech[50] = "^STARSUIT";
37611c37595
< json.BaseContext.PlayerStateData.MissionProgress[187].Progress = -1;
---
> json.BaseContext.PlayerStateData.MissionProgress[187].Progress = 0;
39561c39545
< json.BaseContext.PlayerStateData.MissionProgress[200].Progress = 14;
---
> json.BaseContext.PlayerStateData.MissionProgress[200].Progress = 36;
39711c39695
< json.BaseContext.PlayerStateData.MissionProgress[201].Progress = -1;
---
> json.BaseContext.PlayerStateData.MissionProgress[201].Progress = 1;
```


