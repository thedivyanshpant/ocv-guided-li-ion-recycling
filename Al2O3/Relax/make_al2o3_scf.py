from ase.io import read, write

# --------------------------------------------------
# Read relaxed structure from QE output
# --------------------------------------------------

atoms = read("al2o3_relax.out")

print(f"Number of atoms = {len(atoms)}")

# --------------------------------------------------
# Quantum ESPRESSO input parameters
# --------------------------------------------------

input_data = {

'control':{
    'calculation':'scf',
    'restart_mode':'restart',
    'prefix':'al2o3',
    'pseudo_dir':'./',
    'outdir':'./tmp/',
    'tstress':True,
    'tprnfor':True,
    'disk_io':'low'
},

'system':{
    'ibrav':0,
    'nat':len(atoms),
    'ntyp':2,

    'ecutwfc':60,
    'ecutrho':480,

    'occupations':'fixed',

    'nspin':1
},

'electrons':{
    'conv_thr':1.0e-8,
    'mixing_beta':0.30,
    'electron_maxstep':400
}

}

# --------------------------------------------------
# Pseudopotentials
# --------------------------------------------------

pseudos = {

'Al':'Al.pbe-n-kjpaw_psl.1.0.0.UPF',
'O':'O.pbe-n-kjpaw_psl.0.1.UPF'

}

# --------------------------------------------------
# Write QE input
# --------------------------------------------------

write(
    "al2o3_scf.in",
    atoms,
    format="espresso-in",
    input_data=input_data,
    pseudopotentials=pseudos,
    kpts=(6,6,1)
)

print("Created al2o3_scf.in")
