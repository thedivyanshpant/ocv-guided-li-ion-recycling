#!/usr/bin/env python3

from ase.io import read, write
import numpy as np

# =====================================================
# Read relaxed QE outputs
# =====================================================

lif = read("LiFcell_relax.out")
pvdf = read("pvdf_relax.out")

# =====================================================
# Save relaxed structures
# =====================================================

write("LiF_relaxed.cif", lif)
write("PVDF_relaxed.cif", pvdf)

# =====================================================
# Find top of LiF slab
# =====================================================

top_lif = max(atom.position[2] for atom in lif)

# =====================================================
# Find bottom of PVDF
# =====================================================

bottom_pvdf = min(atom.position[2] for atom in pvdf)

# =====================================================
# Desired adsorption distance
# =====================================================

gap = 2.7

# =====================================================
# Center PVDF in x and y
# =====================================================

cell = lif.cell

# Center of simulation cell
cell_center_x = cell[0, 0] / 2.0
cell_center_y = cell[1, 1] / 2.0

# Geometric center of PVDF
pvdf_center = np.mean(pvdf.get_positions(), axis=0)

dx = cell_center_x - pvdf_center[0]
dy = cell_center_y - pvdf_center[1]

# =====================================================
# Lift PVDF above slab
# =====================================================

dz = (top_lif + gap) - bottom_pvdf

# Translate molecule
pvdf.translate((dx, dy, dz))

# =====================================================
# Combine structures
# =====================================================

combined = lif.copy()
combined.extend(pvdf)

combined.set_cell(lif.cell)
combined.set_pbc(True)

# =====================================================
# Write interface
# =====================================================

write("LiF_PVDF.cif", combined)

# =====================================================
# Verify final gap
# =====================================================

slab_z = []
pvdf_z = []

for atom in combined:
    if atom.symbol in ["Li", "F"] and atom.index < len(lif):
        slab_z.append(atom.position[2])
    else:
        pvdf_z.append(atom.position[2])

top_surface = max(slab_z)
bottom_surface = min(pvdf_z)
final_gap = bottom_surface - top_surface

# =====================================================
# Print information
# =====================================================

print("======================================")
print("LiF top surface     :", top_surface)
print("PVDF bottom atom    :", bottom_surface)
print("Requested gap       :", gap)
print("Actual gap          :", final_gap)
print("======================================")
print("Created:")
print("  LiF_relaxed.cif")
print("  PVDF_relaxed.cif")
print("  LiF_PVDF.cif")
print("======================================")
