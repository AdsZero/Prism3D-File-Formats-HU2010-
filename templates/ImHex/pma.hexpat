#pragma name "PMA Animation File"
#pragma description "Grammar for PMA animation files"
#pragma category "Game Assets/3D"
#pragma author "Adyusha"
#pragma version "1.0"
#pragma file_extensions pma

#pragma array_limit 0xFFFFFF
#pragma pattern_limit 0xFFFFFFF

// Bone Transform structure - вынесена на верхний уровень
struct BoneTransform {
    // Unknown 4x u32 values
    u32 unknown_val1 [[color("C3B882"), name("Unknown 1"), comment("Unknown value 1")]];
    u32 unknown_val2 [[color("C3B882"), name("Unknown 2"), comment("Unknown value 2")]];
    u32 unknown_val3 [[color("C3B882"), name("Unknown 3"), comment("Unknown value 3")]];
    u32 unknown_val4 [[color("C3B882"), name("Unknown 4"), comment("Unknown value 4")]];
    
    // Rotation quaternion
    le float rot_x [[color("FF0000"), name("Rotation X"), comment("X component of rotation quaternion")]];
    le float rot_y [[color("00FF00"), name("Rotation Y"), comment("Y component of rotation quaternion")]];
    le float rot_z [[color("0000FF"), name("Rotation Z"), comment("Z component of rotation quaternion")]];
    le float rot_w [[color("FFFF7F"), name("Rotation W"), comment("W component of rotation quaternion")]];
    
    // Position vector
    le float pos_x [[color("FF0000"), name("Position X"), comment("X position coordinate")]];
    le float pos_y [[color("00FF00"), name("Position Y"), comment("Y position coordinate")]];
    le float pos_z [[color("0000FF"), name("Position Z"), comment("Z position coordinate")]];
    
    // Scale vector
    le float scale_x [[color("FF0000"), name("Scale X"), comment("X scale factor")]];
    le float scale_y [[color("00FF00"), name("Scale Y"), comment("Y scale factor")]];
    le float scale_z [[color("0000FF"), name("Scale Z"), comment("Z scale factor")]];
};

// Bone Animation structure - вынесена на верхний уровень
struct BoneAnimation {
    BoneTransform Keyframes[parent.Keys] [[name("Keyframes"), comment("Animation keyframes for this bone")]];
};

// Main PMA File Structure
struct PMA_file {
    // Header section
    le u32 FileVersion [[color("FF557F"), name("File Version"), comment("Version of the PMA file")]];
    u8 unknown1 [[name("Unknown 1"), comment("Unknown value")]];
    
    u8 unknown5_byte1 [[name("Unknown 5 byte 1"), comment("Part of Unknown 5")]];
    u8 unknown5_byte2 [[name("Unknown 5 byte 2"), comment("Part of Unknown 5")]];
    u8 unknown5_byte3 [[name("Unknown 5 byte 3"), comment("Part of Unknown 5")]];
    
    le u32 unknown2 [[name("Unknown 2"), comment("Unknown value")]];
    le u32 Keys [[color("AAFF00"), name("Keys Count"), comment("Number of animation keys/frames")]];
    le u32 Bones [[color("AAFF7F"), name("Bones Count"), comment("Number of bones")]];
    le u32 unknown [[name("Unknown"), comment("Unknown value")]];
    
    le u32 StartKEYS [[name("Start KEYS"), comment("Start of KEYS array")]];
    le u32 StartID [[color("005500"), name("Start ID"), comment("Start ID")]];
    le u32 EndID [[color("00AA00"), name("End ID"), comment("End ID")]];
    le u32 HEXLength [[color("AA55FF"), name("HEX Length"), comment("Length in hexadecimal")]];
    le u32 unknown4 [[name("Unknown 4"), comment("Unknown value")]];
    
    // KEYS array
    le u32 KeyValues[Keys] [[color("55FFFF"), name("KEYS"), comment("Animation keys array")]];
    
    // ID array
    u8 IDs[Bones] [[color("FF55FF"), name("Bone IDs"), comment("Bone identification numbers")]];
    
    // Array of bone animations
    BoneAnimation BoneAnimations[Bones] [[color("C3B882"), name("Bone Animations"), comment("Animation data for all bones")]];
};

// Create the main structure instance
PMA_file PMAStructure @ 0x00;