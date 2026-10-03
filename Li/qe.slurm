#!/bin/bash
#SBATCH --job-name=Li_scf
#SBATCH --partition=standard
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=48
#SBATCH --cpus-per-task=1
#SBATCH --time=72:00:00
#SBATCH --output=%x.%j.out
#SBATCH --error=%x.%j.err

cd $SLURM_SUBMIT_DIR

# Load Quantum ESPRESSO environment
source ~/qe_env.sh

echo "========================================="
echo "Job ID      : $SLURM_JOB_ID"
echo "Nodes       : $SLURM_JOB_NODELIST"
echo "Tasks       : $SLURM_NTASKS"
echo "Working Dir : $SLURM_SUBMIT_DIR"
echo "Start Time  : $(date)"
echo "========================================="

module list
which pw.x

# MPI/OpenMP settings
export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1
export OPENBLAS_NUM_THREADS=1

# Ensure QE scratch directory exists
mkdir -p /scratch/deepanthpcu/ml/tmp/Lislab

# Run Quantum ESPRESSO SCF
mpiexec.hydra -n $SLURM_NTASKS pw.x -in Lislab_scf.in > Lislab_scf.out

echo "========================================="
echo "Finished : $(date)"
echo "========================================="
