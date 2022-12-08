from src.DNASequence import DNASequence

class FastaRecord:
    def __init__(self, comment: str, sequence: DNASequence):
        self._comment = comment
        self._sequence = sequence

    def __eq__(self, other):
        return (self._comment, self._sequence) == (other._comment, other._sequence)

    def is_plasmid(self) -> bool:
        return "plasmid" in self._comment or "plm" in self._comment

    def get_sequence(self) -> DNASequence:
        return self._sequence

    def get_comment(self) -> str:
        return self._comment