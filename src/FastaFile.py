from src.FastaRecord import FastaRecord
from src.Plasmid import Plasmid
from pathlib import Path
from typing import List

class FastaFile:
    def __init__(self, fasta_filepath: Path):
        # TODO: this class is inefficient as it stores all Fasta records in RAM, it might not be appropriate for real
        # tools. It can be efficiently implemented using context managers (see methods __enter__ and __exit__)
        with open(fasta_filepath) as fasta_file:
            self.all_records = []
            for comment, sequence in zip(fasta_file.readline(), fasta_file.readline()):
                record = FastaRecord(comment, sequence)
                self.all_records.append(record)

    def __eq__(self, other):
        return self.all_records == other.all_records

    def get_all_records(self) -> List[FastaRecord]:
        return self.all_records

    def get_all_plasmids(self) -> List[Plasmid]:
        all_plasmids = []
        for record in self.get_all_records():
            if record.is_plasmid():
                plasmid = Plasmid(record)
                all_plasmids.append(plasmid)
        return all_plasmids
