from ase.io import read, write

# --------------------------------------------------
# Read relaxed adsorption structure
# --------------------------------------------------

atoms = read("limno2_super_relax.out")

print(f"Number of atoms = {len(atoms)}")

input_data = {

    'control': {
        'calculation': 'scf',
        'prefix': 'limno2_super',
        'pseudo_dir': './pseudo/',
        'outdir': './tmp/',
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
        'conv_thr': 1.0e-10,
        'electron_maxstep': 300,
        'mixing_beta': 0.15,
        'mixing_mode': 'local-TF'
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
# Write QE SCF input
# --------------------------------------------------

write(
    "limno2_super_scf.in",
    atoms,
    format="espresso-in",
    input_data=input_data,
    pseudopotentials=pseudopotentials,
    kpts=(3, 3, 3)
)

# --------------------------------------------------
# Append Hubbard U (QE 7.5)
# --------------------------------------------------

with open("limno2_super_scf.in", "a") as f:
    f.write("\n")
    f.write("HUBBARD (ortho-atomic)\n")
    f.write("U Mn-3d 3.9\n")

print("\nFinished.")
print("Created: limno2_super_scf.in")
