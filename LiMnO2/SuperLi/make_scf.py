from ase.io import read, write

# --------------------------------------------------
# Read FINAL relaxed structure from QE output
# --------------------------------------------------

atoms = read("limno2_super_li_relax.out")

# --------------------------------------------------
# QE input
# --------------------------------------------------

input_data = {

'control':{
    'calculation':'scf',
    'restart_mode':'restart',
    'prefix':'limno2_li11',
    'pseudo_dir':'./pseudo/',
    'outdir':'./tmp/',
    'tstress':True,
    'tprnfor':True,
},

'system':{
    'ibrav':0,
    'nat':len(atoms),
    'ntyp':3,

    'ecutwfc':60,
    'ecutrho':480,

    'occupations':'smearing',
    'smearing':'mv',
    'degauss':0.02,

    'nspin':2,
    'starting_magnetization(1)':0.0,
    'starting_magnetization(2)':0.5,
    'starting_magnetization(3)':0.0
},

'electrons':{
    'conv_thr':1.0e-10,
    'mixing_beta':0.30,
    'electron_maxstep':500
}

}

# --------------------------------------------------
# Pseudopotentials
# --------------------------------------------------

pseudos = {
'Li':'li_pbe_v1.4.uspp.F.UPF',
'Mn':'mn_pbe_v1.5.uspp.F.UPF',
'O':'O.pbe-n-kjpaw_psl.0.1.UPF'
}

# --------------------------------------------------
# Write QE input
# --------------------------------------------------

write(
    "limno2_li11_scf.in",
    atoms,
    format="espresso-in",
    input_data=input_data,
    pseudopotentials=pseudos,
    kpts=(3,3,3)
)

# --------------------------------------------------
# Append Hubbard U
# --------------------------------------------------

with open("limno2_li11_scf.in", "a") as f:
    f.write("\n")
    f.write("HUBBARD (ortho-atomic)\n")
    f.write("U Mn-3d 3.9\n")

print("Created limno2_li11_scf.in")
