from pymatgen.core import Structure
from pymatgen.core.surface import SlabGenerator
from pymatgen.io.ase import AseAtomsAdaptor
from ase.io import write

print("Reading bulk structure...")
bulk = Structure.from_file("Al2O3.cif")

print("Generating slab...")

slabgen = SlabGenerator(
    initial_structure=bulk,
    miller_index=(0, 0, 1),
    min_slab_size=8.0,
    min_vacuum_size=15.0,
    center_slab=True,
    in_unit_planes=False
)

slabs = slabgen.get_slabs(symmetrize=False)

print("Number of slabs:", len(slabs))

slab = slabs[0]

atoms = AseAtomsAdaptor.get_atoms(slab)

print("Atoms:", len(atoms))

write("Al2O3_0001.cif", atoms)
write("Al2O3_0001.xyz", atoms)

print("Finished.")