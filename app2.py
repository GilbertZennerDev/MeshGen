import pyvista as pv
import numpy as np

# Define the torus knot parameters
radius = 2
n1 = 3
n2 = 7

# Define the 3D function for the torus knot
def torus_knot(u, v):
    x = (radius + np.cos(n1 * u) * 0.5) * np.cos(n2 * v)
    y = (radius + np.cos(n1 * u) * 0.5) * np.sin(n2 * v)
    z = np.sin(n1 * u) * 0.5
    return x, y, z

# Create a mesh from the 3D function using PyVista
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, 2 * np.pi, 100)
x, y, z = torus_knot(*np.meshgrid(u, v, indexing='ij'))
points = np.column_stack((x.ravel(), y.ravel(), z.ravel()))
mesh = pv.PolyData(points)
mesh.triangulate()
mesh = mesh.extract_surface()

# Visualize the torus knot mesh
pv.plot(mesh, color='b', smooth_shading=True)
