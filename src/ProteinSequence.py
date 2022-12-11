from src.DNASequence import DNASequence

class ProteinSequence:
    @staticmethod
    def _translate(dna_sequence: str) -> str:
        translation_table = {
            'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
            'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
            'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
            'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
            'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
            'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
            'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
            'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
            'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
            'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
            'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
            'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
            'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
            'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
            'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
            'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W',
        }
        protein = ""  # TODO: string concatenation in python is inefficient. Find out why and how to improve.
        for i in range(0, len(dna_sequence), 3):
            codon = dna_sequence[i:i + 3]
            is_full_codon = len(codon) == 3
            if is_full_codon:
                protein += translation_table[codon]
        return protein

    def __init__(self, sequence: DNASequence):
        self._sequence = ProteinSequence._translate(sequence.get_sequence())

    def get_sequence(self) -> str:
        return self._sequence

    def get_first_pos_of_aminoacid(self, aminoacid: str) -> int:
        return self._sequence.find(aminoacid)

    def get_last_pos_of_aminoacid(self, aminoacid: str) -> int:
        return self._sequence.rfind(aminoacid)

    def substr(self, first_pos, last_pos):
        return self._sequence[first_pos:last_pos]

    def __len__(self):
        return len(self._sequence)

    def __str__(self):
        return self._sequence
