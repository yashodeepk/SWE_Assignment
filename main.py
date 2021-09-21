import trimesh
from time import sleep
from savePlot import saveSection

myMesh = trimesh.load_mesh('assignment.stl')
height = int(input('please input height - '))
basePlane = int(input('please input base plane -\n1. front\n2. bottom\n3. left'))

# hard coded base plane (bottom)

saveSection(basePlane, height, myMesh)
sleep(1)

print('saving sections with height 10mm, 30mm and 50mm')
saveSection(1, 10, myMesh)
sleep(1)
saveSection(1, 30, myMesh)
sleep(1)
saveSection(1, 50, myMesh)
sleep(1)