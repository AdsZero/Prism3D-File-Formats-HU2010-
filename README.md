
# HU2010 file formats <br />

## Templates
| № | Format        |   Hexinator  | 010 Editor  | ImHex |  Progress   | Description | Functioning |
| :--- | :--------- | :----------- | :---------- | :---------- | :----------: |:---------- | :----------: |
| 1 | .lnd        | [lnd.grammar](https://github.com/AdsZero/Prism3D-File-Formats-HU2010-/tree/main/templates/hexinator/lnd.grammar) | ... | ... |  95%  |  Location  | :heavy_check_mark: |
| 2 | .tobj       | [tobj.grammar](https://github.com/AdsZero/Prism3D-File-Formats-HU2010-/tree/main/templates/hexinator/tobj.grammar) | [tobj.bt](https://github.com/AdsZero/Prism3D-File-Formats-HU2010-/tree/main/templates/010%20Editor/tobj.bt) | [tobj.hexpat](https://github.com/AdsZero/Prism3D-File-Formats-HU2010-/tree/main/templates/ImHex/tobj.hexpat) |  90%  |  Texture Object  | :heavy_check_mark: |
| 3 | .pmc        | [pmc.grammar](https://github.com/AdsZero/Prism3D-File-Formats-HU2010-/tree/main/templates/hexinator/pmc.grammar)  | ... | ... |  30%  |  Model Collision  | :heavy_check_mark:* |
| 4 | .pma        | [pma.grammar](https://github.com/AdsZero/Prism3D-File-Formats-HU2010-/tree/main/templates/hexinator/pma.grammar)  | ... | ... |  70%  |  Model Animation  | :x: |
| 5 | .pmg       | ... | ... | ... |  0%  |  Model Geometry  | :x: |
| 6 | .pmd       | ... | ... | ... |  0%  |  Model Descriptor  | :x: |
| 7 | .ai       | ... | ... | ... |  0%  |  Logic  | :x: |

> [!IMPORTANT]
> *pmc - It works with the "ai_test" location collision. 
> Condition: the collision file is designed for one mesh and the collision type is Convex or Mesh.

## Scripts
- [pmc_info.py](https://github.com/AdsZero/Prism3D-File-Formats-HU2010-/tree/main/scripts/pmc_info.py) - Using this script, you can view information about the pmc file. Drag and drop the pmc file onto the script.
- [convert_coordinates.py](https://github.com/AdsZero/Prism3D-File-Formats-HU2010-/tree/main/scripts/convert_coordinates.py) - This script converts the coordinates of the objects to a normal view. Place the script next to the "landscape.game.sii" and run it.
