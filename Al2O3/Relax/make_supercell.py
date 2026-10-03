from ase.io import read, write

# Read the slab
slab = read("Al2O3_0001.cif")

# Make a 2×2×1 supercell
slab = slab.repeat((2, 2, 1))

print("Number of atoms:", len(slab))
print("Cell:")
print(slab.cell)

# Save
write("Al2O3_0001_2x2.cif", slab)
write("Al2O3_0001_2x2.xyz", slab)

print("Finished.")