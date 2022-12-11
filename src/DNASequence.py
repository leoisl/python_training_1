class DNASequence:
    def __init__(self, sequence: str):
        self._sequence = sequence

    def get_sequence(self) -> str:
        return self._sequence

    def __eq__(self, other):
        return self._sequence == other._sequence

    def get_rc(self) -> "DNASequence":
        """
        :return: a reverse-complemented sequence
        """
        complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        comp_sequence = [complement.get(base) for base in self._sequence]
        rev_comp_sequence = reversed(comp_sequence)
        return DNASequence("".join(rev_comp_sequence))

    def shift(self, amount: int):
        """
        Returns a new shifted DNA sequence
        :param amount: Amount of bases to shift
        """
        return DNASequence(self._sequence[amount:])

    def __str__(self):
        return self.get_sequence()