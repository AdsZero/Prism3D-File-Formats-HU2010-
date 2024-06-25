import struct
import sys

if len(sys.argv) < 2:
    print("Usage: python script.py <file_path>")
    sys.exit(1)

file_path = sys.argv[1]

with open(file_path, 'rb') as file:
    # Reading the header of the PMC file
    file_version = struct.unpack('<I', file.read(4))[0]
    collision_type = struct.unpack('<I', file.read(4))[0]
    collision_count = struct.unpack('<I', file.read(4))[0]
    materials_count = struct.unpack('<I', file.read(4))[0]
    mesh_count = struct.unpack('<I', file.read(4))[0]

    # Unknown pattern
    rows =collision_count
    cols = 3
    s_array = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            s_array[i][j] = struct.unpack('<I', file.read(4))[0]

    # Sections
    rows = collision_count
    cols = 2
    x_array = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            x_array[i][j] = struct.unpack('<I', file.read(4))[0]

    # Pattern
    rows = collision_count
    cols = 4
    y_array = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            y_array[i][j] = struct.unpack('<I', file.read(4))[0]
            
    # Materials
    mat_array = []
    for i in range(materials_count):
        material_value = struct.unpack('<I', file.read(4))[0]
        mat_array.append(material_value)
    
    # Vertices and indexes (number)
    rows = mesh_count
    cols = 4
    vi_array = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            vi_array[i][j] = struct.unpack('<I', file.read(4))[0]

    end_section = struct.unpack('<I', file.read(4))[0]

    # Coordinates
    rows = int(vi_array[0][1])
    cols = 3
    e_array = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            e_array[i][j] = struct.unpack('<f', file.read(4))[0]

    # Indexes
    x = int(vi_array[0][0])
    y = int(x/3)
    rows = y
    cols = 3
    ry_array = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            ry_array[i][j] = struct.unpack('<h', file.read(2))[0]
    # End file
    rows = mesh_count
    cols = 5
    rty_array = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            rty_array[i][j] = struct.unpack('<I', file.read(4))[0]
            
    #cf_section = struct.unpack('<I', file.read(4))[0]
    #ff_section = struct.unpack('<I', file.read(4))[0]


print("""    
  _    __               __         _   
 /_|  /  ) (__/  /  /  (    )__/  /_| 
(  | /(_/   /   (__/  __)  /  /  (  | 
""")
    
print("Information about the PMC file")
print("File Version: ",file_version)
print("Type of Collision: ",collision_type)
print("Number of Collisions: ",collision_count)
print("Number of Materials: ",materials_count)
print("Number of Meshes: ",mesh_count)
print("Pointers to an unknown pattern: ",(s_array))
print("Pointers to sections: ",(x_array))
print("Pattern: ",(y_array))
print("Materials: ",(mat_array))
print("Vertices and Indexes: ",(vi_array))
print("Number of Indexes: ",(vi_array[0][0]))
print("Number of Vertices: ",(vi_array[0][1]))
print("The beginning of the end of the file: ",(vi_array[0][0]))
print("=======================================================") 
for i in range(len(e_array)):
    print("#", i+1, "Coordinates of the vertex [", i,"] : ", e_array[i])
print("=======================================================")    
for i in range(len(ry_array)):
    print("#", i+1, "Triangle indexes [", i,"] : ",(ry_array[i]))
print("End of file pattern: ",(rty_array))
#print("End of file: ", cf_section," ", ff_section)
input("Press Enter to continue...")
