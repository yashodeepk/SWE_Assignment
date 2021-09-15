import trimesh
import numpy as np
#axis
# Input the slicing heights
z_heights = []

size = int(input('Enter the number of elements: '))

for i in range(size):
    temp = np.float64(input())
    z_heights.append(temp)
    
mesh = trimesh.load_mesh("assignment.stl")
#mesh.visual.face_colors = [100, 100, 100, 255]
for z in range(size):
    slice = mesh.section(plane_origin=[0,z_heights[z],0], 
                        plane_normal=[0,1,0])
    slice.show()
