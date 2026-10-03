from ase.io import read

atoms = read("Cu_PVDF.xyz")

cu_z = []
pvdf_z = []

for atom in atoms:
    if atom.symbol == "Cu":
        cu_z.append(atom.position[2])
    else:
        pvdf_z.append(atom.position[2])

top_cu = max(cu_z)
bottom_pvdf = min(pvdf_z)

print("Top Cu layer z =", top_cu)
print("Bottom PVDF atom z =", bottom_pvdf)
print("Gap =", bottom_pvdf - top_cu, "Angstrom")