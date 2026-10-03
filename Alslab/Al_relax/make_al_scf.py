from ase.io import read, write

atoms = read("al111_relax.out")

input_data = {

'control':{
    'calculation':'scf',
    'prefix':'al111_4x4',
    'restart_mode':'restart',
    'pseudo_dir':'./',
    'outdir':'./tmp/',
    'tstress':True,
    'tprnfor':True
},

'system':{
    'ibrav':0,
    'nat':len(atoms),
    'ntyp':1,

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
}

}

pseudos = {
'Al':'Al.pbe-n-kjpaw_psl.1.0.0.UPF'
}

write(
    "al111_scf.in",
    atoms,
    format="espresso-in",
    input_data=input_data,
    pseudopotentials=pseudos,
    kpts=(4,4,1)
)

print("Created al111_scf.in")
