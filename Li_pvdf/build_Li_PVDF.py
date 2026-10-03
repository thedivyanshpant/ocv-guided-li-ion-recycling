#!/usr/bin/env python3

from ase.io import read, write
import numpy as np

# =====================================================
# Read relaxed structures
# =====================================================

li = read("Lislab_relax.out", index=-1)

pvdf = read(
    "/home/blackbook/DFT/Battery/Done FOr battery/PVDF_relax/pvdf_relax.out",
    index=-1
)

# =====================================================
# Save extracted relaxed structures
# =====================================================

write("Li_relaxed.cif", li)
write("PVDF_relaxed.cif", pvdf)

# =====================================================
# Find top of Li slab
# =====================================================

top_li = max(atom.position[2] for atom in li)

# =====================================================
# Find bottom of PVDF
# =====================================================

bottom_pvdf = min(atom.position[2] for atom in pvdf)

# =====================================================
# Desired interface gap
# =====================================================

gap = 2.7

# =====================================================
# Center PVDF in x and y
# =====================================================

cell = li.cell

# Use center of the slab cell
cell_center_x = cell[0, 0] / 2.0
cell_center_y = cell[1, 1] / 2.0

pvdf_center = np.mean(pvdf.get_positions(), axis=0)

dx = cell_center_x - pvdf_center[0]
dy = cell_center_y - pvdf_center[1]

# =====================================================
# Lift PVDF above Li
# =====================================================

dz = (top_li + gap) - bottom_pvdf

pvdf.translate((dx, dy, dz))

# =====================================================
# Combine structures
# =====================================================

combined = li.copy()
combined.extend(pvdf)

combined.set_cell(li.cell)
combined.set_pbc(True)

# =====================================================
# Write interface
# =====================================================

write("Li_PVDF.cif", combined)

# =====================================================
# Verify gap
# =====================================================

li_z = [atom.position[2] for atom in li]
pvdf_z = [atom.position[2] for atom in pvdf]

top_surface = max(li_z)
bottom_surface = min(pvdf_z)

print("======================================")
print("Li top surface      :", top_surface)
print("PVDF bottom atom    :", bottom_surface)
print("Requested gap       :", gap)
print("Actual gap          :", bottom_surface - top_surface)
print("======================================")
print("Created:")
print("  Li_relaxed.cif")
print("  PVDF_relaxed.cif")
print("  Li_PVDF.cif")
print("======================================")
