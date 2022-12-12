from src.FastaRecord import FastaRecord
from typing import List
from src.Gene import Gene
from src.constants import promoter_sequence, terminator_sequence

class Plasmid:
    def __init__(self, record: FastaRecord):
        self._record = record

    def __str__(self):
        return self._record.get_comment()

    def __repr__(self):
        return str(self)

    def get_record(self) -> FastaRecord:
        return self._record

    def _find_promoter(self, from_pos):
        return self.get_record().get_sequence().get_sequence().find(promoter_sequence, from_pos)

    def _find_terminator(self, from_pos):
        return self.get_record().get_sequence().get_sequence().find(terminator_sequence, from_pos)

    def get_genes(self) -> List[Gene]:
        genes = []
        scanning_pos = 0
        while True:
            first_promoter_match_pos = self._find_promoter(scanning_pos)
            promoter_not_found = first_promoter_match_pos == -1
            if promoter_not_found:
                break

            terminator_match_pos_after_promoter = self._find_terminator(first_promoter_match_pos + 1)
            terminator_not_found = terminator_match_pos_after_promoter == -1
            if terminator_not_found:
                break

            # here, promoter and terminator were found, build and add gene
            terminator_end_pos = terminator_match_pos_after_promoter + len(terminator_sequence)
            gene = Gene(plasmid=self, start_pos=first_promoter_match_pos, end_pos=terminator_end_pos)
            genes.append(gene)
            scanning_pos = terminator_end_pos + 1

        return genes
