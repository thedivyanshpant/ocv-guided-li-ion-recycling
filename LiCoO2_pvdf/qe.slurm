#!/bin/bash
#SBATCH --job-name=LiCoO2_PVDF_scf
#SBATCH --partition=standard
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=48
#SBATCH --cpus-per-task=1
#SBATCH --time=48:00:00
#SBATCH --output=LiCoO2_PVDF_scf.log
#SBATCH --error=LiCoO2_PVDF_scf.err

########################################
# Load QE Environment
########################################
source ~/qe_env.sh

########################################
# Working Directory
########################################
cd ~/DFT/Battery/LiCoO2_pvdf

########################################
# OpenMP Settings
########################################
export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1
export MKL_DYNAMIC=FALSE
export OPENBLAS_NUM_THREADS=1

########################################
# Job Information
########################################
echo "======================================"
echo "Job ID      : $SLURM_JOB_ID"
echo "Nodes       : $SLURM_JOB_NUM_NODES"
echo "MPI Tasks   : $SLURM_NTASKS"
echo "Directory   : $(pwd)"
echo "Started at  : $(date)"
echo "======================================"

echo "Node list:"
scontrol show hostnames $SLURM_JOB_NODELIST

echo
echo "Loaded modules:"
module list

echo
echo "Quantum ESPRESSO:"
which pw.x

########################################
# Run Quantum ESPRESSO
########################################
mpiexec.hydra -n $SLURM_NTASKS pw.x -in LiCoO2_PVDF_scf.in > LiCoO2_PVDF_scf.out

########################################
# Job Finished
########################################
echo "======================================"
echo "Finished at $(date)"
echo "======================================"
