from ase.io import read, write

# --------------------------------------------------
# Read Supercell CIF
# --------------------------------------------------

atoms = read("LiMnO2_supercell.cif")

print("Atoms =", len(atoms))
print("Chemical symbols =", atoms.get_chemical_symbols())

# --------------------------------------------------
# QE parameters
# --------------------------------------------------

input_data = {

    'control': {
        'calculation': 'vc-relax',
        'prefix': 'limno2_super',
        'pseudo_dir': './pseudo/',
        'outdir': './tmp/',
        'tstress': True,
        'tprnfor': True,
        'verbosity': 'high'
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
        'mixing_beta': 0.30,
        'electron_maxstep': 500
    },

    'ions': {
        'ion_dynamics': 'bfgs'
    },

    'cell': {
        'cell_dynamics': 'bfgs'
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
    "limno2_super_relax.in",
    atoms,
    format="espresso-in",
    input_data=input_data,
    pseudopotentials=pseudopotentials,
    kpts=(3, 3, 3)
)

# --------------------------------------------------
# Append Hubbard U (QE 7.5)
# --------------------------------------------------

with open("limno2_super_relax.in", "a") as f:
    f.write("\n")
    f.write("HUBBARD (ortho-atomic)\n")
    f.write("U Mn-3d 3.9\n")

print("\nFinished.")
print("Created: limno2_super_relax.in")
