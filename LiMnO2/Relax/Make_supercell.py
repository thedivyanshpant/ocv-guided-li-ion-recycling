from ase.io import read, write

atoms = read("limno2_vc_relax.out")

supercell = atoms.repeat((2, 2, 1))

write("LiMnO2_supercell.cif", supercell)

print(supercell)

print("done")
