from ase.io import read, write

# --------------------------------------------------
# Read relaxed supercell
# --------------------------------------------------

atoms = read("LiMnO2_super_relaxed.cif")

print("Initial atoms :", len(atoms))

# --------------------------------------------------
# Remove first Li atom
# --------------------------------------------------

for i, atom in enumerate(atoms):
    if atom.symbol == "Li":
        print(f"Removing Li atom index {i}")
        del atoms[i]
        break

print("Atoms after removal :", len(atoms))

# --------------------------------------------------
# Save vacancy structure
# --------------------------------------------------

write("Li11Mn12O24.cif", atoms)

# --------------------------------------------------
# QE parameters
# --------------------------------------------------

input_data = {

    'control': {
        'calculation': 'relax',
        'prefix': 'limno2_li_vac',
        'pseudo_dir': './pseudo/',
        'outdir': './tmp/',
        'tstress': True,
        'tprnfor': True
    },

    'system': {
        'ibrav': 0,
        'nat': len(atoms),
        'ntyp': 3,

        'ecutwfc': 60,
        'ecutrho': 480,

        'occupations': 'smearing',
        'smearing': 'mv',
        'degauss': 0.02,

        'nspin': 2,

        'starting_magnetization(1)': 0.0,
        'starting_magnetization(2)': 0.5,
        'starting_magnetization(3)': 0.0
    },

    'electrons': {
        'conv_thr': 1.0e-8,
        'electron_maxstep': 300,
        'mixing_beta': 0.30
    },

    'ions': {
        'ion_dynamics': 'bfgs'
    }

}

# --------------------------------------------------
# Pseudopotentials
# --------------------------------------------------

pseudopotentials = {

    'Li': 'li_pbe_v1.4.uspp.F.UPF',
    'Mn': 'mn_pbe_v1.5.uspp.F.UPF',
    'O':  'O.pbe-n-kjpaw_psl.0.1.UPF'

}

# --------------------------------------------------
# Write QE input
# --------------------------------------------------

write(
    "limno2_li_vac_relax.in",
    atoms,
    format="espresso-in",
    input_data=input_data,
    pseudopotentials=pseudopotentials,
    kpts=(3, 3, 3)
)

# --------------------------------------------------
# Append Hubbard U
# --------------------------------------------------

with open("limno2_li_vac_relax.in", "a") as f:
    f.write("\n")
    f.write("HUBBARD (ortho-atomic)\n")
    f.write("U Mn-3d 3.9\n")

print("\nDone.")
print("Created:")
print("  Li11Mn12O24.cif")
print("  limno2_li_vac_relax.in")
