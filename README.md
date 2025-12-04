
# HU2010 file formats <br />

## Templates
| Format        |   Hexinator  | 010 Editor  | ImHex |  Progress   | Description | Functioning |
| :--------- | :----------- | :---------- | :---------- | :----------: |:---------- | :----------: |
| .lnd        | [lnd.grammar](https://github.com/AdsZero/Prism3D-File-Formats-HU2010-/tree/main/templates/hexinator/lnd.grammar) | ... | [lnd.hexpat](https://github.com/AdsZero/Prism3D-File-Formats-HU2010-/tree/main/templates/ImHex/lnd.hexpat) |  95%  |  Location  | :heavy_check_mark: |
| .tobj       | [tobj.grammar](https://github.com/AdsZero/Prism3D-File-Formats-HU2010-/tree/main/templates/hexinator/tobj.grammar) | [tobj.bt](https://github.com/AdsZero/Prism3D-File-Formats-HU2010-/tree/main/templates/010%20Editor/tobj.bt) | [tobj.hexpat](https://github.com/AdsZero/Prism3D-File-Formats-HU2010-/tree/main/templates/ImHex/tobj.hexpat) |  90%  |  Texture Object  | :heavy_check_mark: |
| .pmc        | [pmc.grammar](https://github.com/AdsZero/Prism3D-File-Formats-HU2010-/tree/main/templates/hexinator/pmc.grammar)  | ... | ... |  30%  |  Model Collision  | :heavy_check_mark:* |
| .pma        | [pma.grammar](https://github.com/AdsZero/Prism3D-File-Formats-HU2010-/tree/main/templates/hexinator/pma.grammar)  | ... | ... |  70%  |  Model Animation  | :x: |
| .pmg       | ... | ... | ... |  0%  |  Model Geometry  | :x: |
| .pmd       | ... | ... | ... |  0%  |  Model Descriptor  | :x: |
| .ai       | ... | ... | ... |  0%  |  Logic  | :x: |

> [!IMPORTANT]
> *pmc - It works with the "ai_test" location collision. 
> Condition: the collision file is designed for one mesh and the collision type is Convex or Mesh.


## Scripts
- [pmc_info.py](https://github.com/AdsZero/Prism3D-File-Formats-HU2010-/tree/main/scripts/pmc_info.py) - Using this script, you can view information about the pmc file. Drag and drop the pmc file onto the script.
- [convert_coordinates.py](https://github.com/AdsZero/Prism3D-File-Formats-HU2010-/tree/main/scripts/convert_coordinates.py) - This script converts the coordinates of the objects to a normal view. Place the script next to the "landscape.game.sii" and run it.
