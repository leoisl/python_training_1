from src.FastaRecord import FastaRecord
from typing import List
from src.Gene import Gene
from constants import promoter_sequence, terminator_sequence

class Plasmid:
    def __init__(self, record: FastaRecord):
        self._record = record

    def __eq__(self, other):
        return self._record == other._record

    def __str__(self):
        return self._record.get_comment()

    def get_record(self) -> FastaRecord:
        return self._record

    def get_genes(self) -> List[Gene]:
        genes = []
        scanning_pos = 0
        while True:
            first_promoter_match_pos = self.get_record().get_sequence().get_sequence().find(promoter_sequence, scanning_pos)
            promoter_not_found = first_promoter_match_pos == -1
            if promoter_not_found:
                break

            terminator_match_pos_after_promoter = self.get_record().get_sequence().get_sequence().find(promoter_sequence,
                                                                                                  first_promoter_match_pos + 1)
            terminator_not_found = terminator_match_pos_after_promoter == -1
            if terminator_not_found:
                break

            # here, promoter and terminator were found, build and add gene
            terminator_end_pos = terminator_match_pos_after_promoter + len(terminator_sequence)
            gene = Gene(plasmid=self, start_pos=first_promoter_match_pos, end_pos=terminator_end_pos)
            genes.append(gene)
            scanning_pos = terminator_end_pos + 1

        return genes
