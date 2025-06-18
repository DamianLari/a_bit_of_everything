from vedo import Mesh, show

def afficher_stl_rapidement(fichier_stl):
    mesh = Mesh(fichier_stl)
    mesh.c("lightblue").lw(0.5).lighting("plastic")
    show(mesh, __doc__, axes=1, bg="white")

# 🔁 Remplacer par ton fichier STL
afficher_stl_rapidement("exemple.stl")
