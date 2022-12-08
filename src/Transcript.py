from src.Gene import Gene
from src.ProteinSequence import ProteinSequence


class NotAValidTranscript(Exception):
    pass


class Transcript:
    def __init__(self, gene: Gene, reverse: bool, frame: int):
        """
        Builds a transcript given a gene and a frame.
        :param gene: the gene itself
        :param reverse: if the transcript being built is from the forward or reverse strand of the gene
        :param frame: the gene frame (0, 1 or 2)
        """
        frame_is_valid = frame in [0, 1, 2]
        assert frame_is_valid, f"Error when building transcript, invalid frame: {frame}"

        if reverse:
            dna_sequence = gene.get_sequence().get_rc()
        else:
            dna_sequence = gene.get_sequence()
        dna_sequence = dna_sequence.shift(frame)
        protein_sequence = ProteinSequence(dna_sequence)

        first_start_codon = protein_sequence.get_first_pos_of_aminoacid("M")
        last_stop_codon = protein_sequence.get_last_pos_of_aminoacid("_")
        self.protein_sequence = protein_sequence.substr(first_start_codon, last_stop_codon + 1)

        if not self.is_a_valid_transcript():
            raise NotAValidTranscript()

    def is_a_valid_transcript(self) -> bool:
        is_not_empty = len(self.protein_sequence) > 0
        starts_with_start_codon = self.protein_sequence.get_sequence()[0] == 'M'
        ends_with_stop_codon = self.protein_sequence.get_sequence()[-1] == '_'
        return is_not_empty and starts_with_start_codon and ends_with_stop_codon

    def has_PTC(self) -> bool:
        return self.protein_sequence.get_count_of_AA("_") > 1
