#!/bin/bash
#SBATCH --job-name=LiCoO2_relax
#SBATCH --partition=standard
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=48
#SBATCH --cpus-per-task=1
#SBATCH --time=72:00:00
#SBATCH --output=LiCoO2cell_relax.log
#SBATCH --error=LiCoO2cell_relax.err

########################################
# Load QE Environment
########################################
source ~/qe_env.sh

########################################
# Working Directory
########################################
cd ~/DFT/Battery/LiCoO2

########################################
# OpenMP Settings
########################################
export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1
export MKL_DYNAMIC=FALSE
export OPENBLAS_NUM_THREADS=1

########################################
# Intel MPI Settings
########################################
export I_MPI_FALLBACK=disable
export I_MPI_FABRICS=shm:dapl
export I_MPI_DEBUG=5

########################################
# Job Information
########################################
echo "======================================"
echo "Job ID      : $SLURM_JOB_ID"
echo "Nodes       : $SLURM_JOB_NUM_NODES"
echo "MPI Tasks   : $SLURM_NTASKS"
echo "Directory   : $(pwd)"
echo "======================================"

which pw.x

########################################
# Run Quantum ESPRESSO
########################################
mpiexec.hydra -n $SLURM_NTASKS pw.x -in LiCoO2cell_relax.in > LiCoO2cell_relax.out

echo "======================================"
echo "Finished at $(date)"
echo "======================================"
