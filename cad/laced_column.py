from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_Transform
from OCC.Core.gp import gp_Trsf, gp_Vec, gp_Pnt, gp_Dir, gp_Ax1
from OCC.Display.SimpleGui import init_display
from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs
from OCC.Core.IFSelect import IFSelect_RetDone
from math import sqrt
import os

# === Initialize Viewer ===
display, start_display, add_menu, add_function_to_menu = init_display()

# === Helper Functions ===
def translate(shape, dx=0, dy=0, dz=0):
    trsf = gp_Trsf()
    trsf.SetTranslation(gp_Vec(dx, dy, dz))
    return BRepBuilderAPI_Transform(shape, trsf, True).Shape()

def rotate(shape, axis="Z", angle_deg=0):
    angle_rad = angle_deg * (3.14159265 / 180)
    if axis.upper() == "X":
        rot_axis = gp_Ax1(gp_Pnt(0, 0, 0), gp_Dir(1, 0, 0))
    elif axis.upper() == "Y":
        rot_axis = gp_Ax1(gp_Pnt(0, 0, 0), gp_Dir(0, 1, 0))
    else:
        rot_axis = gp_Ax1(gp_Pnt(0, 0, 0), gp_Dir(0, 0, 1))
    trsf = gp_Trsf()
    trsf.SetRotation(rot_axis, angle_rad)
    return BRepBuilderAPI_Transform(shape, trsf, True).Shape()

# === Parameters ===
column_height = 6100  # mm
gap_between_i_sections = 450  # mm
end_plate_thickness = 10  # mm
end_plate_width = 430  # mm
end_plate_depth = 300  # mm
i_section_width = 200  # mm
i_section_depth = 100  # mm

# === Component Builders ===
def create_i_section():
    return BRepPrimAPI_MakeBox(i_section_width, i_section_depth, column_height).Shape()

def create_end_plate(z_pos):
    plate = BRepPrimAPI_MakeBox(end_plate_width, end_plate_depth, end_plate_thickness).Shape()
    x_shift = - (end_plate_width - i_section_width) / 2
    y_shift = - (end_plate_depth - (gap_between_i_sections + i_section_depth)) / 2
    return translate(plate, x_shift, y_shift, z_pos)

def create_diagonal_lace(z_start, flip=False):
    vert = 480
    horiz = gap_between_i_sections
    diag_len = sqrt(vert**2 + horiz**2)
    lace = BRepPrimAPI_MakeBox(100, 8, diag_len).Shape()
    lace = rotate(lace, "Z", 90)
    angle = -40 if not flip else 40
    lace = rotate(lace, "X", angle)
    x_shift = (i_section_width - 100) / 2 
    y_shift = 20 if not flip else gap_between_i_sections 
    return translate(lace, x_shift, y_shift, z_start)

def create_horizontal_lace(z_pos, x_offset):
    length = gap_between_i_sections
    lace = BRepPrimAPI_MakeBox(8, length, 100).Shape()
    x_shift = (i_section_width - 8) / 2 + x_offset - 55
    y_shift = 40
    z_shift = z_pos
    return translate(lace, x_shift, y_shift, z_shift)

# === Build Main Geometry ===
i1 = create_i_section()
i2 = translate(i1, 0, gap_between_i_sections, 0)
top_plate = create_end_plate(column_height)
bottom_plate = create_end_plate(0)

laces = []
z = 0
offset_flip = False

while z + 450 <= column_height:
    offset_x1 = 149 if offset_flip else -40
    offset_x2 = -40 if offset_flip else 149

    flip1 = offset_x1 == -40
    lace1 = create_diagonal_lace(z, flip=flip1)
    lace1 = translate(lace1, dx=offset_x1)
    laces.append(lace1)

    flip2 = offset_x2 == -40
    lace2 = create_diagonal_lace(z, flip=flip2)
    lace2 = translate(lace2, dx=offset_x2)
    laces.append(lace2)

    h_lace1 = create_horizontal_lace(z, offset_x1)
    laces.append(h_lace1)

    if z + 450 <= column_height:
        h_lace2 = create_horizontal_lace(z + 450, offset_x1)
        laces.append(h_lace2)

    z += 450
    offset_flip = not offset_flip

# === STEP Export Section ===
script_dir = os.path.dirname(os.path.abspath(__file__))
cad_folder = os.path.join(script_dir, "cad")
output_file = os.path.join(cad_folder, "output_column.step")
os.makedirs(cad_folder, exist_ok=True)

step_writer = STEPControl_Writer()
step_writer.Transfer(i1, STEPControl_AsIs)
step_writer.Transfer(i2, STEPControl_AsIs)
step_writer.Transfer(top_plate, STEPControl_AsIs)
step_writer.Transfer(bottom_plate, STEPControl_AsIs)

for lace in laces:
    step_writer.Transfer(lace, STEPControl_AsIs)

status = step_writer.Write(output_file)
if status == IFSelect_RetDone:
    print(f"✅ STEP file exported successfully to: {output_file}")
else:
    print("❌ STEP export failed.")

# === Visualization ===
display.DisplayShape(i1, update=True)
display.DisplayShape(i2)
display.DisplayShape(top_plate)
display.DisplayShape(bottom_plate)

for lace in laces:
    display.DisplayShape(lace)

start_display()
