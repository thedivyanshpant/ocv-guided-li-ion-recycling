#!/usr/bin/env python3

from ase.io import read, write
import numpy as np

# =====================================================
# Input files
# =====================================================

SLAB_FILE = "LiCoO2cell_relaxed.cif"
PVDF_FILE = "../PVDF_relax/pvdf_relax.out"
OUTPUT_FILE = "LiCoO2_PVDF.cif"

# Desired adsorption gap (Å)
gap = 2.7

# =====================================================
# Read structures
# =====================================================

slab = read(SLAB_FILE)
pvdf = read(
    PVDF_FILE,
    format="espresso-out",
    index=-1,
)

# =====================================================
# Find top of slab
# =====================================================

top_slab = max(atom.position[2] for atom in slab)

# =====================================================
# Find bottom of PVDF
# =====================================================

bottom_pvdf = min(atom.position[2] for atom in pvdf)

# =====================================================
# Center PVDF in x-y
# =====================================================

cell = slab.cell

cell_center = np.array([
    cell[0, 0] / 2.0,
    cell[1, 1] / 2.0
])

pvdf_center = np.mean(pvdf.get_positions(), axis=0)

dx = cell_center[0] - pvdf_center[0]
dy = cell_center[1] - pvdf_center[1]

# =====================================================
# Raise PVDF above slab
# =====================================================

dz = (top_slab + gap) - bottom_pvdf

pvdf.translate((dx, dy, dz))

# =====================================================
# Combine structures
# =====================================================

combined = slab.copy()
combined.extend(pvdf)

combined.set_cell(slab.cell)
combined.set_pbc(True)

# =====================================================
# Save combined structure
# =====================================================

write(OUTPUT_FILE, combined)

# =====================================================
# Verify final gap
# =====================================================

slab_z = [
    atom.position[2]
    for atom in combined[:len(slab)]
]

pvdf_z = [
    atom.position[2]
    for atom in combined[len(slab):]
]

top_surface = max(slab_z)
bottom_surface = min(pvdf_z)

actual_gap = bottom_surface - top_surface

# =====================================================
# Print summary
# =====================================================

print("\n========================================")
print("Interface successfully created")
print("========================================")
print(f"Slab file      : {SLAB_FILE}")
print(f"PVDF file      : {PVDF_FILE}")
print(f"Output file    : {OUTPUT_FILE}")
print("----------------------------------------")
print(f"Top of slab    : {top_surface:10.4f} Å")
print(f"Bottom of PVDF : {bottom_surface:10.4f} Å")
print(f"Requested gap  : {gap:10.4f} Å")
print(f"Actual gap     : {actual_gap:10.4f} Å")
print("----------------------------------------")
print(f"Total atoms    : {len(combined)}")
print("========================================")
