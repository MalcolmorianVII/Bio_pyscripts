set -e

# Checking for contamination
kraken2 --gzip-compressed --use-names --output 50-FR10242126_kraken2_gtdb_output --db /home/ubuntu/belson/database/krak_db --report 50-FR10242126_CTGGAGAATA-GTTGTATGGA_L002_R1_001_kraken2_gtdb_report --threads 4 --confidence 1 --memory-mapping --paired ../50-FR10242126_CTGGAGAATA-GTTGTATGGA_L002_R1_001.fastq.gz ../50-FR10242126_CTGGAGAATA-GTTGTATGGA_L002_R2_001.fastq.gz

# Denovo assembly
shovill --outdir sho_out --R1 .fastq.gz --R2 .fastq.gz --cpus 4 --ram 16

# mlst 
mlst --scheme senterica --nopath /path/to/assembly/output.fa > results.txt

# dockerized phenix
# prep ref
sudo docker run -v /home/ubuntu/data/belson/projects/benk_genomes/fastqs/2020.08.25/:/data -it --rm mbull/bioinformatics-containers:phenix phenix.py  prepare_reference --mapper bwa  --variant gatk --reference data/LS997973.fasta
# SNIP run
sudo docker run -v /home/ubuntu/oucru_robot/:/data -it --rm mbull/bioinformatics-containers:phenix phenix.py run_snp_pipeline -r1 data/belson/projects/benk_genomes/fastqs/2020.08.25/Sample_50-FR10242126/50-FR10242126_CTGGAGAATA-GTTGTATGGA_L002_R1_001.fastq.gz  -r2 data/belson/projects/benk_genomes/fastqs/2020.08.25/Sample_50-FR10242126/50-FR10242126_CTGGAGAATA-GTTGTATGGA_L002_R2_001.fastq.gz -r data/home/ubuntu/LS997973.fasta -o data/sample1/phenix --keep-temp --sample-name sample1

