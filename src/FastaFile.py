from src.FastaRecord import FastaRecord
from src.DNASequence import DNASequence
from src.Plasmid import Plasmid
from pathlib import Path
from typing import List

# Note: untested, add unit tests
class FastaFile:
    def __init__(self, fasta_filepath: Path):
        # TODO: this class is inefficient as it stores all Fasta records in RAM, it might not be appropriate for real
        # tools. It can be efficiently implemented using context managers (see methods __enter__ and __exit__)
        with open(fasta_filepath) as fasta_file:
            all_lines = fasta_file.readlines()
            all_lines = list(map(str.strip, all_lines))
        self.all_records = []
        for comment, sequence in zip(all_lines[::2], all_lines[1::2]):
            record = FastaRecord(comment, DNASequence(sequence))
            self.all_records.append(record)

    def get_all_plasmids(self) -> List[Plasmid]:
        all_plasmids = []
        for record in self.all_records:
            if record.is_plasmid():
                plasmid = Plasmid(record)
                all_plasmids.append(plasmid)
        return all_plasmids

    def __repr__(self):
        return f"Fasta file with {len(self.all_records)} records"
