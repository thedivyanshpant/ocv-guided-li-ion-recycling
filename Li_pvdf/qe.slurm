#!/bin/bash
#SBATCH --job-name=Li_PVDF_SCF
#SBATCH --partition=standard
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=48
#SBATCH --cpus-per-task=1
#SBATCH --time=96:00:00
#SBATCH --output=%x.%j.out
#SBATCH --error=%x.%j.err

cd "$SLURM_SUBMIT_DIR"

# Load QE environment
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

export OMP_NUM_THREADS=1

mkdir -p ./tmp/Li_PVDF

mpiexec.hydra -n "$SLURM_NTASKS" pw.x \
    -in Li_PVDF_scf.in > Li_PVDF_scf.out

echo "========================================="
echo "Finished : $(date)"
echo "========================================="
