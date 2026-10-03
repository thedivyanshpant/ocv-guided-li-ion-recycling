from ase.io import read

atoms = read("Al2O3_PVDF.xyz")

slab_z = []
pvdf_z = []

for atom in atoms:
    if atom.symbol in ["Al", "O"]:
        slab_z.append(atom.position[2])
    else:
        pvdf_z.append(atom.position[2])

top_surface = max(slab_z)
bottom_pvdf = min(pvdf_z)

print("Top slab atom z =", top_surface)
print("Bottom PVDF atom z =", bottom_pvdf)
print("Gap =", bottom_pvdf - top_surface, "Angstrom")
