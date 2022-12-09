class InvalidSequence(Exception):
    pass

class DNASequence:
    def __init__(self, sequence: str):
        self._sequence = sequence.upper()

        # Note: in object orientation, we should check for consistency in constructors.
        # Constructors should build consistent (i.e. valid) objects, and throughout the lifetime of the object,
        # they have to remain valid.
        sequence_is_only_formed_of_ACGT = self._sequence.count("A") + \
                                          self._sequence.count("C") + \
                                          self._sequence.count("G") + \
                                          self._sequence.count("T") == len(self._sequence)

        if not sequence_is_only_formed_of_ACGT:
            raise InvalidSequence("Invalid sequence detected, ACGT only allowed")

    def get_sequence(self) -> str:
        return self._sequence

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
