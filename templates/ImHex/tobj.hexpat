/*!
 * TOBJ File Format (ImHex Template)
 * ----------------------------------------------------------------------
 * File format: TOBJ
 * Description: A template for analyzing the file format in which a 3D model texture object is stored
 * Format version: 1.0
 * Template author: Adyusha
 * Date of creation: 23/02/2024
 * ----------------------------------------------------------------------
 */

#pragma array_limit 0xFFFF
#pragma pattern_limit 0xFFFFF

struct TOBJ_file {
    char unknown[0x28] [[comment("It is often repeated. It is possible to adjust the display of the image in the game")]];
    u32 path_length [[comment("The length of the string specifying the path to the file")]];
    u32 null_terminator [[comment("Null-terminated string")]];
    char path [path_length] [[comment("The path to the file")]];
};
    
TOBJ_file FileStructure @ 0x00;
