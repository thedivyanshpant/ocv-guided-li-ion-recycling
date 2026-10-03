#!/usr/bin/env python3

from ase.io import read, write

# -------------------------------------------------
# Read relaxed structures directly from QE outputs
# -------------------------------------------------

slab = read("al2o3_relax.out")
pvdf = read("pvdf_relax.out")

# Save for visualization (optional)

write("Al2O3_relaxed.xyz", slab)
write("PVDF_relaxed.xyz", pvdf)

# -------------------------------------------------
# Place PVDF above Al2O3 slab
# -------------------------------------------------

top_surface = max(atom.position[2] for atom in slab)
bottom_pvdf = min(atom.position[2] for atom in pvdf)

gap = 2.5      # Initial adsorption distance (Å)

# Center PVDF over the slab
cell = slab.cell

# Works for your hexagonal cell
x_center = (cell[0][0] + cell[1][0]) / 3.0
y_center = cell[1][1] / 2.0

# Move PVDF to origin
com = pvdf.get_center_of_mass()

pvdf.translate((-com[0], -com[1], -bottom_pvdf))

# Move above surface
pvdf.translate((x_center, y_center, top_surface + gap))

# -------------------------------------------------
# Combine slab + PVDF
# -------------------------------------------------

combined = slab + pvdf

write("Al2O3_PVDF.xyz", combined)

print("Created:")
print("  Al2O3_relaxed.xyz")
print("  PVDF_relaxed.xyz")
print("  Al2O3_PVDF.xyz")
print("Total atoms =", len(combined))
