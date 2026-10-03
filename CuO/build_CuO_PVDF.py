#!/usr/bin/env python3

from ase.io import read, write
import numpy as np

# =====================================================
# Read relaxed structures
# =====================================================

cuo = read("cuo_slab_relax.out", index=-1)
pvdf = read("/home/blackbook/DFT/Battery/Done FOr battery/PVDF_relax/pvdf_relax.out", index=-1)

# =====================================================
# Save extracted relaxed structures
# =====================================================

write("CuO_relaxed.cif", cuo)
write("PVDF_relaxed.cif", pvdf)

# =====================================================
# Find top of CuO slab
# =====================================================

top_cuo = max(atom.position[2] for atom in cuo)

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

cell = cuo.cell

cell_center_x = cell[0, 0] / 2.0
cell_center_y = cell[1, 1] / 2.0

pvdf_center = np.mean(pvdf.get_positions(), axis=0)

dx = cell_center_x - pvdf_center[0]
dy = cell_center_y - pvdf_center[1]

# =====================================================
# Lift PVDF above CuO
# =====================================================

dz = (top_cuo + gap) - bottom_pvdf

pvdf.translate((dx, dy, dz))

# =====================================================
# Combine structures
# =====================================================

combined = cuo.copy()
combined.extend(pvdf)

combined.set_cell(cuo.cell)
combined.set_pbc(True)

# =====================================================
# Write interface
# =====================================================

write("CuO_PVDF.cif", combined)

# =====================================================
# Verify gap
# =====================================================

cuo_z = [atom.position[2] for atom in cuo]
pvdf_z = [atom.position[2] for atom in pvdf]

top_surface = max(cuo_z)
bottom_surface = min(pvdf_z)

print("======================================")
print("CuO top surface     :", top_surface)
print("PVDF bottom atom    :", bottom_surface)
print("Requested gap       :", gap)
print("Actual gap          :", bottom_surface - top_surface)
print("======================================")
print("Created:")
print("  CuO_relaxed.cif")
print("  PVDF_relaxed.cif")
print("  CuO_PVDF.cif")
print("======================================")
