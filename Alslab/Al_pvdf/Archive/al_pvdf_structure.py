#!/usr/bin/env python3

from ase.io import read, write

# -------------------------------------------------
# Read the relaxed structures directly from QE outputs
# -------------------------------------------------

al = read("al111_relax.out")
pvdf = read("pvdf_relax.out")

# Save them as XYZ (optional, useful for visualization)

write("Al111_relaxed.xyz", al)
write("PVDF_relaxed.xyz", pvdf)

# -------------------------------------------------
# Place PVDF above the Al slab
# -------------------------------------------------

top_al = max(atom.position[2] for atom in al)
bottom_pvdf = min(atom.position[2] for atom in pvdf)

gap = 2.5      # Initial adsorption distance (Å)

# Center PVDF over the slab
cell = al.cell

x_center = (cell[0][0] + cell[1][0]) / 3.0
y_center = cell[1][1] / 2.0

# Move PVDF to origin first
com = pvdf.get_center_of_mass()

pvdf.translate((-com[0], -com[1], -bottom_pvdf))

# Move into position
pvdf.translate((x_center, y_center, top_al + gap))

# -------------------------------------------------
# Combine systems
# -------------------------------------------------

combined = al + pvdf

write("Al_PVDF.xyz", combined)

print("Created:")
print("  Al111_relaxed.xyz")
print("  PVDF_relaxed.xyz")
print("  Al_PVDF.xyz")
