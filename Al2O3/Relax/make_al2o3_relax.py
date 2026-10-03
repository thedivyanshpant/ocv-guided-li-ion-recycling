from ase.io import read, write

# --------------------------------------------------
# Read Al2O3 slab
# --------------------------------------------------

atoms = read("Al2O3_0001_2x2.xyz")

print("Atoms =", len(atoms))

# --------------------------------------------------
# QE input
# --------------------------------------------------

input_data = {

'control':{
    'calculation':'relax',
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

    'occupations':'smearing',
    'smearing':'mv',
    'degauss':0.02,

    'nspin':1
},

'electrons':{
    'conv_thr':1.0e-8,
    'mixing_beta':0.30,
    'electron_maxstep':400
},

'ions':{
    'ion_dynamics':'bfgs'
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
    "al2o3_relax.in",
    atoms,
    format="espresso-in",

    input_data=input_data,

    pseudopotentials=pseudos,

    kpts=(4,4,1)
)

print("Created al2o3_relax.in")