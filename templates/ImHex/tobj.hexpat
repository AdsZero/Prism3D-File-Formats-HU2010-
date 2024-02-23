#pragma author Adyusha
#pragma description tobj Prism3D file

struct TOBJ {
    char unknown[0x28] [[comment("It is often repeated. It is possible to adjust the display of the image in the game")]];
    u32 path_length [[comment("The length of the string specifying the path to the file")]];
    u32 null_terminator [[comment("Null-terminated string")]];
    char path [path_length] [[comment("The path to the file")]];
    };
TOBJ tobj @ 0x00;