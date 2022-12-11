from src.ProteinSequence import ProteinSequence

class NotAValidTranscript(Exception):
    pass


class Transcript:
    def __init__(self, gene, reverse: bool, frame: int):
        """
        Builds a transcript given a gene and a frame.
        :param gene: the gene itself
        :param reverse: if the transcript being built is from the forward or reverse strand of the gene
        :param frame: the gene frame (0, 1 or 2)
        """
        frame_is_valid = frame in [0, 1, 2]
        assert frame_is_valid, f"Error when building transcript, invalid frame: {frame}"

        if reverse:
            dna_sequence = gene.get_coding_sequence().get_rc()
        else:
            dna_sequence = gene.get_coding_sequence()
        dna_sequence = dna_sequence.shift(frame)
        protein_sequence = ProteinSequence(dna_sequence)

        first_start_codon_pos = protein_sequence.get_first_pos_of_aminoacid("M")
        last_stop_codon_pos = protein_sequence.get_last_pos_of_aminoacid("_")

        if Transcript.start_and_stop_codons_are_invalid(first_start_codon_pos, last_stop_codon_pos):
            raise NotAValidTranscript()

        self.protein_sequence = protein_sequence.substr(first_start_codon_pos, last_stop_codon_pos + 1)

    @staticmethod
    def build(gene, reverse: bool, frame: int):
        return Transcript(gene, reverse, frame)

    @staticmethod
    def start_and_stop_codons_are_invalid(start_codon_pos: int, stop_codon_pos: int) -> bool:
        there_is_no_start_codon = start_codon_pos == -1
        there_is_no_stop_codon = stop_codon_pos == -1
        start_codon_appears_after_stop_codon = start_codon_pos > stop_codon_pos
        return there_is_no_start_codon or there_is_no_stop_codon or start_codon_appears_after_stop_codon

    def has_PTC(self) -> bool:
        return self.protein_sequence.get_count_of_AA("_") > 1
