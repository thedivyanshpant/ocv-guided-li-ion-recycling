#!/usr/bin/env python3

from ase.io import read, write

# --------------------------------------------------
# Read combined structure
# --------------------------------------------------

atoms = read("Al2O3_PVDF.xyz")

print(f"Total atoms = {len(atoms)}")

# --------------------------------------------------
# QE input
# --------------------------------------------------

input_data = {

'control':{
    'calculation':'relax',
    'prefix':'al2o3_pvdf',
    'pseudo_dir':'./',
    'outdir':'./tmp/',
    'tstress':True,
    'tprnfor':True,
    'disk_io':'low'
},

'system':{
    'ibrav':0,
    'nat':len(atoms),
    'ntyp':4,

    'ecutwfc':60,
    'ecutrho':480,

    'occupations':'fixed',

    'nosym':True,
    'noinv':True,

    'nspin':1
},

'electrons':{
    'conv_thr':1.0e-8,
    'mixing_beta':0.30,
    'electron_maxstep':500
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
'O':'O.pbe-n-kjpaw_psl.0.1.UPF',
'C':'C.pbe-n-kjpaw_psl.1.0.0.UPF',
'H':'H.pbe-kjpaw_psl.1.0.0.UPF',
'F':'F.pbe-n-kjpaw_psl.1.0.0.UPF'

}

# --------------------------------------------------
# Write QE input
# --------------------------------------------------

write(
    "al2o3_pvdf_relax.in",
    atoms,
    format="espresso-in",
    input_data=input_data,
    pseudopotentials=pseudos,
    kpts=(4,4,1)
)

print("Created al2o3_pvdf_relax.in")
