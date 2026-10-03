from ase.io import read
from ase.io.espresso import write_espresso_in

# Read the CIF
atoms = read("Li.cif")

# Pseudopotential
pseudopotentials = {
    "Li": "li_pbe_v1.4.uspp.F.UPF"
}

# QE input parameters
input_data = {
    "control": {
        "calculation": "relax",
        "prefix": "li_bulk",
        "outdir": "./tmp/",
        "pseudo_dir": "./pseudo/",
        "tstress": True,
        "tprnfor": True,
    },
    "system": {
        "ecutwfc": 60,
        "ecutrho": 480,
        "occupations": "smearing",
        "smearing": "mv",
        "degauss": 0.02,
    },
    "electrons": {
        "conv_thr": 1.0e-8,
        "mixing_beta": 0.30,
    },
    "ions": {
        "ion_dynamics": "bfgs",
    },
}

# Write QE input
with open("li_bulk_relax.in", "w") as fd:
    write_espresso_in(
        fd,
        atoms,
        input_data=input_data,
        pseudopotentials=pseudopotentials,
        kpts=(16, 16, 16),
    )

print("Created li_bulk_relax.in")
