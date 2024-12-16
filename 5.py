import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

def plot_polyhedron(vertices, faces, ax, color, edge_color, offset=[0, 0, 0]):
    vertices = vertices + offset
    poly3d = [[vertices[vert_id] for vert_id in face] for face in faces]
    ax.add_collection3d(Poly3DCollection(poly3d, facecolors=color, linewidths=1, edgecolors=edge_color, alpha=.5))

def hexahedron():
    vertices = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
                         [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]])
    faces = [[0, 1, 2, 3], [4, 5, 6, 7], [0, 1, 5, 4], [2, 3, 7, 6], [1, 2, 6, 5], [4, 7, 3, 0]]
    return vertices, faces

def octahedron():
    vertices = np.array([[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]])
    faces = [[0, 2, 4], [0, 2, 5], [0, 3, 4], [0, 3, 5], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5]]
    return vertices, faces

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')

vertices, faces = hexahedron()
plot_polyhedron(vertices, faces, ax, color='orange', edge_color='blue', offset=[-2, 0, 0])

vertices, faces = octahedron()
plot_polyhedron(vertices, faces, ax, color='yellow', edge_color='purple', offset=[2, 0, 0])

ax.set_xlabel('X', fontsize=12, fontweight='bold')
ax.set_ylabel('Y', fontsize=12, fontweight='bold')
ax.set_zlabel('Z', fontsize=12, fontweight='bold')
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])
ax.set_aspect('equal')
ax.set_facecolor('white')

ax.grid(True, color='gray', linestyle='--', linewidth=0.5)

plt.title("3D Polyhedrons", fontsize=15, fontweight='bold', color='white', pad=20)
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

plt.show()
