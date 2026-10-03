from ase.build import fcc111

slab = fcc111(
    'Al',
    size=(4,4,5),
    vacuum=15.0
)

print("Number of atoms =", len(slab))

slab.write("Al111_4x4.cif")
