#! /usr/bin/env python3


job_name = 'najah_test'
queue = 'tiny16core'
prefix = job_name 
num_nodes = 1 
num_proc = 32
walltime = 6


print('#SBATCH -J %s'%job_name)
print('#SBATCH --partition %s'% queue)
print('#SBATCH -o %s_%%j.txt'% prefix)
print('#SBATCH -e %s_%%j.err'% prefix)
print('#SBATCH --mail-type=ALL')
print('#SBATCH --mail-user=nabiggs@uark.edu')  
print('#SBATCH --nodes=%d'% num_nodes)
print('#SBATCH --ntasks-per-node=%d'% num_proc)
print('#SBATCH --time=%.2d:00:00'% walltime)

print()
print('export OMP_NUM_THREADS=%d' % num_proc)
print()

modules = ['samtools','jellyfish','bowtie2', 'salmon/0.8.2','java']
print('# load required modules')
for m in modules: 
    print('module load %s' % m)
print()

 
print('# cd into the directory where you\'re submitting this script from')
print('cd $SLURM_SUBMIT_DIR')
print()
print('# copy files from storage to scratch')
print('rsync -av RNA-R*.fastq.gz /scratch/$SLURM_JOB_ID')

print('# cd onto the scratch disk to run the job')
print('cd /scratch/$SLURM_JOB_ID/')
print()
print('# run the Trinity assembly')
print('/share/apps/bioinformatics/trinity/trinityrnaseq-v2.11.0/Trinity --seqType fq --left RNA-R1.fastq.gz --right RNA-R2.fastq.gz --CPU 48 --max_memory 250G --trimmomatic --no_normalize_reads --full_cleanup --output trinity_Run2')
print()
print('# copy output files back to storage')
print('rsync -av trinity_Run2 $SLURM_SUBMIT_DIR')
