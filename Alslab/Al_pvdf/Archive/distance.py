from ase.io import read

atoms = read("Al_PVDF.xyz")

al_z = []
pvdf_z = []

for atom in atoms:
    if atom.symbol == "Al":
        al_z.append(atom.position[2])
    else:
        pvdf_z.append(atom.position[2])

top_al = max(al_z)
bottom_pvdf = min(pvdf_z)

print("Top Al layer z =", top_al)
print("Bottom PVDF atom z =", bottom_pvdf)
print("Gap =", bottom_pvdf - top_al, "Angstrom")
