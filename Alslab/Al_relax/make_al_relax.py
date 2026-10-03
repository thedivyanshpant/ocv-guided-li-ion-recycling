from ase.io import read, write
from ase.constraints import FixAtoms

# --------------------------------------------------
# Read the Al slab
# --------------------------------------------------
atoms = read("Al111_4x4.cif")

# --------------------------------------------------
# Fix the bottom two layers
# --------------------------------------------------
z = atoms.positions[:,2]

levels = sorted(set(round(i,3) for i in z))

# bottom two layers
fixed_levels = levels[:2]

mask = []

for atom in atoms:
    if round(atom.position[2],3) in fixed_levels:
        mask.append(True)
    else:
        mask.append(False)

atoms.set_constraint(FixAtoms(mask=mask))

print("Atoms =", len(atoms))
print("Fixed atoms =", sum(mask))

# --------------------------------------------------
# QE parameters
# --------------------------------------------------

input_data = {

'control':{
    'calculation':'relax',
    'prefix':'al111',
    'pseudo_dir':'./pseudo/',
    'outdir':'./tmp/',
    'tstress':True,
    'tprnfor':True,
    'verbosity':'high'
},

'system':{
    'ibrav':0,
    'nat':len(atoms),
    'ntyp':1,
    'ecutwfc':60,
    'ecutrho':480,

    'occupations':'smearing',
    'smearing':'mv',
    'degauss':0.02
},

'electrons':{
    'conv_thr':1e-8,
    'mixing_beta':0.30
},

'ions':{
    'ion_dynamics':'bfgs'
}

}

# --------------------------------------------------
# Pseudopotential
# --------------------------------------------------

pseudopotentials = {

'Al':'Al.pbe-n-kjpaw_psl.1.0.0.UPF'

}

# --------------------------------------------------
# Write QE input
# --------------------------------------------------

write(
    "al111_relax.in",
    atoms,
    format="espresso-in",

    input_data=input_data,

    pseudopotentials=pseudopotentials,

    kpts=(4,4,1)
)

print("Finished.")
print("Created al111_relax.in")
