from ase.io import read, write

cu = read("Cu111_4*4.xyz")
pvdf = read("pvdf_relaxed.xyz")

pvdf.translate((12,0,28))

combined = cu + pvdf

write("Cu_PVDF.xyz", combined)