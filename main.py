import argparse
from src.FastaFile import FastaFile


def main():
    parser = argparse.ArgumentParser(description='Parse a fasta file and output which genes can be expressed from plasmid sequences.')
    parser.add_argument('fasta_file', help='The fasta file to be parsed')
    args = parser.parse_args()

    fasta_file = FastaFile(args.fasta_file)
    all_plasmids = fasta_file.get_all_plasmids()
    for plasmid in all_plasmids:
        print(f"Processing plasmid {plasmid}")
        for gene in plasmid.get_genes():
            if gene.is_expressed():
                print(f"Gene {gene} can be expressed")
            else:
                print(f"Gene {gene} will NOT be expressed")

if __name__ == "__main__":
    main()
