from ase.io import read

atoms = read("LiF_PVDF.cif")

slab_z = []
pvdf_z = []

for atom in atoms:
    if atom.symbol in ["Li", "F"]:
        slab_z.append(atom.position[2])
    else:
        pvdf_z.append(atom.position[2])

top_surface = max(slab_z)
bottom_pvdf = min(pvdf_z)
# Current positions
top_lif = max(atom.position[2] for atom in lif)
bottom_pvdf = min(atom.position[2] for atom in pvdf)

gap = 2.7

# Required z shift
dz = (top_LiF + gap) - bottom_pvdf

# Center in x-y
slab_center = LiF.get_positions().mean(axis=0)
pvdf_center = pvdf.get_positions().mean(axis=0)

dx = slab_center[0] - pvdf_center[0]
dy = slab_center[1] - pvdf_center[1]

pvdf.translate((dx, dy, dz))
print("Top slab atom z =", top_surface)
print("Bottom PVDF atom z =", bottom_pvdf)
print("Gap =", bottom_pvdf - top_surface, "Angstrom")
