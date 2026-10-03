from ase.io import read, write

atoms = read("Al_PVDF.xyz")

input_data = {

'control':{
    'calculation':'relax',
    'prefix':'al_pvdf',
    'pseudo_dir':'./',
    'outdir':'./tmp/',
    'tstress':True,
    'tprnfor':True
},

'system':{
    'ibrav':0,
    'nat':len(atoms),
    'ntyp':4,

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
    'electron_maxstep':500
},

'ions':{
    'ion_dynamics':'bfgs'
}

}

pseudos = {
'Al':'Al.pbe-n-kjpaw_psl.1.0.0.UPF',
'C':'C.pbe-n-kjpaw_psl.1.0.0.UPF',
'H':'H.pbe-kjpaw_psl.1.0.0.UPF',
'F':'F.pbe-n-kjpaw_psl.1.0.0.UPF'
}

write(
    "al_pvdf_relax.in",
    atoms,
    format="espresso-in",
    input_data=input_data,
    pseudopotentials=pseudos,
    kpts=(4,4,1)
)

print("Created al_pvdf_relax.in")
