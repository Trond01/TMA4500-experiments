from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import trimesh

# Load the simplified mesh
mesh = trimesh.load("output_simplified_mesh.obj")

# Extract vertices and faces
vertices = mesh.vertices
faces = mesh.faces

# Plot the mesh using Matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Extract x, y, z coordinates
x = vertices[:, 0]
y = vertices[:, 1]
z = vertices[:, 2]

# Plot using faces for triangulation
ax.plot_trisurf(x, y, z, triangles=faces, color="lightblue", alpha=0.7, edgecolor="grey")

# Customize the plot
ax.set_title("Mesh Visualization")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()
