#pragma name "PMA Animation File"
#pragma description "PMA animation files"
#pragma category "Game Assets/3D"
#pragma author "Adyusha"
#pragma version "1.0"
#pragma file_extensions pma
#pragma magic [ 03 00 00 00 ] @ 0x00
#pragma array_limit 0xFFFFFF
#pragma pattern_limit 0xFFFFFFF

// ============================================================
// Data structures
// ============================================================

// Bone transform (56 bytes)
struct BoneTransform {
    // 4 unknown u32 values
    le float unknown_val1 [[color("C3B882"), name("Unknown 1")]];
    le float unknown_val2 [[color("C3B882"), name("Unknown 2")]];
    le float unknown_val3 [[color("C3B882"), name("Unknown 3")]];
    le float unknown_val4 [[color("C3B882"), name("Unknown 4")]];
    
    // Rotation quaternion
    le float rot_x [[color("FF0000"), name("Rotation X")]];
    le float rot_y [[color("00FF00"), name("Rotation Y")]];
    le float rot_z [[color("0000FF"), name("Rotation Z")]];
    le float rot_w [[color("FFFF7F"), name("Rotation W")]];
    
    // Position
    le float pos_x [[color("FF0000"), name("Position X")]];
    le float pos_y [[color("00FF00"), name("Position Y")]];
    le float pos_z [[color("0000FF"), name("Position Z")]];
    
    // Scale
    le float scale_x [[color("FF0000"), name("Scale X")]];
    le float scale_y [[color("00FF00"), name("Scale Y")]];
    le float scale_z [[color("0000FF"), name("Scale Z")]];
};

// Animation of a single bone
struct BoneAnimation {
    BoneTransform Keyframes[parent.Keys] [[name("Keyframes")]];
};

// Root motion key (12 bytes)
struct RootMotionKey {
    le float x [[color("FF0000"), name("X")]];
    le float y [[color("00FF00"), name("Y")]];
    le float z [[color("0000FF"), name("Z")]];
};

// ============================================================
// Main file structure
// ============================================================

struct PMA_file {
    // --- Header ---
    le u32 FileVersion [[color("FF557F"), name("File Version")]];
    le u32 unknown1 [[name("Unknown 1")]];
    le u32 unknown2 [[name("Unknown 2")]];
    
    // Number of keys (u16) and root motion presence flag
    le u16 Keys [[color("AAFF00"), name("Keys Count"), comment("Number of animation keys/frames")]];
    le u16 HasRootMotion [[color("FFAA00"), name("Has Root Motion"), comment("0 = no root motion block, 2 = root motion block present")]];

    le u32 Bones [[color("AAFF7F"), name("Bones Count"), comment("Number of bones")]];
    
    // Time of the last keyframe: (Keys - 1) / 24
    le float LastKeyTime [[color("FFAA00"), name("Last Key Time"), comment("Time of the last keyframe = (Keys - 1) / 24")]];
    
    le u32 StartKEYS [[name("Start KEYS"), comment("Offset to KEYS array")]];
    le u32 StartID [[color("005500"), name("Start ID"), comment("Offset to IDs array")]];
    le u32 EndID [[color("00AA00"), name("End ID"), comment("End offset of IDs array")]];
    le u32 HEXLength [[color("AA55FF"), name("HEX Length"), comment("Offset to root motion block (or end of bone animations)")]];
    le u32 EndOfFile [[name("End of file"), comment("End of file or additional data pointer")]];
    
    // --- Keys array (time stamps) ---
    le float KeyValues[Keys] @ StartKEYS [[color("55FFFF"), name("KEYS"), comment("Animation keyframe times (usually 1/24 sec each)")]];
    
    // --- Bone IDs array ---
    u8 IDs[Bones] @ StartID [[color("FF55FF"), name("Bone IDs"), comment("Bone identification numbers")]];
    
    // --- Bone animations ---
    BoneAnimation BoneAnimations[Bones] @ EndID [[color("C3B882"), name("Bone Animations")]];
    
    // --- Root motion block (only if flag == 2) ---
    if (HasRootMotion == 2) {
        RootMotionKey RootMotion[Keys] @ HEXLength [[name("Root Motion"), comment("Global object translation per keyframe")]];
    }
};

// ============================================================
// Entry point
// ============================================================

PMA_file PMAStructure @ 0x00;