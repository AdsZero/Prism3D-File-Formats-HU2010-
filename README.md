
# HU2010 file formats <br />

## Templates
| №   | Format        |   Hexinator  | 010 Editor  | ImHex |  Progress   | Description | Functioning |
| :----- | :--------- | :----------- | :---------- | :---------- | :----------: |:---------- | :----------: |
| 1   | .lnd        | [lnd.grammar](https://github.com/AdsZero/Prism3D-File-Formats-HU2010-/tree/main/templates/hexinator/lnd.grammar) | ... | [lnd.hexpat](https://github.com/AdsZero/Prism3D-File-Formats-HU2010-/tree/main/templates/ImHex/lnd.hexpat) |  95%  |  Location  | :heavy_check_mark: |
| 2   | .tobj       | [tobj.grammar](https://github.com/AdsZero/Prism3D-File-Formats-HU2010-/tree/main/templates/hexinator/tobj.grammar) | [tobj.bt](https://github.com/AdsZero/Prism3D-File-Formats-HU2010-/tree/main/templates/010%20Editor/tobj.bt) | [tobj.hexpat](https://github.com/AdsZero/Prism3D-File-Formats-HU2010-/tree/main/templates/ImHex/tobj.hexpat) |  90%  |  Texture Object  | :heavy_check_mark: |
| 3   | .pmc        | [pmc.grammar](https://github.com/AdsZero/Prism3D-File-Formats-HU2010-/tree/main/templates/hexinator/pmc.grammar)  | ... | ... |  30%  |  Model Collision  | :heavy_check_mark:* |
| 4   | .pma        | [pma.grammar](https://github.com/AdsZero/Prism3D-File-Formats-HU2010-/tree/main/templates/hexinator/pma.grammar)  | ... |  [pma.hexpat](https://github.com/AdsZero/Prism3D-File-Formats-HU2010-/tree/main/templates/ImHex/pma.hexpat)  |  70%  |  Model Animation  | :x: |
| 5   | .pmg       | ... | ... | ... |  0%  |  Model Geometry  | :x: |
| 6   | .pmd       | ... | ... | ... |  0%  |  Model Descriptor  | :x: |
| 7   | .ai       | ... | ... | ... |  0%  |  Logic  | :x: |

> [!IMPORTANT]
> *pmc - It works with the "ai_test" location collision. 
> Condition: the collision file is designed for one mesh and the collision type is Convex or Mesh.

## Tools
<div align="left">
  <table border="0" cellspacing="0" cellpadding="0">
    <tr>
      <td width="150" valign="top" style="border: none;">
        <img src="https://github.com/AdsZero/Prism3D-File-Formats-HU2010-/blob/main/tools/TOBJ%20Viewer/icon.png" alt="Logo" width="150">
      </td>
      <td valign="top" style="border: none;">
        <h4>TOBJ Viewer</h4>
        <p>Viewing and editing tobj format files.</p>
        <a href="https://github.com/AdsZero/Prism3D-File-Formats-HU2010-/tree/main/tools/TOBJ%20Viewer">
          <img src="https://img.shields.io/badge/Download-green" alt="Download">
        </a>
      </td>
    </tr>
  </table>
</div>

## Scripts
- [pmc_info.py](https://github.com/AdsZero/Prism3D-File-Formats-HU2010-/tree/main/scripts/pmc_info.py) - Using this script, you can view information about the pmc file. Drag and drop the pmc file onto the script.
- [convert_coordinates.py](https://github.com/AdsZero/Prism3D-File-Formats-HU2010-/tree/main/scripts/convert_coordinates.py) - This script converts the coordinates of the objects to a normal view. Place the script next to the "landscape.game.sii" and run it.
