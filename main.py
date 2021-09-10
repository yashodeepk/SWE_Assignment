from numpy import float64
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot


# Input the slicing heights
z_heights = []

size = int(input('Enter the number of elements: '))

for i in range(size):
    temp = float64(input())
    z_heights.append(temp)

print(z_heights)

# Create a new plot
figure = pyplot.figure()
axes = mplot3d.Axes3D(figure,auto_add_to_figure=False)
figure.add_axes(axes)

# Load the STL files and add the vectors to the plot
your_mesh = mesh.Mesh.from_file('assignment.stl')
print(your_mesh)
axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

# Auto scale to the mesh size
scale = your_mesh.points.flatten()
axes.auto_scale_xyz(scale, scale, scale)

# Show the plot to the screen
pyplot.show()