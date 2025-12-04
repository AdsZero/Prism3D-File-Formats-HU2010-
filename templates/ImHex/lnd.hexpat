#pragma name "Prism3D (.lnd)"
#pragma description "Prism3D Location Format (.lnd)"
#pragma category "Game Assets/3D"
#pragma author "Adyusha"
#pragma version "1.0"
#pragma date "2025-12-04"

#pragma magic [ 05 00 00 00 ?? ?? ?? ?? ?? ?? ?? ?? 10] @ 0x00
#pragma file_extensions lnd

struct Vector3f {
    le float coord_x [[color("FF0000"), name("Coordinate X"), comment("X coordinate")]];
    le float coord_y [[color("55AA00"), name("Coordinate Y"), comment("Y coordinate")]]; 
    le float coord_z [[color("0055FF"), name("Coordinate Z"), comment("Z coordinate")]];
};

struct TextureData {
    le float scale [[color("707070"), name("Scale"), comment("Texture scaling")]];
    le float n1 [[color("505050"), name("n1"), comment("Unknown value")]]; 
    le float n2 [[color("303030"), name("n2"), comment("Unknown value")]]; 
};

struct UV_MATERIAL {
    TextureData texture_0 [[name("Texture 1"), comment("Texture")]];
    TextureData texture_1 [[name("Texture 2"), comment("Texture")]];
    TextureData texture_2 [[name("Texture 3"), comment("Texture")]];
};

struct SECTION {
    Vector3f pointA [[name("point A"), comment("point A")]];
    Vector3f pointB [[name("point B"), comment("point B")]];
    le u16 TAB [[color("C0C0C0"), name("TAB"), comment("Indentation between bytes")]];
    UV_MATERIAL UV_Materials[parent.Material] [[name("UV Materials"), comment("UV Materials")]];
};

struct LND_file {
    le u32 Version [[color("C7D100"), name("File Version"), comment("File Version")]]; 
    le u32 Meshes [[color("A3AB00"), name("Meshes"), comment("Defines the number of Sections")]]; 
    le u32 Material [[color("6F7500"), name("Material"), comment("Defines the size of the UV_MATERIAL array inside each section")]];
    le u32 HeaderSize [[color("444700"), name("Header Size"), comment("Header size")]];
    
    SECTION Sections[Meshes] [[name("Sections"), comment("Sections or chunks that contain meshes")]];
};

LND_file FileStructure @ 0x00;
