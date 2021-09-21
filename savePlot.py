from datetime import datetime
import matplotlib.pyplot as plt

def saveSection(basePlane, height, mesh):
    rightNow = datetime.now()

    myMesh = mesh
    if (basePlane == 1):
        height = height + 25
        planeNormal = [0, 0, 1]

    if (basePlane == 2):
        planeNormal = [0, 1, 0]

    if (basePlane == 3):
        planeNormal = [1, 0, 0]

    planeOrigin = [0, 0, 0]
    for i in range(len(planeNormal)):
        planeOrigin[i] = planeNormal[i]*height

    try:
        slicedMesh = myMesh.section(plane_origin=planeOrigin, plane_normal=planeNormal)
        sliced2D, to_3d = slicedMesh.to_planar()
        plt.axes().set_aspect('equal', 'datalim')
        eformat = {'Line0': {'color': 'g', 'linewidth': 1},
           'Line1': {'color': 'y', 'linewidth': 1},
           'Arc0': {'color': 'r', 'linewidth': 1},
           'Arc1': {'color': 'b', 'linewidth': 1},
           'Bezier0': {'color': 'k', 'linewidth': 1},
           'Bezier1': {'color': 'k', 'linewidth': 1},
           'BSpline0': {'color': 'm', 'linewidth': 1},
           'BSpline1': {'color': 'm', 'linewidth': 1}
        }
        for entity in sliced2D.entities:
            if hasattr(entity, 'plot'):
                entity.plot(sliced2D.vertices)
                continue
            discrete = entity.discrete(sliced2D.vertices)
            eKey = entity.__class__.__name__ + str(int(entity.closed))

            fmt = eformat[eKey].copy()
            if hasattr(entity, 'color'):
                fmt['color'] = entity.color
            plt.plot(*discrete.T, **fmt)
            fileName = datetime.now().strftime('section%d%b%Y%H%M%S') + '.png'
        plt.savefig(fileName)
        
        print('section saved with file name ', fileName)

    except AttributeError:
        print('geometry does not exist in the slicing plane')