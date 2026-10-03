from ase.io import read, write

# --------------------------------------------------
# Read CIF
# --------------------------------------------------

atoms = read("LiMnO2.cif")

print("Atoms =", len(atoms))
print("Chemical symbols =", atoms.get_chemical_symbols())

# --------------------------------------------------
# QE parameters
# --------------------------------------------------

input_data = {

    'control': {
        'calculation': 'vc-relax',
        'prefix': 'limno2',
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
        'starting_magnetization(2)': 0.5
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
    "limno2_vc_relax.in",
    atoms,
    format="espresso-in",
    input_data=input_data,
    pseudopotentials=pseudopotentials,
    kpts=(6, 6, 3)
)

print("\nFinished.")
print("Created: limno2_vc_relax.in")
