#pragma name "Prism3D (.tobj)"
#pragma description "Prism3D Texture Object Format (.tobj)"
#pragma category "Game Assets/3D"
#pragma author "Adyusha"
#pragma version "1.0"
#pragma date "2024-02-23"

#pragma magic [ 01 0A B1 70] @ 0x00
#pragma file_extensions tobj

#pragma array_limit 0xFFFF
#pragma pattern_limit 0xFFFFF

struct TOBJ_file {
    char unknown[0x28] [[comment("It is often repeated. It is possible to adjust the display of the image in the game")]];
    u32 path_length [[comment("The length of the string specifying the path to the file")]];
    u32 null_terminator [[comment("Null-terminated string")]];
    char path [path_length] [[comment("The path to the file")]];
};
    
TOBJ_file FileStructure @ 0x00;
